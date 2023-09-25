class SalaryContract:
    def __init__(self, wage):
        self.wage = wage
    
    def get_total_amount(self):
        return self.wage
    
    def get_text(self):
        return f'works on a monthly salary of {self.wage}'
    
class HourlyContract:
    def __init__(self, wage, hours):
        self.wage = wage
        self.hours = hours
    
    def get_total_amount(self):
        return self.wage * self.hours
    
    def get_text(self):
        return f'works on a contract of {self.hours} hours at {self.wage}/hour'

class ContractCommision:
    def __init__(self, commission_rate, amount_of_commisions):
        self.commission = commission_rate
        self.amount_of_commisions = amount_of_commisions
    
    def get_total_amount(self):
        return self.commission * self.amount_of_commisions
    
    def get_text(self):
        return f'receives a commission for {self.amount_of_commisions} contract(s) at {self.commission}/contract'

class BonusCommision:
    def __init__(self, bonus):
        self.bonus = bonus
    
    def get_total_amount(self):
        return self.bonus
    
    def get_text(self):
        return f'receives a bonus commission of {self.bonus}'
    
class Payroll:
    def __init__(self, contract, commision):
        self.contract = contract
        self.commision = commision
    
    def get_total_amount(self):
        total_amount = 0
        if self.contract is not None:
            total_amount += self.contract.get_total_amount()

        if self.commision is not None:
            total_amount += self.commision.get_total_amount()
        return total_amount
    
    def get_commission_text(self):
        if self.commision is None:
            return ''
        return self.commision.get_text()
    
    def get_text(self):
        return f'{self.contract.get_text()}{(" and "+self.get_commission_text()) if self.commision is not None else ""}. Their total pay is {self.get_total_amount()}.'
