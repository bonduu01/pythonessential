class Bank_Account:
    def __init__(self, iban):
        # print('__init__ called')
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


new_iban = '0328474644'
bank_account = Bank_Account(new_iban)
print(bank_account.validate(new_iban))
