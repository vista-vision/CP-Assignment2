#   Matrix D

r=1
c=3
p=[]

for i in range(r):
    d=[]
    for j in range(c):
        entry=int(input("Enter a value for the matrix (adding columnwise)."))
        d.append(entry)
    p.append(d)