#   Matrix C

r=1
c=3
o=[]

for i in range(r):
    q=[]
    for j in range(c):
        entry=int(input("Enter a value for the matrix (adding columnwise)."))
        q.append(entry)
    o.append(q)