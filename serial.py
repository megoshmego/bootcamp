from incremental_counter import Counter

class serial:
    
    def __init__(self, start = 0,):
        self.start = self.inc = self 
                
           
    def inc(self):
        """"returns next number"""
        self.inc()
        return self.inc()
    
    def restart(self):
        """resets number to 100"""
        self.inc = self.start