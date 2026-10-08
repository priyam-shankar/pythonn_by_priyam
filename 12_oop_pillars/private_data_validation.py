class ATM:
    def __init__(self, pin):
       # self.pin = pin => public attribute
       self.__pin = pin  #private attribute
       
    def verify_pin(self,entered_pin):
        if entered_pin == self.__pin:
            print(f"{entered_pin} - Access Granted")
        else:
            print(f"{entered_pin} - Incorrect pin")
        
       
atm1 = ATM(1234)
atm1.verify_pin(1234)


# ATM
# Concept:
# - __pin → private attribute
# - The user enters entered_pin
# - The method compares the entered PIN with the private PIN
# - Correct PIN → Access Granted ✅
# - Wrong PIN → Incorrect PIN ❌
# Topic: Private Data + Controlled Access + Validation 🔐