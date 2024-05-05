# num = float(input("Enter any number: "))
#
# if num%2==0:
#     print("The number is even.")
# else:
#     print("The number is even.")

# num1 = float(input("Enter any number: "))
# num2 = float(input("Enter any number: "))
#
# product = num1 * num2;
#
# print(f"The product of {num1} and {num2} is {product}")

# year = int(input("Enter year: "))
#
# if year%4==0:
#     print(f"{year} is a leap year.")
# elif year%400==0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# sentence = input("Enter any sentence: ")
# list_of_words = sentence.split()
# total_words = len(list_of_words)
# print(f"The given sentence has {total_words} words.")

# age = int(input("Enter your age: "))
#
# if age<=0:
#     print("The age is invalid.")
#
# elif age<18:
#     print("You are not eligilbe to vote.")
# else:
#     print("You are eligible to vote.")

# num = float(input("Enter any number: "))
#
# if num%2==0 and num%3==0:
#     print(f"{num} is divisible by 2 and 3.")
# else:
#     print(f"{num} is not divisible by 2 and 3.")

# name = input("Enter your name: ")
# def hello(name):
#     print(f"Hello, {name}!")
#
# hello(name)

def fn1():
    print("hello from fn1")

def fn2():
    print("hello from fn2")

# def main():
#     fn1()
#     fn2()
#
# main()

# num1 = float(input("Enter any number: "))
# num2 = float(input("Enter any number: "))
# num3 = float(input("Enter any number: "))
#
# def sum3nums(num1,num2, num3):
#     sum = num1+num2+num3
#
#     print(f"The sum of three numbers is {sum}")
#
# sum3nums(num1,num2,num3)

# number = float(input("Enter any number: "))
#
# def mul_of_3(num):
#     if num%3==0:
#         print(f"{num} is multiple of 3.")
#     else:
#         print(f"{num} is not multiple of 3.")
#
# mul_of_3(number)


# marks = float(input("Enter your marks: "))

# def check_grade(gpa):
#     if marks > 100:
#         print("Enter valid marks.")
#     elif marks>=90:
#         print("A")
#     elif marks >=80:
#         print("B")
#     elif marks>=70:
#         print("C")
#     elif marks>=60:
#         print("D")
#     elif marks>=0:
#         print("F")
#     else:
#         print("Enter Valid marks.")
#
# check_grade(marks)

# num1 = float(input("Enter any number: "))
# num2 = float(input("Enter any number: "))
# num3 = float(input("Enter any number: "))
#
# def max_num(num1,num2,num3):
#     maxim = max(num1,num2,num3)
#     print(f"Maximum number is {maxim}")
# max_num(num1,num2,num3)

# letter = input("Enter any letter: ")
# vowel_letter = ["a","e","i","o","u"]
# def check_vowel(letter):
#     if letter in vowel_letter:
#         print(f"{letter} is vowel.")
#     else:
#         print(f"{letter} is not vowel.")
#
# check_vowel(letter)

# ls =["aanik", "magar", 45]
# print(len(ls))


# print(list(range(6)))
# print(list(range(1,6)))


# numbers = [1,2,3,4,5]
# total = sum(numbers)
# print(total)

# list are mutable

# fruits = ["banana", "cherry", "apple"]
# # print(sorted(fruits))
# new_fruit = []
# for fruit in fruits:
#     if "cherry" in fruit:
#         break
#     else:
#         new_fruit.append(fruit)
#
# print(new_fruit)

# tupules are immutable

# fruits = ("banana", "cherry", "apple")
# # print(sorted(fruits))
# new_fruit = ()
# for fruit in fruits:
#     if "cherry" in fruit:
#         break
#     else:
#         new_fruit.append(fruit)
#
# print(new_fruit)

# numbers = [1,2,3,4,5]
# new_num = [num for num in numbers if num < 5]
# print(new_num)

# num = int(input("Enter any integer: "))
# multiples = range(1,11)
# mul_num = []
# for mul in multiples:
#     if mul > 11:
#         break
#     else:
#         mul_num.append(num * mul)
# print(mul_num)

