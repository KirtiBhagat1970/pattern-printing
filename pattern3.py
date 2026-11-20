#inverted right angled triangle
for i in range(4,0,-1):  #count from 4 to 1 for the rows
    for j in range(i):   #print i rows on current row
        print("*",end=" ")  # print each star on the same line with space
    print()                 #moves to next line
    
# dryrun:
# 1. i=4 -> j runs 0,1,2,3   (4 times) ->print:* * * *
# 1. i=3 -> j runs 0,1,2     (3 times) ->print:* * * 
# 1. i=2 -> j runs 0,1       (2 times) ->print:* * 
# 1. i=1 -> j runs 0,1       (1 times) ->print:* 
