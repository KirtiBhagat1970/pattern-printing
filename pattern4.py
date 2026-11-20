#increasing number triangle
for i in range(1,6):   #outer loop runs from 1 to 5 stop before 6
    for j in range(1,i+1): # inner loop runs from 1 to current row value
        print(j,end=" ")   # prints value of j stay on current row
    print()                #moves to next line
    
# dryrun:
#  1.   i=1
#     j=1,2 print 1
# 2.   i=2
#      j=1,2,3 print 1,2
# 3.   i=3
#      j=1,2,3,4 print 1,2,
# 4.  i=4
#     j=1,2,3,4,5 print 1,2,3
# 5.  i=5
#     j=1,2,3,4,5,6 print 1,2,3,4

    