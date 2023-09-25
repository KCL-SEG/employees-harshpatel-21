"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from contracts import SalaryContract, HourlyContract, ContractCommision, BonusCommision, Payroll

class Employee:
    def __init__(self, name, payroll):
        self.name = name
        self.payroll = payroll

    def get_pay(self):
        # print(self.payroll)
        return self.payroll.get_total_amount()

    def __str__(self):
        return self.name+" "+self.payroll.get_text()
    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_payroll = Payroll(SalaryContract(4000), None)
billie = Employee('Billie', billie_payroll)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_payroll = Payroll(HourlyContract(25,100), None)
charlie = Employee('Charlie',charlie_payroll)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_payroll = Payroll(SalaryContract(3000), ContractCommision(200,4))
renee = Employee('Renee',renee_payroll)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_payroll = Payroll(HourlyContract(25,150), ContractCommision(220,3))
jan = Employee('Jan', jan_payroll)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_payroll = Payroll(SalaryContract(2000), BonusCommision(1500))
robbie = Employee('Robbie', robbie_payroll)

#Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_payroll = Payroll(HourlyContract(30,120), BonusCommision(600))
ariel = Employee('Ariel', ariel_payroll)