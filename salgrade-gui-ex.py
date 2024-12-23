import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import sqlite3

class SalGrade:
    def __init__(self, grade, losal, hisal):
        self.grade = grade
        self.losal = losal
        self.hisal = hisal

class SalGradeDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS SALGRADE
                               (GRADE DECIMAL,
                               LOSAL DECIMAL,
                               HISAL DECIMAL)''')
        self.conn.commit()

    def create_salgrade(self, salgrade):
        self.cursor.execute("INSERT INTO SALGRADE (GRADE, LOSAL, HISAL) VALUES (?, ?, ?)",
                            (salgrade.grade, salgrade.losal, salgrade.hisal))
        self.conn.commit()

    def read_salgrade(self, grade):
        self.cursor.execute("SELECT * FROM SALGRADE WHERE GRADE=?", (grade,))
        row = self.cursor.fetchone()
        if row:
            return SalGrade(row[0], row[1], row[2])
        else:
            return None

    def update_salgrade(self, salgrade):
        self.cursor.execute("UPDATE SALGRADE SET LOSAL=?, HISAL=? WHERE GRADE=?",
                            (salgrade.losal, salgrade.hisal, salgrade.grade))
        self.conn.commit()

    def delete_salgrade(self, grade):
        self.cursor.execute("DELETE FROM SALGRADE WHERE GRADE=?", (grade,))
        self.conn.commit()

    def get_all_salgrades(self):
        self.cursor.execute("SELECT * FROM SALGRADE")
        rows = self.cursor.fetchall()
        salgrades = [SalGrade(row[0], row[1], row[2]) for row in rows]
        return salgrades

    def filter_salgrades(self, min_losal, max_losal):
        self.cursor.execute("SELECT * FROM SALGRADE WHERE LOSAL BETWEEN ? AND ?", (min_losal, max_losal))
        rows = self.cursor.fetchall()
        salgrades = [SalGrade(row[0], row[1], row[2]) for row in rows]
        return salgrades

    def sort_salgrades(self, key):
        self.cursor.execute("SELECT * FROM SALGRADE ORDER BY " + key)
        rows = self.cursor.fetchall()
        salgrades = [SalGrade(row[0], row[1], row[2]) for row in rows]
        return salgrades

    def close_connection(self):
        self.conn.close()

class Application(tk.Tk):
    def __init__(self, db_file):
        super().__init__()
        self.title("SalGrade Management System")
        self.db = SalGradeDB(db_file)

        self.create_widgets()

    def create_widgets(self):
        self.record_nav_frame = ttk.Frame(self)
        self.record_nav_frame.pack(fill=tk.X, padx=10, pady=5)

        self.grade_label = ttk.Label(self.record_nav_frame, text="Grade:")
        self.grade_label.grid(row=0, column=0, padx=5, pady=5)
        self.grade_entry = ttk.Entry(self.record_nav_frame, width=10)
        self.grade_entry.grid(row=0, column=1, padx=5, pady=5)

        self.nav_buttons_frame = ttk.Frame(self.record_nav_frame)
        self.nav_buttons_frame.grid(row=0, column=2, padx=5, pady=5)

        self.prev_button = ttk.Button(self.nav_buttons_frame, text="Prev", command=self.prev_record)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.next_button = ttk.Button(self.nav_buttons_frame, text="Next", command=self.next_record)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.record_details_frame = ttk.Frame(self)
        self.record_details_frame.pack(fill=tk.X, padx=10, pady=5)

        self.losal_label = ttk.Label(self.record_details_frame, text="Lowest Salary:")
        self.losal_label.grid(row=0, column=0, padx=5, pady=5)
        self.losal_entry = ttk.Entry(self.record_details_frame, width=10)
        self.losal_entry.grid(row=0, column=1, padx=5, pady=5)

        self.hisal_label = ttk.Label(self.record_details_frame, text="Highest Salary:")
        self.hisal_label.grid(row=0, column=2, padx=5, pady=5)
        self.hisal_entry = ttk.Entry(self.record_details_frame, width=10)
        self.hisal_entry.grid(row=0, column=3, padx=5, pady=5)

        self.crud_buttons_frame = ttk.Frame(self)
        self.crud_buttons_frame.pack(fill=tk.X, padx=10, pady=5)

        self.create_button = ttk.Button(self.crud_buttons_frame, text="Create", command=self.create_grade)
        self.create_button.pack(side=tk.LEFT, padx=5)
        self.read_button = ttk.Button(self.crud_buttons_frame, text="Read", command=self.read_grade)
        self.read_button.pack(side=tk.LEFT, padx=5)
        self.update_button = ttk.Button(self.crud_buttons_frame, text="Update", command=self.update_grade)
        self.update_button.pack(side=tk.LEFT, padx=5)
        self.delete_button = ttk.Button(self.crud_buttons_frame, text="Delete", command=self.delete_grade)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.list_all_button = ttk.Button(self, text="List All", command=self.list_all)
        self.list_all_button.pack(fill=tk.X, padx=10, pady=5)

        self.filter_frame = ttk.Frame(self)
        self.filter_frame.pack(fill=tk.X, padx=10, pady=5)

        self.min_losal_label = ttk.Label(self.filter_frame, text="Min Lowest Salary:")
        self.min_losal_label.grid(row=0, column=0, padx=5, pady=5)
        self.min_losal_entry = ttk.Entry(self.filter_frame, width=10)
        self.min_losal_entry.grid(row=0, column=1, padx=5, pady=5)

        self.max_losal_label = ttk.Label(self.filter_frame, text="Max Lowest Salary:")
        self.max_losal_label.grid(row=0, column=2, padx=5, pady=5)
        self.max_losal_entry = ttk.Entry(self.filter_frame, width=10)
        self.max_losal_entry.grid(row=0, column=3, padx=5, pady=5)

        self.filter_button = ttk.Button(self.filter_frame, text="Filter", command=self.filter_salgrades)
        self.filter_button.grid(row=0, column=4, padx=5, pady=5)

        self.sort_frame = ttk.Frame(self)
        self.sort_frame.pack(fill=tk.X, padx=10, pady=5)

        self.sort_label = ttk.Label(self.sort_frame, text="Sort by:")
        self.sort_label.grid(row=0, column=0, padx=5, pady=5)
        self.sort_var = tk.StringVar()
        self.sort_combobox = ttk.Combobox(self.sort_frame, textvariable=self.sort_var, values=["GRADE", "LOSAL", "HISAL"])
        self.sort_combobox.current(0)
        self.sort_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.sort_button = ttk.Button(self.sort_frame, text="Sort", command=self.sort_salgrades)
        self.sort_button.grid(row=0, column=2, padx=5, pady=5)

        self.print_pdf_button = ttk.Button(self, text="Print to PDF", command=self.print_to_pdf)
        self.print_pdf_button.pack(fill=tk.X, padx=10, pady=5)

        self.current_record = 0
        self.total_records = len(self.db.get_all_salgrades())
        self.update_nav_buttons_state()

    def update_nav_buttons_state(self):
        self.prev_button.config(state=tk.NORMAL if self.current_record > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_record < self.total_records - 1 else tk.DISABLED)

    def prev_record(self):
        if self.current_record > 0:
            self.current_record -= 1
            self.update_record_fields()

    def next_record(self):
        if self.current_record < self.total_records - 1:
            self.current_record += 1
            self.update_record_fields()

    def update_record_fields(self):
        salgrades = self.db.get_all_salgrades()
        salgrade = salgrades[self.current_record]
        self.grade_entry.delete(0, tk.END)
        self.grade_entry.insert(0, str(salgrade.grade))
        self.losal_entry.delete(0, tk.END)
        self.losal_entry.insert(0, str(salgrade.losal))
        self.hisal_entry.delete(0, tk.END)
        self.hisal_entry.insert(0, str(salgrade.hisal))
        self.update_nav_buttons_state()

    def create_grade(self):
        grade = float(self.grade_entry.get())
        losal = float(self.losal_entry.get())
        hisal = float(self.hisal_entry.get())
        new_grade = SalGrade(grade, losal, hisal)
        self.db.create_salgrade(new_grade)
        messagebox.showinfo("Success", "Grade {} created successfully.".format(grade))
        self.current_record = len(self.db.get_all_salgrades()) - 1
        self.update_record_fields()

    def read_grade(self):
        grade = float(self.grade_entry.get())
        salgrade = self.db.read_salgrade(grade)
        if salgrade:
            messagebox.showinfo("Grade Details", "Grade: {}\nLowest Salary: {}\nHighest Salary: {}".format(salgrade.grade, salgrade.losal, salgrade.hisal))
        else:
            messagebox.showerror("Error", "Grade {} not found.".format(grade))

    def update_grade(self):
        grade = float(self.grade_entry.get())
        losal = float(self.losal_entry.get())
        hisal = float(self.hisal_entry.get())
        updated_grade = SalGrade(grade, losal, hisal)
        self.db.update_salgrade(updated_grade)
        messagebox.showinfo("Success", "Grade {} updated successfully.".format(grade))

    def delete_grade(self):
        grade = float(self.grade_entry.get())
        self.db.delete_salgrade(grade)
        messagebox.showinfo("Success", "Grade {} deleted successfully.".format(grade))
        self.total_records -= 1
        self.current_record = min(self.current_record, self.total_records - 1)
        self.update_record_fields()

    def list_all(self):
        salgrades = self.db.get_all_salgrades()
        if salgrades:
            salgrades_str = "\n".join(["Grade: {}, Lowest Salary: {}, Highest Salary: {}".format(s.grade, s.losal, s.hisal) for s in salgrades])
            messagebox.showinfo("All Grades", salgrades_str)
        else:
            messagebox.showinfo("No Records", "No records found.")

    def filter_salgrades(self):
        min_losal = float(self.min_losal_entry.get())
        max_losal = float(self.max_losal_entry.get())
        salgrades = self.db.filter_salgrades(min_losal, max_losal)
        if salgrades:
            salgrades_str = "\n".join(["Grade: {}, Lowest Salary: {}, Highest Salary: {}".format(s.grade, s.losal, s.hisal) for s in salgrades])
            messagebox.showinfo("Filtered Grades", salgrades_str)
        else:
            messagebox.showinfo("No Records", "No records found in the specified range.")

    def sort_salgrades(self):
        key = self.sort_var.get()
        salgrades = self.db.sort_salgrades(key)
        if salgrades:
            salgrades_str = "\n".join(["Grade: {}, Lowest Salary: {}, Highest Salary: {}".format(s.grade, s.losal, s.hisal) for s in salgrades])
            messagebox.showinfo("Sorted Grades", salgrades_str)
        else:
            messagebox.showinfo("No Records", "No records found.")

    def print_to_pdf(self):
        salgrades = self.db.get_all_salgrades()
        if salgrades:
            data = [["Grade", "Lowest Salary", "Highest Salary"]]
            for s in salgrades:
                data.append([str(s.grade), str(s.losal), str(s.hisal)])
            
            pdf_filename = "salgrades.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
            table = Table(data)
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])
            table.setStyle(style)
            doc.build([table])
        else:
            messagebox.showinfo("No Records", "No records found.")

if __name__ == "__main__":
    app = Application('salgrade.db')
    app.mainloop()
