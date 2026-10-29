#10/22/26
class Patient:
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
        
    def set_name(self,name):
        self.__name = name
        
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
    
    def get_name(self):
        return self.__name
        
    def get_bill_amount(self):
        return self.__bill_amount
    
    def calculate_bill(self):
        print(f"Patient Name: {self.__name}\nOriginal Bill: {self.__bill_amount}\nFinal Bill: {self.__bill_amount}")
        
class SeniorPatient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)

    def calculate_bill(self):
        orig_bill = self.get_bill_amount()
        final_bill= orig_bill - (orig_bill*0.20)
        print(f"\nPatient Name: {self.get_name()}\nOriginal Bill: {self.get_bill_amount()}\nFinal Bill: {final_bill}")
    
class PhilHealthPatient(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)
        
    def calculate_bill(self):
        orig_bill = self.get_bill_amount()
        final_bill= orig_bill - (orig_bill*0.15)
        print(f"\nPatient Name: {self.get_name()}\nOriginal Bill: {self.get_bill_amount()}\nFinal Bill: {final_bill}")

reg_patient = Patient("Juan Dela Cruz", 15000)
snr_patient = SeniorPatient("Maria Santos", 15000)
phh_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System\n----------------------- ")
reg_patient.calculate_bill()
snr_patient.calculate_bill()
phh_patient.calculate_bill()
