class SerialNumbers:
    numbers_countup = 0
    def __init__(self, numbers):
        self.numbers = numbers
        SerialNumbers.numbers_countup += 1
        
    def reset(self):
         self.numbers = SerialNumbers.numbers_countup
         +++
         
         
        
        
