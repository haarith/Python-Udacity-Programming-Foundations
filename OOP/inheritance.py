class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        
#billy_haris = Parent("Haris", "black")
#print(billy_haris.last_name)

miley_haris = Child("Haris", "brown", 3)
print(miley_haris.last_name)
print(miley_haris.number_of_toys)
