#repeated row number triangle

for i in range(1,6):  #outer loop runs from 1 to 5 
    for j in range(1,i+1): #inner loop runs from 1 to i+1
        print(i,end=" ")   #print row value separete with space
    print()
    
# dryrun:
# 1. i=1 -> j runs 1         (1 times) -> print:1
# 2. i=2 -> j runs 1,2       (2 times) -> print: 2 2
# 3. i=3 -> j runs 1,2,3     (3 times) -> print:3 3 3 
# 4. i=4 -> j runs 1,2,3,4   (4 times) -> print:4 4 4 4
# 5. i=5 -> j runs 1,2,3,4,5  (5 times) -> print:5 5 5 5 5