# num = int(input("Enter any integer: "))
#
# def calc_fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * calc_fact(n-1)
#
# num_fact = calc_fact(num)
#
# print(f"Factorial of {num} is {num_fact}.")


# 1. ans
# numbers = range(1,6)
# new_number = []
# for num in numbers:
#     if num == 6:
#         break
#     else:
#         new_number.append(num)
#
# print(new_number)

# 2. ans

# numbers = range(1, 11)
# sum = 0
#
# for num in numbers:
#     if num == 11:
#         break
#     else:
#         sum += num
# print(sum)

# 3. ans
# fruits = ["mango", "banana", "orange", "pineapple"]
# for fruit in fruits:
#     print(fruit)

# 4. ans

# vowels = ["a","e","i","o","u"]
# total = 0
#
# for vowel in vowels:
#     if vowel in vowels:
#         total += 1
# print(total)

# 5. ans
# numbers = range(1, 21)
# even_numbers = []
#
# for number in numbers:
#     if number >= 20:
#         break
#     elif number % 2 == 0:
#         even_numbers.append(number)
#
# print(even_numbers)

# 7. ans
# numbers = range(1, 6)
# sqr_num = []
# for number in numbers:
#     if number >=6:
#         break
#     else:
#         sqr_num.append(number**2)
# print(sqr_num)


# 8. ans
# number = int(input("Enter any integer: "))
# factorial = 1
#
# if number >= 1:
#     for number in range(1, number+1):
#         factorial = factorial*number
#
# print(factorial)


# 9. ans
# names = ["Aanik", "Noah", "Nitesh", "Neesha", "Nabish"]
#
# for name in names:
#     print(f"Hello {name}!")

# 10. ans
# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for number in range(1,11):
#     n3 = n1 + n2
#     print(n3)
#     n1,n2 = n2,n3

# 11. ans
# list_numbers = [3,4,7,2,9,6,8]
# greatest = list_numbers[0]
#
# for number in list_numbers:
#     if number > greatest:
#         greatest = number
# print(greatest)

# quiz = [("What is the capital of France?", "c", ["a) London", "b) Berlin", "c) Paris", "d) Rome"]),
#         ("What is 2+2?", "b", ["a) 3", "b) 4", "c) 5", "d) 6"]),
#         ("What is the largest planet in our solar system?", "d", ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"]),
#         ("Who wrote Romeo and Juliet?", "c", ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) Mark Twain"])
# ]
#
# # Function
# def run_quiz(quiz):
#     score = 0
#
#     for question, correct_answer, options in quiz:
#         print(question)
#         for option in options:
#             print(option)
#
#         user_answer = input("Enter the letter of your answer (e.g., 'a', 'b', 'c', 'd': ")
#
#         if user_answer == correct_answer:
#             print("Correct!\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {correct_answer}\n")
#
#     return score
#
# # Main Program
# if __name__ == "__main__":
#     print("Welcome to the Simple Quiz!\n")
#     total_questions = len(quiz)
#     user_score = run_quiz(quiz)
#
#     print(f"You got {user_score} out of {total_questions} questions correct.")
#     percentage = (user_score / total_questions) * 100
#     print(f"Your percentage is {percentage}%")


# import random
#
#
# # Function to generate random addition or subtraction questions
# def generate_question():
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     operator = random.choice(["+", "-"])
#
#     if operator == "+":
#         answer = num1 + num2
#     else:
#         answer = num1 - num2
#
#     question = f"What is {num1} {operator} {num2}?"
#
#     return question, answer
#
#
# # Function to run the math quiz
# def run_math_quiz(num_questions):
#     score = 0
#
#     for _ in range(num_questions):
#         question, correct_answer = generate_question()
#         print(question)
#         user_answer = int(input("Your answer: "))
#
#         if user_answer == correct_answer:
#             print("Correct!\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {correct_answer}\n")
#
#     return score
#
#
# # Main program
# if __name__ == "__main__":
#     print("Welcome to the Math Quiz!\n")
#     num_questions = 5  # You can change the number of questions here
#     user_score = run_math_quiz(num_questions)
#
#     print(f"You got {user_score} out of {num_questions} questions correct.")
#     percentage = (user_score / num_questions) * 100
#     print(f"Your score is {percentage}%.")


