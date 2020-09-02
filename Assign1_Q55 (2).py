a = 1.0
b = 3.0
c = 7.0
x1 = 3.0
y1 = 8.0
x= ((2*a*c)-(2*b*a*y1)-(x1*(a*a-b*b)))/(a*a+b*b); 
y= ((a*a-b*b)*y1-2*a*b*x1+2*b*c)/(a*a+b*b);  
print("Image of the point (" + str(x1) + ", " + str(y1) + ") is")
print( "(" + str(x) + ", " + str(y) + ")" )