# dbms_mysql.py
import pymysql

# MySQL 서버에 연결하는 함수
conn = pymysql.connect(
    host = "localhost",      # MySQL 서버 주소 # IP주소 쓰는데 보통 같은 컴이면 localhost 씀   
    user="root",
    password = "3758",
    database = "exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor      # cursorclass 지정 안해주면 tuple 형태로 저장
)

# 커서 생성 => (DB와 관련된) 명령어 작성할 수 있음
cursor = conn.cursor()

# 커서를 통해 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한번 호출에 하나의 row를 가져올 때 사용하는 함수
print("현재 데이터베이스 fetchone : ", cursor.fetchone())       # 한번에 하나
print("현재 데이터베이스 fetchall : ", cursor.fetchall())       # 한번에 전부 출력
print("현재 데이터베이스 fetchmany: ", cursor.fetchmany())      # 갯수 지정해서 출력


# 서버 연결 해제 함수
conn.close()