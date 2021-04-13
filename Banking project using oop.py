from datetime import datetime
import time
class Banking:
    def __init__(self,name,password,amount):
        self.__name = name # __varname(private variable)
        self.__password = password
        self.__amount = amount
        self.__history = [] # {"code":1/2/3/4}
        self.CODES = {1:"Successful Addition",2:"Successful Deduction",3:"Unsuccessful Addition",4:"Unsuccessful Deduction"}
    def add_money(self,amount):
        if amount<0:
            print("Try to call deduct money function")
            self.__history.append({"code":3,"time":datetime.now().time()})
        else:
            self.__amount+=amount
            self.__history.append({"code":1,"time":datetime.now().time()})
    def deduct_money(self,amount):
        if amount == 0:
            print("Try deducting more")
            self.__history.append({"code":4,"time":datetime.now().time()})
        elif amount> self.__amount:
            print("Insufficient Balance!!!")
            self.__history.append({"code":4,"time":datetime.now().time()})
        else:
            self.__amount+=amount
            self.__history.append({"code":2,"time":datetime.now().time()})
    def show_balance(self):
        print("CURRENT BALANCE: ",self.__amount)
    def show_transactions(self,n=None):
        reversed = self.__history[::-1]
        maximum = len(self.__history) if n == None else n
        for i in range(maximum):
            print("{} at {}".format(self.CODES[reversed[i]["code"]],reversed[i]["time"]))
customer1 = Banking("brian","temp123",100)
customer1.add_money(20)
time.sleep(1)
customer1.deduct_money(10)
time.sleep(2)
customer1.add_money(30)
customer1.show_balance()
customer1.show_transactions()
        
        
       