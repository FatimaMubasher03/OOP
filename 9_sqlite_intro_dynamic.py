import sqlite3 as dbms

con = dbms.connect('abc.db')

cur = con.cursor()

# one time task
#cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")

r = 'BSDSF22M088'
n = 'Zafar'
d = 'DS'
s = 99

cur = con.execute("insert into student (semester, rollno, stname, deptno) values(?,?,?,?)", (s, r,n,d))
con.commit()

print(cur.rowcount)

cur.execute("SELECT rollno, stname, deptno, semester FROM student")
for row in cur:
    print(row)

cur.close()
con.close()
