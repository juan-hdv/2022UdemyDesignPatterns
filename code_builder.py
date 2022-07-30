# You are asked to implement the Builder design pattern 
# for rendering simple chunks of code.
# 
# Sample use of the builder you are asked to create:
# cb = CodeBuilder('Person')\
#      .add_field('name', '""')\
#      .add_field('age', '0')
# print(cb)
# 
# The expected output of the above code is:
# # class Person: 
#   def __init__(self): 
#       self.name = ""
#       self.age = 0
# Please observe the same placement of spaces and indentation.

class TheClassField:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return "self." + self.name + " = " + str(self.value) + "\n"

class TheClass:
    INDENT = ' '*2

    def __init__(self, name):
        self.name = name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append (TheClassField(name,value))

    def __str__(self):
        result = "class " + self.name + ":\n"
        if self.fields:
            result += 1*self.INDENT + "def __init__(self):\n" 
            for element in self.fields:
                result += 2*self.INDENT + str(element)
        else:
            result += self.INDENT + "pass\n"

        return result

class CodeBuilder:
    def __init__(self, class_name):
        self.theclass = TheClass(class_name)

    def add_field(self, name, value):
        self.theclass.add_field(name, value)
        return self

    def __str__(self):
        return str(self.theclass)

cb = CodeBuilder('Person')\
     .add_field('name', '""')\
     .add_field('age', '0')
print(cb)
