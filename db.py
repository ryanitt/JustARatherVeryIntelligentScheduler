import mysql.connector
import datetime
class DataBase:

    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="mainAd",
                    password="K3nnyisjeonmayer",
                    database="jarvisfc"
                    )
        self.mycursor = self.mydb.cursor()

    def saveToDB(self):
        self.mycursor.execute("COMMIT;")


    def createMeetingsTable(self):
        created = False
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            if(x[0] == 'meetings'):
                created = True

        if not created:
            self.mycursor.execute("CREATE TABLE meetings (\
                            id INTEGER NOT NULL AUTO_INCREMENT,\
                            topic VARCHAR(255),\
                            time DATETIME,\
                            PRIMARY KEY (id)\
                            );")
            print('created meetings')

    def createPersonsTable(self):
        created = False
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            if(x[0] == 'persons'):
                created = True

        if not created:
            self.mycursor.execute("CREATE TABLE persons (\
                            id INTEGER NOT NULL AUTO_INCREMENT,\
                            discord VARCHAR(255),\
                            tag INTEGER,\
                            PRIMARY KEY (id)\
                            );")
            print('created persons')

    def createTables(self):
        self.createMeetingsTable()
        self.createPersonsTable()

    def createMeeting(self, topic, Y, M, D, h, m):
        meeting_date = datetime.datetime(Y, M, D, hour=h, minute=m).strftime('%Y-%m-%d %H:%M:%S')
        print(meeting_date)
        sql = "INSERT INTO meetings (topic, time) VALUES (%s, %s);"
        val = (topic, meeting_date)
        self.mycursor.execute(sql, val)
        
    def createPerson(self, disc, tag):
        sql = "INSERT INTO persons (discord, tag) VALUES (%s, %s)"
        val = (disc, tag)
        print(sql, val)
        self.mycursor.execute(sql, val)

    def showInfo(self):
        self.mycursor.execute("SELECT * FROM meetings")
        for x in self.mycursor:
            print(x)

        self.mycursor.execute("SELECT * FROM persons")
        for x in self.mycursor:
            print(x)



if __name__ == "__main__":
    db = DataBase()
    db.createTables()
    db.createMeeting("meeting 1", 1997, 1, 31, 13, 45)
    db.createMeeting("meeting 2", 1998, 2, 1, 7, 30)
    db.createMeeting("meeting 3", 1999, 3, 2, 2, 00)
    db.createMeeting("meeting 4", 2000, 4, 3, 15, 15)
    db.createPerson("Question", "0874")
    db.createPerson("Rice", "2405")
    db.createPerson("FunkyPants4457", "6186")
    db.createPerson("chendaddy15", "6336")
    db.createPerson("Kurozinx", "7652")

    db.showInfo()
    db.saveToDB()
