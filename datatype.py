# Data type
number = 100  # int
second = 56.78  # float
text = "Hello there"  # str
ispythoninteresting = True  # bool

# storing multiple values in a variable
cars = ["toyota", "Nissan", "md"]  # List
fruits = ("banana", "oranges", "apples")  # Tuple
countries = {"Kenya", "Uganda", "Congo", "Rwanda"}  # set
details = {
    "firstname": "Robert",
    "age": 32,
    "course": "web development",
    "Nationality": "Kenyan"
}  # Dictionary
print(details["firstname"])
print(details["age"])
print(second)
print(text)
print(cars)
print(countries)

# determine a data type
print(type(text))
print(type(countries))
print(type(details))

# typecasting - converting one data to another
print(float(number))
print(int(second))
