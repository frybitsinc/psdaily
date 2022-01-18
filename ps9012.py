n = int(input())

for i in range(n):
    data = input()
    ps = []
    for j in data:
        if j=="(":
            ps.append(j)
        elif j==")":
            if len(ps)!=0 and ps[-1]=="(":
                ps.pop()
            else:
                ps.append(")")
                break
    if len(ps)==0:
        print("YES")
    else:
        print("NO") 
