import mysql.connector
import http.server
import socketserver

connection = mysql.connector.connect(
    user='root',password='root', host='mysql', port="3306", database='db')

cursor = connection.cursor()
cursor.execute('Select * FROM users')
users = cursor.fetchall()
connection.close()
print(users)

f = open("index.html", "w")
for user in users:
    for element in user:
        f.write(f"{element} ")
    f.write("\n")
f.close()
    


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1234), handler) as httpd:
    httpd.serve_forever()
print("end")
while(1):
    pass




