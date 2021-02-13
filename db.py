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


    def createMeeting(self, topic, Y, M, D, h, m):
        meeting_date = datetime.datetime(Y, M, D, hour=h, minute=m).strftime('%Y-%m-%d %H:%M:%S')
        print(meeting_date)
        sql = "INSERT INTO meetings (topic, time) VALUES (%s, %s)"
        val = (topic, meeting_date)
        self.mycursor.execute(sql, val)


    def showMeetings(self):
        self.mycursor.execute("SELECT * FROM meetings")

        for x in self.mycursor:
            print(x)



if __name__ == "__main__":
    db = DataBase()
    # db.createMeetingsTable()
    db.createMeeting("your dad", 1997, 1, 31, 13, 45)
    db.showMeetings()
