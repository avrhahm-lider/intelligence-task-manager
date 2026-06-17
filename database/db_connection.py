import mysql.connector
class DB_connection:
    def __init__(self):
        self.__connection = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "1234",
            database = "Intelligence_db"
            
        )
    def get_connection(self):
        return self.__connection
     
    def create_database(self):
        cursor = self.__connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db;")
        cursor.close()

    def create_tables(self):
        cursor = self.__connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS agents(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(50) NOT NULL,
                       specialty VARCHAR(50) NOT NULL,
                       is_active BOOLEAN DEFAULT TRUE,
                       completed_missions INT DEFAULT 0,
                       failed_missions INT DEFAULT 0,
                       agent_rank ENUM('Junior' , 'Senior' , 'Commander' ) NOT NULL
                       )
                       """)    
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS mission(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       title VARCHAR(50) NOT NULL,
                       description TEXT NOT NULL,
                       location VARCHAR(50) NOT NULL,
                       difficulty INT NOT NULL,
                       importance INT NOT NULL,
                       status VARCHAR(50) DEFAULT 'NEW',
                       risk_level VARCHAR(50) NOT NULL, 
                       assigned_agent_id INT
                       )
                       """)
con = DB_connection().create_tables()        