# Define a list of true/false questions and answers as tuples (question, correct answer)
# true_false_quiz = [
#     ("The Earth is flat.", False),
#     ("The capital of France is Paris.", True),
#     ("Python is a compiled language.", False),
#     ("Water boils at 100 degrees Celsius at sea level.", True),
#     ("The moon is made of cheese.", False),
#     ("The sun rises in the west.", False),
# ]
#
# # Function to run the true/false quiz
# def run_true_false_quiz(quiz):
#     score = 0
#
#     for question, correct_answer in quiz:
#         print(question)
#         user_answer = input("True or False? (Enter 'T' or 'F'): ").strip().lower()
#
#         if (user_answer == "t" and correct_answer) or (user_answer == "f" and not correct_answer):
#             print("Correct!\n")
#             score += 1
#         else:
#             print("Wrong!\n")
#
#     return score
#
# # Main program
# if __name__ == "__main__":
#     print("Welcome to the True/False Quiz!\n")
#     total_questions = len(true_false_quiz)
#     user_score = run_true_false_quiz(true_false_quiz)
#
#     print(f"You got {user_score} out of {total_questions} questions correct.")
#     percentage = (user_score / total_questions) * 100
#     print(f"Your score is {percentage}%.")


# class Person:
#
#     def __init__(self, name, age):        # __init__ does not return value, it only initializes the values
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"hello {self.name}"
#
# person1 = Person("aanik", 20)
# print(person1.name)
# print(person1.greet())

# from tkinter import *
#
# x = Label (text="Hello, World!")
# x.pack()
# x.mainloop()


# class Person:
#     name = ''
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#
# class Employee(Person):
#     emp_no = 0
#
#     def get_emp_no(self):
#         return self.emp_no
#
#     def set_emp_no(self, new_emp_no):
#         self.emp_no = new_emp_no
#
#     def get_name(self):
#         return 'Mr. ' + self.name
#         return 'Mr. ' + Person.get_name(self)
#
#
# E = Employee()
#
# E.set_name("Aanik")
# print(E.get_name())
#
# E.set_emp_no(1)
# print(E.get_emp_no())


class BankAccount:

    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance

    def get_acc_num(self):
        return self.account_num

    def set_acc_num(self, account_num):
        self.account_num = account_num

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, account_num, deposit_amt):

        if self.account_num == account_num:
            new_balance = self.get_balance() + deposit_amt
            self.set_balance(new_balance)
            return "Rs." + str(deposit_amt) + " is added to your bank account."

    def withdraw(self, account_num, withdraw_amt):

        if self.account_num == account_num:
            if self.get_balance() > withdraw_amt:
                new_balance = self.get_balance() - withdraw_amt
                self.set_balance(new_balance)
                return "Rs." + str(withdraw_amt) + " is deducted from your bank account."
            else:
                print("Insufficient Balance!")

    def display_balance(self, account_num):

        if self.account_num == account_num:
            return "Your current balance is Rs." + str(self.get_balance())


class SavingAccount(BankAccount):
    def __init__(self, account_num, balance):
        super().__init__(account_num, balance)

    def calc_interest(self, account_num, time, rate):
        if self.account_num == account_num:
            if self.get_balance() > 0:
                interest = (self.get_balance()*time*rate)/100
                self.set_balance(self.get_balance()+interest)
                return "Rs." + str(interest) + " interest is added to your bank account."
            else:
                print("Insufficient balance")

    def display_balance(self, account_num):

        if self.account_num == account_num:
            return "Your current balance is Rs." + str(self.get_balance())+" including interest."


aanik = SavingAccount(account_num=23456789, balance=2000)
# aanik.deposit(123456789, 1000)
aanik.withdraw(23456789, 500)
aanik.calc_interest(23456789, 3, 10)
print(aanik.display_balance(23456789))


