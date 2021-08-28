class Bank():
   def __init__(self, cardNumber, PINnumber):
      self.cardNumber = cardNumber
      self.PINnumber = PINnumber
   def CashWithdrawl(self, amount):
      newAmount = 10000 - amount
      print("Your Balance is: ", newAmount)
   def BalanceEnquiry(self):
      print("Your Balance is 10,000")

def main():
   caRdNumber = input("Enter your Card Number: ")
   pINnumber = input("Enter your PIN: ")
   newUser = Bank(caRdNumber, pINnumber)
   print("Choose your activity.")
   print("1. Cash Withdrawl 2. Balance")
   activity = int(input("Enter your Activity Number: "))
   if(activity == 1):
      amount = int(input("Enter amount to Withdraw: "))
      newUser.CashWithdrawl(amount)
   elif(activity == 2):
      newUser.BalanceEnquiry()
   else:
      print("Enter a valid number.")

main()