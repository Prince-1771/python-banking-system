import random
from datetime import datetime
import os

def get_time_12hr():
    return datetime.now().strftime("%d-%b-%Y | %I:%M:%S %p")

print("\n" + "="*40)
print("        WELCOME TO HDFC BANK")
print("="*40)
print(f"\n⏰ Login Time: {get_time_12hr()}\n")
print("Good Morning! Thank you for visiting us today.\n")
name=input("Enter Your Full Name = ")
print(f"\n✓ Welcome, {name}!\n")
mobile = input("Enter Your 10 Digit Mobile Number = ").strip()
if not (mobile.isdigit() and len(mobile) == 10):
    print("\n❌ Invalid mobile number! Please enter a 10 digit number.\n")
    exit()

def saving():
    print("\n" + "-"*40)
    print("SAVING ACCOUNT TYPES")
    print("1. Regular Saving Account")
    print("2. FD Account (Fixed Deposit)")
    
    def saccount():
        print(f"\n✓ Your Account Number: {acnumber}\n")
        
    ac=int(input("Please select account type (1 or 2): "))
    if(ac==1 or ac==2):
        acnumber=random.randint(4569871250,8857945149)
        saccount()
    else:
        print("\n❌ Invalid choice! Please select 1 or 2.\n")

def current():
    acnumber=random.randint(4569871250,8857945149)

    print(f"\n✓ Your Account Number: {acnumber}\n")

print("-"*40)
print("🏦 ACCOUNT TYPE SELECTION")
print("-"*40)

choice=int(input("Select Account Type:\n1 = Saving Account\n2 = Current Account\n\nYour choice (1 or 2): "))
if(choice==1):
    saving()
elif(choice==2):
    current()
else:
    print("\n❌ Invalid choice entered! Please select 1 or 2.\n")

print("-"*50)
print("💳 DEBIT CARD SETUP")
print("-"*50)
print("Note: Debit card annual charge is 300 Rs (deducted from account)")
debitcard=input("Do you want a Debit Card? (Y/N): ").strip().upper()
if debitcard == 'Y' or debitcard == 'y':
    print("Your Debit Card Is Generated Successfully Do You Want To Know The Details ???\n")
    info=input("Enter Y for Yes and N for No = ").strip().upper()
    if info == 'Y':
        print("Your Debit Card Number Is = ",random.randint(4569871234567890,8857945145678901))
        print("Your CVV Is = ",random.randint(100,999))
        print("Your Debit Card Expiry Date Is = 12/29\n")
    else:
        print("Thank You\n")

print("Your Acccount Is Ready To Use\n")
customerid=random.randint(21456,85689)
print(f"✓ Your Customer ID: {customerid}\n")
print("You Have To Create 4 Digit PIN For Your Account")
pin = input("Enter your 4 Digit PIN: ").strip()
if not (pin.isdigit() and len(pin) == 4):
    print("\n❌ PIN Must Be Exactly 4 digits. Please restart the process.\n")
    exit()
print(f"\n✓ Your PIN {pin} Has Been Set Successfully.\n")
print("\n" + "-"*50)
print("💰 INITIAL DEPOSIT")
print("-"*50)
print("⚠️  Minimum balance required: 5,000 Rs")
amt=int(input("Enter amount to deposit (must be > 5000 Rs): "))

if(amt>5000):
    print(f"\n✓ Your deposit of {amt} Rs has been credited to your account.\n")
else:
    print("\n❌ Amount is less than minimum required (5000 Rs). Account creation cancelled.\n")
    exit()

if debitcard == 'Y' or debitcard == 'y':
    print(f"✓ Debit Card activated!")
    print(f"💳 Annual charge: 300 Rs (deducted from account)")
    amt=amt-300
elif debitcard == 'N':
    print("✓ You can activate debit card later.\n")
else:
    print("❌ Invalid choice for debit card!\n")

print("\n" + "="*50)
print("        YOUR ACCOUNT IS READY!")
print("="*50)

nominee = None
aadhar = None
pan = None
address = None

