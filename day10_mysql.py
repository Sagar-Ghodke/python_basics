'''morning :'''
# installlation and databases assess

'''database creation in mysql server'''
    # from terminal
    # link all tables : with : 
                                # primary key 
                                # foregin key
                                
                                





# ===============================================================================


from mysql.connector import Error
import mysql.connector as sqlcon

try:
    my_db = sqlcon.connect(host = "localhost",\
        user = "root",\
            passwd = "Sagar@1254",\
                database = "DPU_training")
    print("Successfully connected with the databases.")
    
    cursor = my_db.cursor()
    cursor.execute("SHOW TABLES") #can do all from here too what terminal does.
    
    table = cursor.fetchall()
    # table = cursor.fetchmany(1)
    print(table)
        
except Error as e:
    print(f"Error while connectiong with the databases: {e}")