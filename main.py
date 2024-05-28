# 1) class or method for the ATM simulator functionality
class User:
  def __init__(self,pin,balance,name):
    self.pin = pin
    self.balance = balance
    self.name = name

# 2) multiple conditions for selecting at least 4 ATM functionalities 

def simulator(obj):
  print(f'''*** Welcome {obj.name} to ATM machine simulator!! ***''')
  pin = int(input('Enter your pin :'))

  if pin != obj.pin:
    print('Please enter correct pin here!!')
    print('Thank you.')
    return
  while True:
    print('''
          Options you can Excercise are:
            1) Balance
            2) Withdraw
            3) Deposit
            4) Exit
        ''')
    choose=int(input('Select Your Transaction from the above options: '))
    if choose == 1:
      print(f'{obj.name} your available A/C balance is : {obj.balance:.2f}')
    elif choose == 2:
      withdraw = int(input('Enter Amount:'))
      if withdraw <= obj.balance:
        obj.balance -= withdraw
        print(f' {obj.name} ,Your available balance A/C : {obj.balance:.2f}')
      else:
        print('Insufficient Balance')
    elif choose == 3:
      deposit = int(input('Enter Amount:'))
      obj.balance += deposit
      print(f'{obj.name},your current A/C balance is : {obj.balance:.2f}')
    elif choose == 4:
      print('Thank you!')
      break
    else:
      print('Please select correct option')
  return

# Define main method and calling the class or method in the main method 
def main():
  obj = User(1234,10000,'vishvesh')   # calling class here
  simulator(obj)   # calling method here

# calling main method here
main()                   