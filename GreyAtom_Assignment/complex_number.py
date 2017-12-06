# Complex number package
import numpy as np
import sys

class complex_number:
    def __init__(self,x= 0,y = 0):
        self.real = x
        self.imag = y

    def getData(self):
        print("{0}+{1}i".format(self.real,self.imag))

    def add(self,other):
    	print("Addition is","{0}+{1}i".format(self.real+other.real,self.imag+other.imag))
    	
    def sub(self, other):
        print("Substraction is ","{0}+{1}i".format(self.real-other.real,self.imag-other.imag))

    def mul(self, other):
    	print("Multiplication is ","{0}+{1}i".format(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag))
       

    def div(self, other):
        SR, SI, OR, OI = self.real, self.imag, other.real, other.imag 
        r = OR**2 + OI**2
        try:
        	print("Division is ","{0}+{1}i".format((SR*OR+SI*OI)/r, (SI*OI-SR*OI)/r))
        except ZeroDivisionError:
       		print("Cannot divide by zero")
            
    def abs(self):
    	print("Absolute is ","{0}".format(self.real**2 + self.imag**2))

    def Real(self):
    	return self.real

    def Imaginary(self):
    	return self.imag

    def conjugate(self):
    	return complex_number(self.real ,- self.imag)
    	
    def argument(self):
    	if (self.real==0 and self.imag==0):
    		print("complex number 0+0i has magnitude zero, but doesn’t really have an angle.") 
    		sys.exit()
    	elif (self.real==0 and self.imag>=0 ):
    		return int(90)
    	elif self.real==0 and self.imag<0 :
    		return int(270)
    	else:
    		return np.arctan(self.imag/self.real)
    

try:
	# first complex number is X+Yi
	X =6
	Y=4.3
	# second complex number is X1+Y1i
	X1=3
	Y1=2.7
	if type(X) == int or type(X1) == float or type(X1) == int or type(Y1) == float:  
	  	print("Valid number")
except:
    print("Please enter valid int or float number")
    sys.exit(1) 

# Create a new complex_number object
c1 = complex_number(X,Y) 
# Create a new complex_number object
c2 = complex_number(X1,Y1)
# Call getData() function
c1.getData()
c2.getData()
c1.add(c2)
c1.sub(c2)
c1.mul(c2)
c1.div(c2)
c1.abs()
print("Real part is ",c1.Real())
print("Imaginary part is ",c1.Imaginary())
a=c1.conjugate()
if a.imag>=0:
	print("Conjugate is ","{0}+{1}i".format(a.real,a.imag))
else:
	print("Conjugate is ","{0}{1}i".format(a.real,a.imag))
b=c1.argument()
print("Argument is ",b)

