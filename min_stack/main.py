class MinStack:
    # @param x, an integer
    # @return an integer
    
    def __init__(self):
      self.stk = []
      self.min = []
      
    def push(self, x):
      self.stk.append(x)
      if len(self.min) == 0 or self.min[-1] >= x:
        self.min.append(x)
    
      return len(self.stk)
        
    # @return nothing
    def pop(self):
      if len(self.stk) > 0:
        tp = self.stk.pop(-1)
        if tp == self.min[-1]:
          self.min.pop(-1)
        

    # @return an integer
    def top(self):
      if len(self.stk) > 0:
        return self.stk[-1]
        

    # @return an integer
    def getMin(self):
        return self.min[-1]