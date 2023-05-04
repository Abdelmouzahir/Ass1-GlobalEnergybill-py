#first take data from user and create variables

print("Welcome to the Global Energy bill calculator!")
while True:
    account_number = input("Please enter your account number: ")
    try:
        val_account = int(account_number)
        break
    except ValueError:
        print("Please enter a valid account number!")


while True:
    month = input("Enter the month number (e.g., for January, enter 1): ")
    try:
        val_month = int(month)
        if val_month >= 1 and val_month <= 12:
          break
        else:
            print("please enter a month between 1 and 12!")
    except ValueError:
        print("Please enter a valid Month number!")
    
while True:
    elec_plan = input("Enter your electricity plan (EFIR or EFLR): ")
    elec_plan = elec_plan.upper()
    if elec_plan == 'EFIR' or elec_plan == 'EFLR':
        break
    else:
        print("Please enter a valid Electricity plan!")

elec_amount = float(input("Please enter the amount of electricity you used in month " + month + " (in kWh): "))    

while True:
    gas_plan = input("Enter your Gas plan (GFIR or GFLR): ")
    gas_plan = gas_plan.upper()
    if gas_plan == 'GFIR' or gas_plan == 'GFLR':
        break
    else:
        print("Please enter a valid gas plan!")
      

gas_amount = float(input("Please enter the amount of gas you used in month " + month + " (in GJ): "))

while True:
  province = input("Enter the abbreviation for your province of residence (two letters): ")
  province_list = ['AB','BC' ,'MB','NT','NU','QC','SK','YT', 'ON','NB','NL','NS','PE']
  province = province.upper()
  if province in province_list:
    break
  else: 
    print("Please enter a valid Province abbreviation!")

#after collecting informations we pass to calculation

fixed_monthly_fee = 1.32
CGE_fixed_fee = 120.62
#elec
def elec_rate(elec_amount,elec_plan):
    if elec_plan == 'EFIR'  and elec_amount <= 1000:
       elec_rate = (elec_amount*0.0836)
    elif  elec_plan == 'EFIR' and elec_amount > 1000:  
       elec_rate = (1000*0.0836)+((elec_amount-1000)*0.0941)
    elif elec_plan == 'EFLR':
        elec_rate = (elec_amount*0.0911)
    else:
        return False
    return elec_rate
elec_bill = float(elec_rate(elec_amount,elec_plan))

#gas
def gas_rate(gas_amount,gas_plan):
    if gas_plan == 'GFIR'  and gas_amount <= 950:
       gas_rate = (gas_amount*0.0456)
    elif  gas_plan == 'GFIR' and gas_amount > 950:  
       gas_rate = (950*0.0456)+((gas_amount-950)*0.0589)
    elif gas_plan == 'GFLR':
        gas_rate = (gas_amount*0.0393)
    else:
        return False
    return gas_rate
gas_bill = float(gas_rate(gas_amount,gas_plan))

Bill_amount =  fixed_monthly_fee + CGE_fixed_fee + elec_bill + gas_bill

#tax calculation
def tax_calculation(province):
    if province in ('AB' , 'BC' , 'MB' , 'NT' , 'NU' , 'QC' , 'SK' , 'YT'):
        tax_calculation = 0.05
    elif province in ('ON'):
        tax_calculation = 0.13
    elif province in ('NB' , 'NL' , 'NS' , 'PE'):
        tax_calculation = 0.15
    else:
        return False
    return tax_calculation
tax_rate= float(tax_calculation(province))                    

amount_due = Bill_amount + (Bill_amount*tax_rate)

#final result
print("Thank you! Your total amount due now is : $",amount_due)