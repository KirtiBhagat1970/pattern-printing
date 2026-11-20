#hollow sqaure
n=5
for i in range(1,n+1):                     #outer loop run from 1 to 5
    for j in range(1,n+1):                 #inner loop runs from 1 to 5
        if i==1 or j==1 or i==n or j==n:   # if (i==1,j==1,i==5,j==5) print * at that position otherwise space
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# dryrun:
# 1. i=1 -> j=1,2,3,4,5  print : * * * * *
# 2. i=2 -> j=1,2,3,4,5  print : *       *
# 3. i=3 -> j=1,2,3,4,5  print : *       *
# 4. i=4 -> j=1,2,3,4,5  print : *       *
# 5. i=5 -> j=1,2,3,4,5  print : * * * * *