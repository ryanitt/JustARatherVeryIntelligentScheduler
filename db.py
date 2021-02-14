import mysql.connector
import datetime
class DataBase:

    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Bestintentions56*",
                    database="jarvisfc"
                    )
        self.mycursor = self.mydb.cursor(buffered=True)

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
                            name VARCHAR(255) UNIQUE,\
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
                            clientID VARCHAR(255),\
                            PRIMARY KEY (clientID)\
                            );")
            print('created persons')

    def createAttendanceTable(self):
        created = False
        self.mycursor.execute("SHOW TABLES")
        for x in self.mycursor:
            if(x[0] == 'attendance'):
                created = True

        if not created:
            self.mycursor.execute("CREATE TABLE attendance (\
                            pNo VARCHAR(255),\
                            mNo INTEGER,\
                            PRIMARY KEY (pNo, mNo),\
                            FOREIGN KEY(mNo) REFERENCES meetings(id)\
                            );")      
            print('created attendance')

    def createTables(self):
        self.createMeetingsTable()
        self.createPersonsTable()
        self.createAttendanceTable()

    # def createMeeting(self, name, Y, M, D, h, m):
    #     meeting_date = datetime.datetime(Y, M, D, hour=h, minute=m).strftime('%Y-%m-%d %H:%M:%S')
    #     print(meeting_date)
    #     sql = "INSERT INTO meetings (name, time) VALUES (%s, %s);"
    #     val = (name, meeting_date)
    #     self.mycursor.execute(sql, val)

    def createMeeting(self, name, time):
        sql = "SELECT * FROM meetings WHERE name = %s"
        val = (name,)
        self.mycursor.execute(sql, val)

        if(self.mycursor.rowcount > 0):
            print("meeting already exists: ", name)
            return

        sql = "INSERT INTO meetings (name, time) VALUES (%s, %s);"
        val = (name, time)
        self.mycursor.execute(sql, val)

    def createPerson(self, disc):
        if disc[0:3] != "<@!":
            print("not a valid client ID: ", disc)
            return
        sql = "SELECT * FROM persons WHERE clientID = %s"
        val = (disc,)
        self.mycursor.execute(sql, val)

        if(self.mycursor.rowcount > 0):
            print("person already exists: ", disc)
            return


        sql = "INSERT INTO persons (clientID) VALUES (%s)"
        val = (disc,)
        print(sql, val)
        self.mycursor.execute(sql, val)

    def createAttendance(self, disc, meetingName):
        sql  = "SELECT * FROM meetings WHERE name = %s"
        tpc = (meetingName,)
        self.mycursor.execute(sql, tpc)
        meeting = self.mycursor.fetchone()
        print(meeting)

        sql = "INSERT INTO attendance (pNo, mNo) VALUES (%s, %s)"
        val = (disc, meeting[0])
        print(sql, val)
        self.mycursor.execute(sql, val)

    def showInfo(self):
        self.mycursor.execute("SELECT * FROM meetings")
        for x in self.mycursor:
            print(x)

        self.mycursor.execute("SELECT * FROM persons")
        for x in self.mycursor:
            print(x)

    def displayMeetings(self):
        self.mycursor.execute("SELECT * FROM meetings ORDER BY time")
        returnStr = ""
        for x in self.mycursor:
            x = list(x)
            returnStr = returnStr + x[1] + " " + x[2].strftime("%m/%d/%Y, %H:%M") + "\n"
        
        return returnStr.rstrip()



if __name__ == "__main__":
    db = DataBase()
    db.createTables()
    db.createMeeting("test", datetime.datetime(2021, 2, 14, hour=16, minute=30).strftime('%Y-%m-%d %H:%M:%S'))
    db.createMeeting("testLater", datetime.datetime(2021, 3, 14, hour=16, minute=30).strftime('%Y-%m-%d %H:%M:%S'))
    # db.createMeeting("meeting 2", 1998, 2, 1, 7, 30)
    # db.createMeeting("meeting 3", 1999, 3, 2, 2, 00)
    # db.createMeeting("meeting 4", 2000, 4, 3, 15, 15)
    # db.createPerson("<@!103683474916925440>")
    # db.createPerson("<@!216745727857131520>")
    # db.createPerson("<@!128311377767956481>")
    
    # db.createAttendance("<@!103683474916925440>", "meeting 1")
    # db.createAttendance("<@!216745727857131520>", "meeting 3")
    # db.createAttendance("<@!128311377767956481>", "meeting 2")
    # db.createAttendance("<@!216745727857131520>", "meeting 4")
    # db.showInfo()
    # db.saveToDB()
    print(db.displayMeetings())
