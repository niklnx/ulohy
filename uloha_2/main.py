
print ("napis x souřadnici bodu A")
x1 = int (input())
print ("napis y souřadnici bodu A")
y1 = int (input())
print ("napis x souřadnici bodu B")
x2 = int (input())
print ("napis y souřadnici bodu B")
y2 = int (input())
print ("napis x souřadnici bodu C")
x3 = int (input())
print ("napis y souřadnici bodu C")
y3 = int (input())

vysledek = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2

if vysledek == 0:
    print("bod lezi na primce")
else:
    print("bod nelezi na jedne primce")



