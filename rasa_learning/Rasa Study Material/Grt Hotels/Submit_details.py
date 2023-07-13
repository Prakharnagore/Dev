import mysql.connector

def dataupdate(Name,Fromdate,Todate,rooms,email):

    mydb = mysql.connector.connect(host="localhost",port='3306',user="root", passwd="saurav1988",database='hotelsbot')

    mycursor = mydb.cursor()

   # sql = "CREATE TABLE Feedback (Name VARCHAR(255),Fromdate VARCHAR(255),Todate VARCHAR(255),rooms int(24))"

    sql = 'INSERT INTO hotels (Name,Fromdate,Todate,rooms,email) VALUES ("{0}","{1}","{2}","{3}","{4}");'.format(Name, Fromdate, Todate, rooms, email)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")


if __name__ == "__main__":
    dataupdate("Ashish", "may", "june", "2","eshaan201@gmail.com")
