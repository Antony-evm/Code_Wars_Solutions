# Description:
# My 7th kata, a Python puzzle, define x such that str(x) raises an exception.

# Note that str() calls rarely raise an exception
# You cannot simply define a custom class and overide __str__
#(actually it is possible, but I've forbiden the easiest ways), or redefine str, but there are multiple other solutions.

class Root:
    def __str__(self):
        raise ValueError("Nope I'm broken")

class Broken(Root):
    pass
        
x = Broken()

# Attributed to @ChristianECooper