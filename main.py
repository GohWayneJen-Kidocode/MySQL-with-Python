import mysql.connector
from datetime import datetime

db = mysql.connector.connect(host="localhost", user="root", password="ScoolL", database="testdatabase")

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint, personId int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("DESCRIBE Person")

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("Tim", 19))
# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("Tim", 19))
# db.commit()

# for x in mycursor:
#     print(x)

# mycursor.execute("SELECT * FROM Person")

# for x in mycursor:
#     print(x)

# mycursor.execute("DROP TABLE Person")

# mycursor.execute("CREATE TABLE Test (name varchar(50), created datetime, gender ENUM('M', 'F', 'O'))")
# mycursor.execute("ALTER TABLE Test ADD id int PRIMARY KEY NOT NULL AUTO_INCREMENT")
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Tim", datetime.now(), 'M'))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Wayne", datetime.now(), 'M'))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Audrey", datetime.now(), 'F'))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Cathulu", datetime.now(), 'O'))


# db.commit()

# mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id ASC")

# for x in mycursor:
#     print(x)

# mycursor.execute("DROP TABLE Test")


# users = [("Wayne", "Kido6099", "hello", "kidosol6099@gmail.com"), ("Tim", "TimmyBoy", "Pizza12", "Tim@gmail.com")]
# user_scores = [(10, 14), (12, 13)]
# Q1 = "CREATE TABLE Users(id int PRIMARY KEY AUTO_INCREMENT, name varchar(50), passwd varchar(50)"
# Q2 = "CREATE TABLE Scores(id int PRIMARY KEY  AUTO_INCREMENT, FOREIGN KEY(userId) REFERENCES Users(id), int game1 DEFAULT 0, int game2 DEFAULT 0"

# mycursor.execute(Q1)
# mycursor.execute(Q2)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# Q3 = "INSERT INTO Users(name, passwd) VALUES (%s,%s)"
# Q4 = "INSERT INTO Scores(userId, game1, game2) VALUES(%s,%s,%s)"

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,) + user_scores[x])

# mycursor.execute("SELECT * FROM Users")
# for x in mycursor:
#     print(x)

# mycursor.execute("SELECT * FROM Scores")
# for x in mycursor:
#     print(x)