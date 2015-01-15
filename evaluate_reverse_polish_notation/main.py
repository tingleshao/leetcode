class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for j in tokens:
          if len(j) > 1 and j[0] == "-":
            j = j[1:]
            stack.insert(0,-1*int(j))
          elif j.isdigit():
            stack.insert(0,int(j))
          else:
            if j == "+":
              a = stack.pop(0)
              b = stack.pop(0)
              res = b + a 
              stack.insert(0,res)
            elif j == "-":
              a = stack.pop(0)
              b = stack.pop(0)
              res = b - a 
              stack.insert(0,res)
            elif j == "*":
              a = stack.pop(0)
              b = stack.pop(0)
              res = b * a 
              stack.insert(0,res)
            elif j == "/":
              a = float(stack.pop(0))
              b = float(stack.pop(0))
              res = b / a 
           #   if res == -1 and a < 0 and abs(a) > abs(b):
           #     stack.insert(0,0)
          #    else:
              stack.insert(0,int(res))
        return stack[0]
				

def main():
    s = Solution()
    a1 = ["2", "1", "+", "3", "*"]
    a2 = ["4", "13", "5", "/", "+"]
    a3 = ["3","-4","+"]
    a4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    a5 = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    print s.evalRPN(a1)
    print s.evalRPN(a2)
    print s.evalRPN(a3)
    print s.evalRPN(a4)
    print s.evalRPN(a5)
  
if __name__ == "__main__":
    main()