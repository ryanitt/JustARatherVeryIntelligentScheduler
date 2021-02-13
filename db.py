import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mainAd",
  password="K3nnyisjeonmayer",
  database="jarvisfc"
)


mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

created = False


for x in mycursor:
    if(x[0] == 'meetings'):
        created = True

if not created:
    mycursor.execute("CREATE TABLE meetings (topic VARCHAR(255), time DATETIME)")
    print('created meetings')

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)