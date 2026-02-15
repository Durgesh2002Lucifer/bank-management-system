# import json
# import random
# import string
# from pathlib import Path

# class Bank:
#     database = Path(__file__).parent / "data.json"
#     data = []

#     try:
#         if Path(database).exists():
#             with open(database) as fs:
#                 data = json.loads(fs.read())
#         else:
#             print("No such file exist ")               
#     except Exception as err:
#         print(f"an exception accured as {err}")        

#     @staticmethod
#     def update():
#         with open(Bank.database,'w') as fs:
#             fs.write(json.dumps(Bank.data))

#     @classmethod
#     def __AccountNumberGenerator(cls):
#         alpha = random.choices(string.ascii_letters, k = 3)
#         num =  random.choices(string.digits, k = 3)
#         specialCharacters = random.choices("@#$%^&*?", k = 1)

#         id = alpha + num + specialCharacters
#         random.shuffle(id)
#         return "".join(id)
    
#     def Createaccount(self):
#         info = {
#             "Name" : input("Tell your name: "),
#              "Age" : int(input("Enter your age: ")),
#             "Pin"  : int(input("Enter the 4 digit pin: ")),
#             "Email": input("Enter the email: "),
#             "Account_No.": Bank.__AccountNumberGenerator(),
#             "Balance"    : 0
#             }
#         if info["Age"] < 18 or len(str(info["Pin"])) != 4:
#             print("Sorry your account is not created ")
#         else:
#             print("Congratulations! your account have been created")
#             for i in info:
#                 print(f"{i} : {info[i]}")
#             print("Please note down your account number ") 

#             Bank.data.append(info)
#             Bank.update() 

#     def depositMoney(self):
#         accnumber = input("Enter your account number ").strip()
#         pin = int(input("Enter your pin ").strip())

#         for user in Bank.data:
#             if user["Account_No."] == accnumber and user["Pin"] == pin:
#                 amount = int(input("Enter the amount: "))
    
#                 if 0 < amount <= 10000:
#                     print("Before update:", user['Balance'])
#                     user['Balance'] += amount
#                     print("After update:", user['Balance'])

#                     Bank.update()
#                     print("Amount added successfully!")
#                     return
#                 else:
#                     print("Invalid amount.")
#                     return
#         print("Account not found.")

#     def withdrawMoney(self):
#         accnumber = input("Enter your account number ").strip()
#         pin = int(input("Enter your pin ").strip())

#         for user in Bank.data:
#             if user["Account_No."] == accnumber and user["Pin"] == pin:
#                 amount = int(input("Enter the amount: "))
    
#                 if user['Balance'] >= amount:
#                     print("Before update:", user['Balance'])
#                     user['Balance'] -= amount
#                     print("After update:", user['Balance'])

#                     Bank.update()
#                     print("Amount withdraw successfully!")
#                     return
#                 else:
#                     print("Invalid amount.")
#                     return

#         print("Account not found.")    

#     def showDetails(self):
#         accnumber = input("Enter your account number ").strip()
#         pin = int(input("Enter your pin ").strip())

#         for user in Bank.data:
#             if user["Account_No."] == accnumber and user["Pin"] == pin:
#                 print("Your Account Details are \n\n\n")
#                 for i in user:
#                     print(f"{i} : {user[i]}")

#     def UpdatDetails(self):
#         accnumber = input("Enter your account number ").strip()
#         pin = int(input("Enter your pin ").strip())

#         for user in Bank.data:
#             if user["Account_No."] == accnumber and user["Pin"] == pin:

#                 print("You cannot change Age, Account Number, or Balance.")
#                 print("Leave blank if you don't want to change something.\n")
    
#                 new_name = input("Enter new name: ").strip()
#                 new_email = input("Enter new email: ").strip()
#                 new_pin = input("Enter new pin: ").strip()

#                 if new_name:
#                     user["Name"] = new_name

#                 if new_email:
#                     user["Email"] = new_email

#                 if new_pin:
#                     if len(new_pin) == 4 and new_pin.isdigit():
#                         user["Pin"] = int(new_pin)
#                     else:
#                         print("Invalid PIN. Must be 4 digits.")
#                         return

#                 Bank.update()
#                 print("Bank details have been updated successfully!")
#                 return

#         print("Account not found.")

#     def DeleteAccount(self):
#         accnumber = input("Enter your account number ").strip()
#         pin = int(input("Enter your pin ").strip())

#         for user in Bank.data:
#             if user["Account_No."] == accnumber and user["Pin"] == pin:
#                 check = input("press y if you actually want to delete the account or n: ")
#                 if check == 'n' or check == 'N':
#                     print("byPass")
#                 else:
#                     index = Bank.data.index(user)
#                     Bank.data.pop(index)
#                     Bank.update() 
#                     print("your account have delete successfully..")   

                       
# user = Bank()
# print("press 1 for creating an account ")
# print("press 2 for Depositing the money in the bank ")
# print("press 3 for withdrawing the money ")
# print("press 4 for details ")
# print("press 5 for updating the details ")
# print("press 6 for deleting your account ")

# check = int(input("tell your response :- "))

# if check == 1:
#     user.Createaccount()

# if check == 2:
#     user.depositMoney()   

# if check == 3:
#     user.withdrawMoney()     

# if check == 4:
#     user.showDetails()   

# if check == 5:
#     user.UpdatDetails()    

# if check == 6:
#     user.DeleteAccount()     