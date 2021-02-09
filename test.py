a = 1#float(input("Hvad er a: "))
b = 2#float(input("Hvad er b: "))
c = 3#float(input("Hvad er c: "))

d = float(b*b) - (4*a*c)
print("d = ", d)

ls1 = (-b-pow(d,0.5))/(2*a)
ls2 = (-b+pow(d,0.5))/(2*a)

if d < 0:
    print("andengradsligningen kan ikke løses")
elif d==0:
     print("der er 1 løsning og den giver", ls1)
elif d > 0:
    print("der er 2 x værdier", ls2," og", ls1) 

print("Toppunkt:")
topx = -b / (2*a)
topy = -d / (4*a)
print("("+str(topx)+", "+str(topy)+")")