# Python program to show that we can creat
# instance variables inside methods

# Class for computer science Student
class CSSGenius2:

    # Class variable
    stream = "Computer science"

    # The init method or constructor
    def _init_ (self, classCode):

        # Instance Variable
        self.classCode = classCode

    # Adds an instance variable
    def setAddress(self, address):
        self.address = address

    # Retrieves instance variab;e
    def getAddress(self):
        return self.address

# Driver code
a = CSSGenius2
a.setAddress("Noida, UP")
print (a.getAddress())
