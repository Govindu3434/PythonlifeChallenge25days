#  ATM SMALL PROJECT
                
S = '''  
1. Credit
2. Debit
3. Min Balance
4. Exit
'''

name = "vijay"
password = "1432"
amount = 10000  # Initial balance

user_name = input("Enter the user name: ")
password_input = input("Enter the password: ")
if name == user_name and password == password_input:
    while True:
        print(S)
        option = int(input("Enter the option: "))
        
        if option == 1:
            credit_amount = float(input("Enter the amount: "))
            amount += credit_amount
            print("Amount after credit:", amount)
            
        elif option == 2:
            debit_amount = float(input("Enter the amount: "))
            amount -= debit_amount
            print("Amount after debit:", amount)
            
        elif option == 3:
            print("Current Amount:", amount)
            
        elif option == 4:
            print("Thank you for using ATM!")
            break
else:
    print("Invalid credentials!")           