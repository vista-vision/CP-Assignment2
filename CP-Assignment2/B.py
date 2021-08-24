#   Matrix B

r=3
c=3
n=[]

for i in range(r):
    b=[]
    for j in range(c):
        entry=int(input("Enter a value for the matrix (adding columnwise)."))
        b.append(entry)
    n.append(b)