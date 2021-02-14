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
                            name VARCHAR(255),\
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

    def createAttendenceTable(self):
        created = False
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            if(x[0] == 'attendence'):
                created = True

        if not created:
            self.mycursor.execute("CREATE TABLE attendence (\
                            pNo INTEGER,\
                            mNo INTEGER,\
                            PRIMARY KEY (pNo, mNo),\
                            FOREIGN KEY(pNo) REFERENCES persons(id),\
                            FOREIGN KEY(mNo) REFERENCES meetings(id)\
                            );")      
            print('created attendence')

    def createTables(self):
        self.createMeetingsTable()
        self.createPersonsTable()
        self.createAttendenceTable()

    def createMeeting(self, name, Y, M, D, h, m):
        meeting_date = datetime.datetime(Y, M, D, hour=h, minute=m).strftime('%Y-%m-%d %H:%M:%S')
        print(meeting_date)
        sql = "INSERT INTO meetings (name, time) VALUES (%s, %s);"
        val = (name, meeting_date)
        self.mycursor.execute(sql, val)
        
    def createPerson(self, disc, tag):
        sql = "INSERT INTO persons (discord, tag) VALUES (%s, %s)"
        val = (disc, tag)
        print(sql, val)
        self.mycursor.execute(sql, val)

    def createAttendence(self, disc, tag, name):
        sql  = "SELECT * FROM meetings WHERE name = %s"
        tpc = (name,)
        self.mycursor.execute(sql, tpc)
        meeting = self.mycursor.fetchone()
        print(meeting)

        sql  = "SELECT * FROM persons WHERE discord = %s AND tag = %s"
        val = (disc, tag)
        self.mycursor.execute(sql, val)
        person = self.mycursor.fetchone()
        print(person)

        sql = "INSERT INTO attendence (pNo, mNo) VALUES (%s, %s)"
        val = (person[0], meeting[0])
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
    # db.createMeeting("meeting 1", 1997, 1, 31, 13, 45)
    # db.createMeeting("meeting 2", 1998, 2, 1, 7, 30)
    # db.createMeeting("meeting 3", 1999, 3, 2, 2, 00)
    # db.createMeeting("meeting 4", 2000, 4, 3, 15, 15)
    # db.createPerson("Question", "0874")
    # db.createPerson("Rice", "2405")
    # db.createPerson("FunkyPants4457", "6186")
    # db.createPerson("chendaddy15", "6336")
    # db.createPerson("Kurozinx", "7652")
    db.createAttendence("Rice", "2405", "meeting 1")
    db.showInfo()
    db.saveToDB()
