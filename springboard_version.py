"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start."""

        self.start = self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to original start."""

        self.next = self.start
        
    """"Why in the generate instance method, is there "return self.next -1"
    if the point of the exercise is to increment? 
    
    Why under the __init__  dunder is the start parameter set to zero? 
    is it indicating that the start of the numbers generated begins at
    an index of zero, or is it some kind of placeholder? Why can't that 
    be left blank?
    
    also under __init__ why is the self.start = self.next = start? is it
    because it assumes that this is the beginning and the first number 
    of the iteration is the starting number?
    """