#butterfly pattern
n=5
for i in range(1,n+2):            # outer loop runs 4 times for row
    for j in range(1,i+1):        #inner loop runs i+1 times for column
        print("*",end=" ")      # print * and add space for separation
    print()  
for i in range(n,0,-1):     #count from 4 to 1 for the rows
    for j in range(1,i+1):      #print i rows on current row
        print("*",end=" ")  # print each star on the same line with space
    print()         
