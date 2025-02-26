# Create a list of your favorite movies and print the second one.

movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Lord of the Rings", "Pulp Fiction"]
print(movies[1])

# Create a dictionary for a person (name, age, city) and print their city.

person = { "name":"vedant" , "age" : 11 , "city" : "Mumbai"}
print(person["city"])

# Use a for loop to print numbers from 1 to 10.

for  i in range(1,11):
    print(i)

# Use a while loop to print numbers from 10 to 1.
j = 10
while j > 0:
    print(j)
    j = j - 1

# Write a program that checks if a number is positive, negative, or zero.
num = 10
if num == 0:
    print("Zero")
elif num > 0 :
    print("positive")
else:
    print("negative")

# Write a function to calculate the area of a rectangle (length × width).

def area(length,width):
    print(length*width) 
area(10,29)

# Write a program to find the largest number in a list.

list = [1,34,55,64,32,5,4]
print(max(list))

# Write a function to check if a string is a palindrome (e.g., "madam").

data = "madam"
if data == data[::-1]:
    print("palindrome")