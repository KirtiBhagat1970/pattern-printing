#diamond
n=5
for i in range(1,n+1):        #star pyramid
    for sp in range(n-i): 
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):     #inverted star pyramid
    for sp in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
    
# dryrun:
# 1. i=1 -> sp=5-1=4 j=2*1-1=1 j=0                  print:        *
# 2. i=2 -> sp=5-2=3 j=2*2-1=3 j=0,1,2              print:      * * *
# 3. i=3 -> sp=5-3=2 j=2*3-1=5 j=0,1,2,3,4          print:    * * * * * 
# 4. i=4 -> sp=5-4=1 j=2*4-1=7 j=0,1,2,3,4,5,6      print:  * * * * * * *
# 5. i=5 -> sp=5-5=0 j=2*5-1=9 j=0,1,2,3,4,5,6,7,8  print:* * * * * * * * *
# 6. i=4 -> sp=5-4=1 j=2*4-1=7 j=0,1,2,3,4,5,6      print:  * * * * * * *
# 7. i=3 -> sp=5-3=2 j=2*3-1=5 j=0,1,2,3,4          print:    * * * * *
# 8. i=2 -> sp=5-2=3 j=2*2-1=3 j=0,1,2              print:      * * *
# 9. i=1 -> sp=5-1=4 j=2*1-1=1 j=0                  print:        *
 