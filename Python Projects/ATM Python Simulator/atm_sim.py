# Define a class to represent an ATM machine
class ATM:
  # Initialize the ATM with a given balance
  def __init__(self, balance):
    self.balance = balance

  # Function to check the balance
  def check_balance(self):
    print(f"Your balance is ${self.balance}.")

  # Function to withdraw money
  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds.")
    else:
      self.balance -= amount
      print(f"You withdrew ${amount}. Your new balance is ${self.balance}.")

  # Function to deposit money
  def deposit(self, amount):
    self.balance += amount
    print(f"You deposited ${amount}. Your new balance is ${self.balance}.")

# Create a new ATM with a starting balance of $1000
atm = ATM(1000)

# Main loop to handle user input
while True:
  print("Enter a command:")
  print("1 - Check balance")
  print("2 - Withdraw money")
  print("3 - Deposit money")
  print("4 - Exit")

  # Get the user's command
  command = int(input())

  # Handle the user's command
  if command == 1:
    atm.check_balance()
  elif command == 2:
    print("Enter the amount to withdraw:")
    amount = int(input())
    atm.withdraw(amount)
  elif command == 3:
    print("Enter the amount to deposit:")
    amount = int(input())
    atm.deposit(amount)
  elif command == 4:
    break
  else:
    print("Invalid command.")
