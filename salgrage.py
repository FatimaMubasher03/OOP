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

    def close_connection(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = SalGradeDB('salgrade.db')
    
    # Create a SalGrade instance
    grade1 = SalGrade(6, 40000, 50000)
    
    # Create
    db.create_salgrade(grade1)
    
    # Read
    retrieved_grade = db.read_salgrade(6)
    print(retrieved_grade.grade, retrieved_grade.losal, retrieved_grade.hisal)
    
    # Update
    grade1.losal = 45000
    grade1.hisal = 55000
    db.update_salgrade(grade1)
    updated_grade = db.read_salgrade(6)
    print(updated_grade.grade, updated_grade.losal, updated_grade.hisal)
    
    # Delete
    db.delete_salgrade(6)
    deleted_grade = db.read_salgrade(6)
    print(deleted_grade)
    
    db.close_connection()
