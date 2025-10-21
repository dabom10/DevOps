# dbms_mysql.py
import pymysql

# MySQL 서버에 연결하는 함수
conn = pymysql.connect(
    host = "localhost",
    user="root",
    password = "3758",
    database = "exampledb",
)

# 커서 생성 => (DB와 관련된) 명령어 작성할 수 있음
cursor = conn.cursor()

# 커서를 통해 명령어 실행
sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)
print('데이터 조회 완료')
# 서버 연결 해제 함수
conn.close()

