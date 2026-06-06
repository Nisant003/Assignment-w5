# Q1
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")





# Q2
list_q2 = [10, 20, 30, 40]
running_total = 0
for num in list_q2:
    running_total += num
    print(f"Added {num}. Running total is {running_total}.")
print("-" * 30)
print(f"Total Sum: {running_total}")




# Q3
student_names = ["Ram", "Hari", "Sita"]
print(" --- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")




# Q4
pages = [45, 30, 50, 40]
print("--- Book Chapter Summary ---")
for index, page_count in enumerate(pages, start=1):
    print(f"Chapter {index} has {page_count} pages.")





# Q5
given_list = [4, 5, 3, 2]
product = 1
for num in given_list:
    product *= num
print("Product:", product)




# Q6
number = 11
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")





# Q7
given_list = [3, 2, 1, 4, 5]
reversed_list = []
for i in range(len(given_list) - 1, -1, -1):
    reversed_list.append(given_list[i])
print("Reversed list:", reversed_list)




# Q8
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
for item in list1:
    if item in list2:
        common.append(item)
print("Common elements:", common)





# Q9
lst = [1, 2, 3, 4]
for item in lst:
    if item == 1 or item == 4:
        print(item)





# Q10
text = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char not in vowels:
        result += char
print("String without vowels:", result)




# Q11
sentence = 'Loops are Fun'
v_count = 0
c_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
print(f"vowels: {v_count}")
print(f"consonants: {c_count}")





# Q12
given_list = [1, 2, 3, 4, 5]
evens = []
odds = []
for num in given_list:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print("Evens:", evens)
print("Odds:", odds)





# Q13
num = 17
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is prime: {is_prime}")






# Q14
given_list = [1, 2, 3, 4, "a", "b"]
ints = []
strs = []
for item in given_list:
    if type(item) == int:
        ints.append(item)
    elif type(item) == str:
        strs.append(item)
print("Integers:", ints)
print("Strings:", strs)





# Q15
user_input = "Python3.10"
letters = 0
digits = 0
for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print(f"Letters: {letters}")
print(f"Digits: {digits}")




# Q16
username = "user123"
password = "securePass1"
valid = True
for char in username:
    if char.isspace():
        valid = False
if len(password) < 6:
    valid = False
if valid:
    print("Valid Credentials")
else:
    print("Invalid Credentials")





# Q17
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")





# Q18
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")




# Q19
for i in range(1, 9):
    print(f'Table of {i} ')
    for j in range(1,11):
        print(f'{i} x { j } = {i * j}')



# Q20
lst = [1, 2, 3, 4]
for item in lst:
    if item == 1 or item == 2:
        print(item)





# Q21
start, end = 1, 10
odd_sum = 0
for i in range(start, end + 1):
    if i % 2 != 0:
        odd_sum += i
print("Sum of odds:", odd_sum)





# Q22
start, end = 1, 10
even_sum = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        even_sum += i
print("Sum of evens:", even_sum)





# Q23
text = "Keep coding and practicing"
space_count = 0
for char in text:
    if char == " ":
        space_count += 1
print("Total spaces:", space_count)




# Q24
given_list = [1, 2, 3, 4]
cubed_list = []
for num in given_list:
    cubed_list.append(num ** 3)
print(cubed_list)





# Q25
a = "programming"
reversed_str = ""
for char in a:
    reversed_str = char + reversed_str
print(reversed_str)





# Q26
for i in range(50):
    print(i, end=" ")
    if i == 7:
        break
print()




# Q27
text = "Python"
for letter in text:
    print(letter)





# Q28
a = ["ram", "shyam", 1, 2]
for name in a:
    if isinstance(name, str):
        print(f"Hello!{name}", end=" ")
print()





# Q29
a = ["ram", "shyam"]
lst = []
for item in a:
    lst.append(f"Dr.{item}")
print(lst)




# Q30
numbers = [1, 2, 3, 4]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)




# Q31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positive_lst = []
for num in lst1:
    if num > 0:
        positive_lst.append(num)
print(positive_lst)





# Q32
given_list = [0, 1, 2, 3, 4, 5, 6]
for num in given_list:
    if num == 3 or num == 6:
        continue
    print(num)





# Q33
first_list = [10, "hello", 3.14, True]
second_list = []
for item in first_list:
    second_list.append(type(item))
print(second_list)




# Q34
for i in range(3):
    print(i)
else:
    print("Done")





# Q35
for i in range(105, 6, -7):
    print(i, end=" ")
print()





# Q36
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
clean_string = ""
for char in string:
    if char not in bad_chars and char != " ":
        clean_string += char
print(clean_string)




# Q37
series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens_count = 0
odds_count = 0
for num in series:
    if num % 2 == 0:
        evens_count += 1
    else:
        odds_count += 1
print(f"Even numbers: {evens_count}")
print(f"Odd numbers: {odds_count}")





# Q38
total_sum = 0
for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i
print("Sum of multiples:", total_sum)





# Q39
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of evens: {even_sum}")
print(f"Sum of odds: {odd_sum}")





# Q40
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for num in list1:
    if num == target:
        count += 1
print(f"The number {target} appears {count} times in the list .")