def acservice():
    global nominee, aadhar, pan, address
    print("Nominee Is = ", nominee or 'Not Set')
    print("Aadhar Number Is = ", aadhar or 'Not Set')
    print("Pan Number Is = ", pan or 'Not Set')
    print("Address Is = ", address or 'Not Set')
    print("\n💳 ACCOUNT RELATED SERVICES")
    print("Which Service Do You Want ?")
    print("1. Add Nominee To Your Account")
    print("2. Enter Your Aadhar Number")
    print("3. Enter Your Pan Number")
    print("4. Enter Your Address")
    print("5. Exit")
    service=int(input("Enter Your Choice = "))
    if(service==1):
        nominee=input("Enter Nominee Full Name = ")
        print(f"\n✓ Nominee {nominee} added successfully to your account.\n")
        acservice()
    elif(service==2):
        aadhar = input("Enter Your 12 Digit Aadhar Number = ").strip()
        if not (aadhar.isdigit() and len(aadhar) == 12):
            print("\n❌ Invalid Aadhar number! Please enter a 12 digit number.\n")
        else:
            print(f"\n✓ Aadhar number {aadhar} linked successfully to your account.\n")
        acservice()
    elif(service==3):
        pan=input("Enter Your Pan Number = ")
        print(f"\n✓ Pan number {pan} linked successfully to your account.\n")
        acservice()
    elif(service==4):
        address=input("Enter Your Address = ")
        print(f"\n✓ Address '{address}' updated successfully in your account.\n")
        acservice()
    elif(service==5):
        return
    else:
        print("\n❌ Invalid choice! Please select 1-5.\n")
        acservice()

while True:
    print("\n" + "-"*50)
    print("💳 BANKING SERVICES MENU")
    print("-"*50)
    print("1. Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Check Balance")
    print("4. Transfer Money")
    print("5. Account Related Services")
    print("6. Account Details")
    print("7. Exit")
    print("-"*50)

    service=int(input("Select a service (1-7): "))
    if(service==1):
        print("\n💰 DEPOSIT CASH")
        print("-"*30)
        dep=int(input("Enter amount to deposit: "))
        amt=amt+dep
        print(f"✓ {dep} Rs deposited successfully!")
        print(f"⏰ Transaction Time: {get_time_12hr()}")
        print(f"Your new balance: {amt} Rs\n")
        
    elif(service==2):
        print("\n💸 WITHDRAW CASH")
        print("-"*30)
        mpin=input("Enter your 4 Digit PIN to proceed: ").strip()
        if mpin != pin:
            print("\n❌ Incorrect PIN! Transaction cancelled.\n")
            continue
        wit=int(input("Enter amount to withdraw: "))
        if(wit>amt):
            print(f"❌ Insufficient balance! Your balance: {amt} Rs\n")
        else:
            amt=amt-wit
            print(f"⏰ Transaction Time: {get_time_12hr()}")
            print(f"✓ {wit} Rs withdrawn successfully!")
            print(f"Your new balance: {amt} Rs\n")
            
    elif(service==3):
        print("\n📊 ACCOUNT BALANCE")
        print("-"*30)
        print(f"⏰ Check Time: {get_time_12hr()}")
        print(f"Your current balance: {amt} Rs\n")
        
    elif(service==4):
        print("\n📤 TRANSFER MONEY")
        print("-"*30)
        mpin=input("Enter your 4 Digit PIN to proceed: ").strip()
        if mpin != pin:
            print("\n❌ Incorrect PIN! Transaction cancelled.\n")
            continue
        tr=int(input("Enter amount to transfer: "))
        if(tr>amt):
            print(f"❌ Insufficient balance! Your balance: {amt} Rs\n")
        else:
            amt=amt-tr
            print(f"✓ {tr} Rs transferred successfully!")
            print(f"⏰ Transaction Time: {get_time_12hr()}")
            print(f"Your new balance: {amt} Rs\n")
    elif(service==5):
        acservice()
            
    elif(service==6):
        print("\n🏦 ACCOUNT DETAILS")
        print("-"*30)
        print(f"⏰ Access Time: {get_time_12hr()}")
        print(f"Account Holder Name: {name}")
        print(f"Account Balance: {amt} Rs")
        print(f"Customer ID: {customerid}")
        print(f"Account Type: {'Saving' if choice==1 else 'Current'}")
        print(f"Mobile Number: {mobile}")
        print(f"Debit Card: {'Activated' if debitcard=='Y' else 'Not Activated'}")
    elif(service==7):
        print("\n" + "="*50)
        print(f"⏰ Logout Time: {get_time_12hr()}")
        print("Thank you for using HDFC Bank!")
        print("Your transaction is complete.")
        print("="*50 + "\n")
        break
        
    else:
        print("\n❌ Invalid choice! Please select 1-7.\n")
