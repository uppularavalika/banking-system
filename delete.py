import mysql.connector

# creating connection.
class delete:
    def __init__(self):
      self.conn=mysql.connector.connect(
           host="localhost",
           user="root",
           password="Ravalikag1@",
           database="banking"
           )
    def specific_del(self,table_name,cusid):
        cur = self.conn.cursor()
        cur.execute(f"delete from {table_name} where customerid={cusid}")
        self.conn.commit()
        print("Data has been deleted sucessfully")