s=["{ [ ( ) ] }","( [ ) ]","{ { [] ( } } )","{ [ ( ) ] }"]
for j in s:
    m=j.split()
    left =[]
    for i in m:
        if i=="(" or i=="{" or i=="[":
            left+=[i]
        elif i==")" and left[len(left)-1]=="(" and len(left)!=0:
            left.pop()
        elif i=="}" and left[len(left)-1]=="{" and len(left)!=0:
            left.pop()
        elif i=="]" and left[len(left)-1]=="[" and len(left)!=0:
            left.pop()
    if len(left)==0:
        print("True")
    else:
        print("False")