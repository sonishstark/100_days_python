len("1234")

#the type inbuilt function helps you identify what data type it is
print(type("Hello"))
print(type(123))
print(type(12.3))
print(type(True))


#type conversion or casting
int("123")
#converts into numbers and does addition
print(int("123") + int("456"))

name_of_the_user = input("Enter your name\n")
length_of_name = len(name_of_the_user)

#converting the integer to string because it can't concatenate
#now adding str make the entire thing string so we can print
print("Number of letters in your name: " + str(length_of_name))
