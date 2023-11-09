x=5
print(x)

# creating library my sql-connecror-python
import mysql.connector

# creating connection.
class insert:
    def __init__(self):
      self.conn=mysql.connector.connect(
           host="localhost",
           user="root",
           password="Ravalikag1@",
           database="banking"
           )
    def personal_details(self,cid,fname,lname,add,phne,adn,pan):
        curr=self.conn.cursor()
        curr.execute(f"insert into personal_details values({cid},'{fname}','{lname}','{add}',{phne},'{adn}','{pan}')")
        self.conn.commit()
        print ("personal information has been saved sucessfully:")




    def bank_details(self,acn,cid,ifsc,actype):
      cur=self.conn.cursor()
      cur.execute(f"insert into bank_details values({acn},{cid},'{ifsc}','{actype}')")
      self.conn.commit()
      print ("bank details has been sucessfully saved")


    def transaction_details(self,tid,sac,rac,am,mtd):
       cur=self.conn.cursor()
       cur.execute(f"insert into transaction_details values({tid},{sac},{rac},{am},'{mtd}')")
       self.conn.commit()
       print("transaction details has been saved sucessfully:")


    def account_details(self,acn,tid,am,cb,tp):
       cur=self.conn.cursor()
       cur.execute(f"insert into account_details values({acn},{tid},{am},{cb},'{tp}')")
       self.conn.commit()
       print("account details has been saved sucessfully:")

       



