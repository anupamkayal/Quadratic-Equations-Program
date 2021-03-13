#-----------Quadratric Equations-------------
a= int(input('please enter the value of a:  '))
b= int(input('please enter the value of b:  '))
c=int( input('please enter the value of c:  '))
import math

def quadratric(a,b,c,):
	d=math.sqrt((b**2-4*a*c))
	x=(-(b)+d)/(2*a)
	print('+x='+str(x))
	d=math.sqrt((b**2-4*a*c))
	x=(-(b)-d)/(2*a)
	print('-x='+str(x))
	
quadratric(a,b,c,)
	
	
	
	



