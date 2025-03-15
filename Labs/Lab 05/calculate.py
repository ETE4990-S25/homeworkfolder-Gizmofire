class Calculator(object):
    def add(self,x,y):
        return x + y
    
    def subtract(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def divide(self,x,y):
        if y == 0:
            raise ValueError("Can not divide by zero!")
        return x / y
    
if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(2,2)
    print(result)