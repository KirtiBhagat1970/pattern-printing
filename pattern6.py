#right aligned triangle

n=5
for i in range(1,n+1):      # outer loop runs from 1 to 6
    for sp in range(n-i):   #print space n-i times in same row
        print(" ",end=" ")  # print space on sam eline
    for j in range(i):      
        print("*",end=" ")
    print()                #move to next line

# dryrun:
# 1.i=1 -> sp=5-1=4 j=0           (1 times) print         *
# 2.i=2 -> sp=5-2=3 j=0,1         (2 times) print       * *
# 3.i=3 -> sp=5-3=2 j=0,1,2       (3 times) print     * * *
# 4.i=4 -> sp=5-4=1 j=0,1,2,3     (4 times) print    * * * *
# 5.i=5 -> sp=5-1=0 j=0,1,2,3,4   (5 times) print  * * * * *

    
