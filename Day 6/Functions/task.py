#checking for date 13thd
def my_dob():
    print("Happy birthday")

def addition(a,b):
    print(a+b)

my_dob()
addition(3,4)


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb():
    turn_left()
    while front_is_clear():
        move()
        if not at_goal():
            while not wall_on_right():
                turn_right()
                move()


while not at_goal():
    if wall_in_front():
        climb()
    else:
        move()