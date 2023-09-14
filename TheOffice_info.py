# # 1, Import libraries:
import mysql.connector
from mysql.connector import Error

#
# # # # __________________________________________
# # #
# # #
# 2. Connects to the MySQL database server:
def create_connection(host_name, user_name, user_password, unix_socket, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            unix_socket=unix_socket
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "root", "/Applications/MAMP/tmp/mysql/mysql.sock", db_name="TheOffice_info")

# # #
# # # # __________________________________________
# # #
# #
# 3. Create the database:
# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# create_database_query = "CREATE DATABASE TheOffice_info"
# create_database(connection, create_database_query)

#
# __________________________________________
#
#
##4. Create function to excute queries:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
# #
##Create queries for creating tables:

# create_Employees_table = """
# CREATE TABLE IF NOT EXISTS Employees (
#   id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age INT,
#   gender TEXT,
#   nationality TEXT,
#   specialty TEXT,
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
#
# create_Positions_table = """
# CREATE TABLE IF NOT EXISTS Positions (
#   id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   job TEXT,
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
# #
# create_EmplPositions_table = """
# CREATE TABLE IF NOT EXISTS EmplPositions (
#   id INT AUTO_INCREMENT,
#   emply_id INT NOT NULL,
#   Positions_id INT NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees(id),
#   FOREIGN KEY (Positions_id) REFERENCES Positions(id),
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
# #
# create_Department_table = """
# CREATE TABLE IF NOT EXISTS Department (
#   id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   salary INT NOT NULL,
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
#
#
# create_EmplDepartment_table = """
# CREATE TABLE IF NOT EXISTS EmplDepartment (
#   id INT AUTO_INCREMENT,
#   emply_id INT NOT NULL,
#   Dep_id INT NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees(id),
#   FOREIGN KEY (Dep_id) REFERENCES Department(id),
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
#
# create_EmplRate_table = """
# CREATE TABLE IF NOT EXISTS EmplRate (
#   id INT AUTO_INCREMENT,
#   emply_id INT NOT NULL,
#   rate_id INT NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees(id),
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
# execute_query(connection, create_Employees_table)
# execute_query(connection, create_Positions_table)
# execute_query(connection, create_EmplPositions_table)
# execute_query(connection, create_Department_table)
# execute_query(connection, create_EmplDepartment_table)
# execute_query(connection, create_EmplRate_table)
#
#
# # # ___________________________________________________
# #4. Create INSERT queries:
#
# create_Employees_query = """
# INSERT INTO Employees (name, age, gender, nationality, specialty) VALUES (%s, %s, %s, %s, %s)
# """
# Employees_val = [
#     ('Michael', 45, 'male', 'USA', 'MIS'),
#     ('Pam', 30, 'female', 'USA', 'IT'),
#     ('Jim', 27, 'male', 'England', 'CS'),
#     ('Meredith', 50, 'female', 'France', 'LANGUAGE'),
#     ('Dwight', 31, 'male', 'Germany', 'HISTORY')
# ]
#
# cursor = connection.cursor()
# cursor.executemany(create_Employees_query, Employees_val)
# connection.commit()
#
# create_Positions_query = """
# INSERT INTO Positions (name, job) VALUES (%s, %s)
# """
# Positions_val = [
#     ("Michael", "Regional Manager"),
#     ("Pam", "Receptionist"),
#     ("Jim", "Salesman"),
#     ("Meredith", "Accountant"),
#     ("Dwight", "Assurance Manager")
# ]
#
# cursor = connection.cursor()
# cursor.executemany(create_Positions_query, Positions_val)
# connection.commit()
#
#
#
#
#
# # #
# create_EmplPositions_query = "INSERT INTO EmplPositions (emply_id, Positions_id) VALUES (%s, %s)"
# EmplPositions_val = [
#     (1, 1),  # Assuming these are the employee and position IDs
#     (2, 2),
#     (3, 3),
#     (4, 4),
#     (5, 5)
# ]
#
#
# cursor = connection.cursor()
# cursor.executemany(create_EmplPositions_query, EmplPositions_val)
# connection.commit()
# #
# #
# create_Department_query = "INSERT INTO Department (name, salary) VALUES (%s, %s)"
#
# Department_val = [
#     ('Michael', 20000),
#     ('Pam', 6000),
#     ('Jim', 10000),
#     ('Meredith', 8000),
#     ('Dwight', 13000)
# ]
# cursor = connection.cursor()
# cursor.executemany(create_Department_query, Department_val)
# connection.commit()
#
# #
# create_EmplDepartment_query = "INSERT INTO EmplDepartment (emply_id, Dep_id) VALUES (%s, %s)"
#
# EmplDepartment_val = [
#     (1, 1),  #Assuming these are the employee and department IDs
#     (2, 2),
#     (3, 3),
#     (4, 4),
#     (5, 5)
# ]
#
# cursor = connection.cursor()
# cursor.executemany(create_EmplDepartment_query, EmplDepartment_val)
# connection.commit()
#
# #
# create_EmplRate_query = "INSERT INTO EmplRate (emply_id, rate_id) VALUES (%s, %s)"
# EmplRate_val = [
#     (1, 67),  # Assuming these are the employee and rate IDs
#     (2, 78),
#     (3, 92),
#     (4, 55),
#     (5, 85)
# ]
#
# cursor = connection.cursor()
# cursor.executemany(create_EmplRate_query, EmplRate_val)
# connection.commit()
#
#
# # ___________________________________________________

# # #
# # # __________________________________________
# #
# # #
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

#
# # # __________________________________________
#
##Create SELECT queries:

# select_Positions = "SELECT * FROM Positions"
# Positions = execute_read_query(connection, select_Positions)
#
# for pos in Positions:
#     print(pos)

# select_EmplRate = "SELECT * FROM EmplRate"
# EmplRate = execute_read_query(connection, select_EmplRate)
#
# for Rate in EmplRate:
#     print(Rate)

# select_Employees_Department = """
# SELECT
# Employees.name, Department.salary
# FROM
# Employees
# JOIN Department ON Employees.id = Department.id
# """
#
# Employees_Department = execute_read_query(connection, select_Employees_Department)
# for Employees_Department in Employees_Department:
#     print(Employees_Department)

#
#Create SELECT queries with WHERE:

# select_Employees = "SELECT * FROM Employees where gender = 'female'"
#
# Employees = execute_read_query(connection, select_Employees)
#
# for emp in Employees:
#     print(emp)

# select_EmplyRate_Department = """
# SELECT
#     SUM(EmplRate.id) as EmplyRate
# FROM
#     EmplRate
# JOIN
#     Employees ON EmplRate.emply_id = Employees.id
# JOIN
#     EmplDepartment ON Employees.id = EmplDepartment.emply_id
# JOIN
#     Department ON EmplDepartment.Dep_id = Department.id
# """
#
# EmplyRate_Department = execute_read_query(connection, select_EmplyRate_Department)
#
# for dep in EmplyRate_Department:
#     print(dep)

#  Update records using SELECT:
# select_Positions_job = "SELECT job FROM Positions WHERE id = 3"
#
# Positions_job = execute_read_query(connection, select_Positions_job)
# for job in Positions_job:
#     print(job)

# update_Positions_job = """
# UPDATE
#   Positions
# SET
#   job = "General Manger"
# WHERE
#   id = 3
# """
#
# execute_query(connection, update_Positions_job)


# # Delete records using SELECT:
# delete_EmplRate = "DELETE FROM EmplRate WHERE id = 4"
# execute_query(connection, delete_EmplRate)




