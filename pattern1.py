#solid square
for i in range(0,4): 
    #outer loop runs 4 times that is for rows
    for j in range(0,4): #inner loop runs 4 times for columns
        print("*",end=" ") # print asterik(*) followed the space 
    print() # for moving next line
    
# dryrun:
# 1. i=0  first row
#    j=0,1,2,3 print * four times on line 1
# 2. i=1  second row
#    j=0,1,2,3 print * four times on line 2
# 3. i=2  third row
#    j=0,1,2,3 print * four times on line 3
# 4. i=3   fourth row
#    j=0,1,2,3 print * four times on line 4