# Part 1: Create the parant class with shared family traits
class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Height (cm)", self.height_cm)

# Part 2: create the child class that inheratis from family member
class kid(FamilyMember):

    # Part 3 : give kid its own details, plus inheritad traits.
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    # PArt 4: Ovviride show_traits to add to the kids own details too
    def show_traits(self):
      print("Name", self.name)
      print("age", self.age)
      super().show_traits()

# Part 5: ADd a brand new method that only kid has
    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)

# Part 6:  create a kid object with real family trait values
child = kid("Maya", 10, "Brown", 140)

#7
child.show_traits()
child.favorite_hobby("Painting")

# Part 8: check weather kid is raelly a subclass of familyyMember
print(" Is kid a subclass of FamilyMemeber?", issubclass(kid, FamilyMember))