
f = open("ex.txt").readlines()
group1 = [] 
group2 = [] 
red="\x1b[41m"
reset = "\x1b[0m"

for i in f : 
    
    if  0 < float(i) <5:
        group1.append(float(i))
    elif -5< float(i) <0 :
        group2.append(float(i))


count1 = len(group1)
count2 = len(group2)
total = count1 + count2 
pr1 = count1/total 

pr2 = count2/total
height = 20.0
h1 = pr1*height
h2 = pr2*height
print(h2)
width = 20 
for row in range(int(height) , 0 , -1):
    if row<=h1:
        left = (red+" "+reset)*width
    else: left = " "* width
    if row <= h2 :
        right = (red+" "+reset)* width 
    else: right = " "* width 
    print(f"    {left}                                           {right}")
print("    "+ str(pr1*100) + "%                                             "+str(pr2*100)+"%")