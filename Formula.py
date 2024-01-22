import cmath
A = float(input("Que número es A:"))
B = float(input("Que número es B:"))
C = float(input("Que número es C:"))
Formula1=(-B+cmath.sqrt(B**2-4*A*C))/(2*A)
Formula2=(-B-cmath.sqrt(B**2-4*A*C))/(2*A)
print(Formula1) 
print(Formula2) 