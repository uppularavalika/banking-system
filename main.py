from creat import insert
from read import read
from update import update
from delete import delete

obj=insert()
objread=read()
objupdate=update()
objdelete=delete()

print("------------bank management system-------------------------")
print("for insering the data press 1:")
print("for read the data press 2:")
print("for update the data press 3:")
print("for delete the data press 4:")


opr=int(input("please enter your operation:"))
def myopr():
    print("------for personal information press 1-----")
    print("------for bank details press 2------")
    print("------for transaction details press 3------")
    print("------for account details press 4------")
    vr=int(input("please select the table:"))
    if vr ==1:
        return 'personal_details'
    elif vr ==2:
        return 'bank_details'
    elif vr ==3:
        return 'transaction_details'    
    elif vr ==4:  
        return 'account_details' 

if opr ==1:
     h= myopr()
     if h=='personal_details':
         cid=int(input("please enter customer id:"))
         fname=input("please enter customer first name:")
         lname=input("please enter customer last name:")
         phne=int(input("please enter customer phone number:"))
         add=input("please enter customer address:")
         adn=input("please enter customer aadhar number:")
         pan=input("please enter customer pan number:")
         obj.personal_details(cid,fname,lname,add,phne,adn,pan)
     elif h=='bank_details': 
         acn=int(input("please enter account number:"))  
         cid=int(input("please enter customer id:"))  
         ifsc=int(input("please enter ifsc code:"))  
         actype=input("please enter account type:")
         obj.bank_details(acn,cid,ifsc,actype)
     elif h=='transaction_details':   
          tid=int(input("please enter transaction id:"))
          sac=int(input("please enter sender account number:"))
          rac=int(input("please enter receiver account number:"))
          am=int(input("please enter account:"))
          mtd=input("please select the method")
          obj.transaction_details(tid,sac,rac,am,mtd)
     elif h=='account_details': 
          acn=int(input("please enter account number:"))
          tid=int(input("please enter transactionid:"))
          am=int(input("please enter amount:"))
          cb=int(input("please enter closing balance:"))
          tp=input("please enter transaction type:")
          obj.account_details(acn,tid,am,cb,tp)


if opr==2: # user want to read the data
    j= myopr()
    cusid=int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)

if opr==3:  
    j= myopr()
    cusid=int(input("please enter customer id for fetching data"))
    colname=input("please enter column name:")
    newval=input("please enter new values:")
    objupdate.myupdate(j,colname,newval,cusid)

if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to delete the data:"))
    objdelete.specific_del(k,cusid)
    
