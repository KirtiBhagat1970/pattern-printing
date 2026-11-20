#hollow right angled triangle
n=5
for i in range(1,n+1):              #outer loop runs from 1 to 5
    for j in range(1,i+1):          #inner loop runs from 1 to i value
        if j==1 or j==i or i==n:    # if any of condition is true of this the * will be printed
            print("*",end=" ")
        else:
            print(" ",end=" ")      # if condition is false print space at that place
    print()                         #move to next line
    
# dryrun:
# 1. i=1 -> j=1           print:*
# 2. i=2 -> j=1,2         print:* *
# 3. i=3 -> j=1,2,3       print:*   *
# 4. i=4 -> j=1,2,3,4     print:*     *   
# 5. i=5 -> j=1,2,3,4,5   print:* * *  *
 