database ={}

class Budget:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.spent = 0
        self.receive = 0
        
    def deposit(self):
        deposit = int(input("Enter the amount to deposit for %s budget: " % self.name))
        self.balance += deposit 
        print("You have deposited %d for %s\n" % (self.balance, self.name))
        database[self.name] = deposit
        print(database)


    def withdrawal(self):
        withdraw = int(input("How much would you like to withdraw from %s budget: " % self.name))
        if self.balance > withdraw:
            self.balance -= withdraw
            self.spent += withdraw
            database[self.name] =  self.balance
            print(database)
            print("You have succesfully withdrawn %d\n" %self.spent)
            
        else:
            print("Insufficient Balance")



    def category_balance(self):
         print("Your balance from %s budget is %d\n" %( self.name, self.balance))
         

    def transfer(self,category):
        self.category = category
        
        if category in database:
            transferAmount = int(input("How much would you like to transfer from %s budget?: " % self.name))
            updated_balance = database[self.name] - transferAmount
            database[self.name] = updated_balance

            database [self.category] += transferAmount
            print(database)

        else:
            transferAmount = int(input("How much would you like to transfer from %s budget?: " % self.name))
            updated_balance = database[self.name] - transferAmount
            database[self.name] = updated_balance

            database [self.category]= transferAmount
            print(database)


            if self.balance > transferAmount:
                self.balance -= transferAmount
                self.receive += transferAmount
                print("You have succesfully transferred %d\n" %self.receive)
            else:
                print("You have exceeded your balance")


feeding = Budget("food")
Entertainment = Budget("party")

feeding.deposit()
Entertainment.deposit()

feeding.withdrawal()
Entertainment.withdrawal()

feeding.category_balance()
Entertainment.category_balance()

feeding.transfer(input("What category would you like to transfer to: "))
Entertainment.transfer(input("What category would you like to transfer to: "))


