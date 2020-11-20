# Class for computer Science Students
class CSSGenius:

    # Class viariable
    stream = "Computer science"

    # The init method or constructor
    def _init_ (self, classCode):

        # Instance Variable
        self.classCode = classCode

# Objects of CSStudent class
a = CSSGenius(101)
b = CSSGenius(102)

print(a.stream) # prints "Computer Science"
print(b.stream) # prints "Computer Science"
print(a.classCode) # prints 101

# Class variables can be accessed using class
# name also
print (CSSGenius.stream) # prints "Computer science" 
