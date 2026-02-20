#initiate a class...
class employee:
    #special method
    def __init__(self):
        self.id =123
        self.salary=100000
        self.designation="SDE"

    #writing method or function of class..
    def travel(self,designation):
        print(f"employee is traveling to {designation}")

#creating an object..of the class..
sam=employee()
print(sam.id)
print(sam.salary)
print(sam.designation)
#calli ng a method..
sam.travel("delhi")