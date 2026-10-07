class Student:
    def __init__(self):
        print("constructor was called...")

s1 = Student()
s2 = Student()


class BankAccount:
   pass
account1 = BankAccount()


account1.name = "Priyam"
account1.account_number = 12345678
account1.balance = 5000
print(account1.name,account1.account_number,account1.balance)

account2 = BankAccount()

account2.name = "Bittu"
account2.account_number = 98765432
account2.balance = 74123
print(account2.name,account2.account_number,account2.balance)

# all these things are ok but 
# Without a constructor, we have to create each object
# and manually assign its properties one by one.

# If we have many customers, this becomes repetitive
# and makes the code longer and harder to manage.

# A constructor helps us set the initial data
# when the object is created.