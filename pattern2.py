#right angled triangle
for i in range(0,4): # outer loop runs 4 times for row
    for j in range(i+1): #inner loop runs i+1 times for column
        print("*",end=" ") # print * and add space for separation
    print()  #goes to next line
    
# dryrun:
# 1. i=0  first row
#    j=0,1 print * 1 times on line 1
# 2. i=1  second row
#    j=0,1,2 print * 2 times on line 2
# 3. i=2  third row
#    j=0,1,2,3 print * 3 times on line 3
# 4. i=3   fourth row
#    j=0,1,2,3,4 print * 4 times on line 4