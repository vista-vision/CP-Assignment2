#   Matrix A

r=3
c=3
m=[]

for i in range(r):
    a=[]
    for j in range(c):
        entry=int(input("Enter a value for the matrix (adding columnwise)."))
        a.append(entry)
    m.append(a)