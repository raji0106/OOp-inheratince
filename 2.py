class Employee(Person):

    def __init__(self, name, age, employye_id, department, performance_rating):
        super(), self.__init__(name, age, employye_id)
        self.department = department
        self.performance_rating = performance_rating

    def calculate_bonus(self, salary):
        if self.performance_rating >= 9:
            return salary * 0.20
        elif self.performance_rating >=7:
            return salary * 0.15
        elif self.performance_rating >=5:
            return salary * 0.10
        else:
            return salary * 0.05

    def dispaly_deatails (self):
        super().display_deatails()
        print(f"Department: [self.departmemnt]")
        print(f"Performance Rating: [self.performance_rating]/10")