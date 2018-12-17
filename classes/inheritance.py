class Parent():
    def implicit(self):
        print("Parent implicit()")
    def override(self):
        print("Parent override()")
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def override(self):
        print("Child override()")
    def altered(self):
        print("Child altered()")
        super(Child, self).altered()
        print("After super()")

parent = Parent()
child = Child()

parent.implicit()
child.implicit()
child.override()
parent.altered()
child.altered()