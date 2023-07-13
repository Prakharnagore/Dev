import mysql.connector

def datatoget(name,email,confirm):

    mydb = mysql.connector.connect(host="localhost",port='3308',user="root", passwd="saurav1988",database='hotelsbot')

    mycursor = mydb.cursor()

   # sql = "CREATE TABLE Feedback (Name VARCHAR(255),Fromdate VARCHAR(255),Todate VARCHAR(255),rooms int(24))"

    sqls = 'INSERT INTO hotelconfirm (name,email,confirmnumber) VALUES ("{0}","{1}","{2}");'.format(name, email, confirm)

    mycursor.execute(sqls)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")


if __name__ == "__main__":
    datatoget("Ashish", "eshaan201@gmail.com","1e2f")
