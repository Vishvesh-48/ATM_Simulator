# ATM_Simulator

## Project Overview
This project is an ATM Machine Simulator implemented in Python. The purpose of this project is to simulate basic ATM functionalities, such as checking the balance, withdrawing money, depositing money, and exiting the session. The simulator interacts with the user through the command line.

## Thought Process and Design

### Class Definition
The first step was to create a `User` class to encapsulate user-related data and methods. This class includes attributes for the user's PIN, balance, and name. The `__init__` method initializes these attributes when a `User` object is created.

### ATM Simulator Function
The next step was to design the `simulator` function, which serves as the main interface for the user to interact with the ATM. This function performs the following tasks:
- Displays a welcome message.
- Verifies the user's PIN.
- Provides options for different ATM functionalities.
- Handles user inputs and performs the corresponding actions (check balance, withdraw, deposit, exit).

### Error Handling and User Experience
To ensure a smooth user experience, basic error handling was incorporated to manage incorrect PIN entries and insufficient balance situations. This ensures that the user is informed of any issues in a clear and friendly manner.

### Implementation

Here’s the implementation of the `User` class and `simulator` function:

#### User Class
```python
class User:
    def __init__(self, pin, balance, name):
        self.pin = pin
        self.balance = balance
        self.name = name
```
## Simulator Function
```python
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
        choose = int(input('Select Your Transaction from the above options: '))
        if choose == 1:
            print(f'{obj.name} your available A/C balance is : {obj.balance:.2f}')
        elif choose == 2:
            withdraw = int(input('Enter Amount:'))
            if withdraw <= obj.balance:
                obj.balance -= withdraw
                print(f'{obj.name}, Your available balance A/C : {obj.balance:.2f}')
            else:
                print('Insufficient Balance')
        elif choose == 3:
            deposit = int(input('Enter Amount:'))
            obj.balance += deposit
            print(f'{obj.name}, your current A/C balance is : {obj.balance:.2f}')
        elif choose == 4:
            print('Thank you!')
            break
        else:
            print('Please select correct option')
    return
  ```
### Main Function
The main function initializes a User object and calls the simulator function:
```python
def main():
    obj = User(1234, 10000, 'Vishvesh')  # Create a User object
    simulator(obj)  # Call the simulator function with the User object

if __name__ == "__main__":
    main()  # Call the main function
```
### Running the Project
To run this project on your local machine:

1-Ensure Python is installed. You can download it from python.org.

2-Navigate to the project directory:
```sh
cd <project_directory>
```
3-Run the script:
```sh
python <script_name>.py
```
Replace <project_directory> with the path to your project directory and <script_name> with the name of your Python script file, e.g., main.py.

### Future Improvements
Add functionality to change the PIN.
Implement more robust error handling.
Create a graphical user interface (GUI) for better user experience.
### Acknowledgements
Thanks to all who inspired and guided this project.

### Save and Commit the README.md

1. **Save the File:**
   - After writing your `README.md`, save the file by clicking `File > Save` or pressing `Ctrl+S`.

2. **Move the File to Your Local Machine Folder:**
   - If you're using Google Colab, download the `README.md` file to your local machine.
   - Move the `README.md` file to your project directory on your local machine.

3. **Version Control (Optional):**
   - If you are using version control (e.g., Git), you can add and commit the `README.md` file to your repository:
     ```sh
     git add README.md
     git commit -m "Add README.md with project details"
     ```

By following these steps, you will have a detailed `README.md` file in your project directory that explains the project's purpose, design, usage, and other relevant information.


