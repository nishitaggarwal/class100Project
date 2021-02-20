#%%
class Atm(object):
    
    def __init__(self, atm_card_number,pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
        
    
    def CashWithdrawl(self):
        print("Cash of about 1,00,000 has been Withdrawled")
        print("kindly keep it safe")

    def BalanceEnquiry(self):
        print("Balance Enquiry ")
        print("Current Balance is Rs 50,00,000")

pin_Number = input("Enter your Pin Number:-     Try 1234")

audi = Atm("DCB BANK",pin_Number)
audi.CashWithdrawl()
# %%
