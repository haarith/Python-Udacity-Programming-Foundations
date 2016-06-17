class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

billy_haris = Parent("Haris", "black")
print(billy_haris.last_name)
