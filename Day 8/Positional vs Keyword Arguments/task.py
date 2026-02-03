# Functions with two input
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}?")

#positional argument
greet_with_name("Jack Bauer", "Virginia")

#conditional argument
greet_with_name(name = "John", location = "New York")
