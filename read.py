import mysql.connector

# creating connection.
class read:
    def __init__(self):
      self.conn=mysql.connector.connect(
           host="localhost",
           user="root",
           password="Ravalikag1@",
           database="banking"
           )
      
    def specific_info(self,customer_id ,table_name):
      cur=self.conn.cursor()
      if table_name=='personal_details' or table_name=='bank_details':
        cur.execute(f"select * from {table_name} where customerid={customer_id}") 
        print(cur.fetchall())

      if table_name=='transaction_details':
          print('test1')
          cur.execute(f'''SELECT * FROM TRANSACTION_DETAILS WHERE TRANSACTIONID IN
              (SELECT TRANSACTIONID FROM ACCOUNT_DETAILS WHERE ACCOUNT_NUMBER IN 
              (SELECT ACCOUNT_NUMBER FROM BANK_DETAILS WHERE CUSTOMERID={customer_id}));
                      ''')
          print(cur.fetchall())