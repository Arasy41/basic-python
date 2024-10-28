import mysql.connector as mysql
host = "localhost"
user = "root"
passwd = ""
port = 3307
# menghubungkan Python dengan MySQL
db = mysql.connect(
 host=host,
 user=user,
 passwd= passwd,
 port=port
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE data_siswa_smk")
db.database ="data_siswa_smk"

cursor = db.cursor()
cursor.execute("SHOW TABLES")
data = cursor.fetchall()
print(data)
