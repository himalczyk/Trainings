fibonacci = 0
x = 0

for x in range (100):
    if(x==0):
        n=0
    if(x==1):
        n=1
    if(x>1):
        n=(x-1)+(x-2)
        fibonacci=n
        print(fibonacci)
    x=x+1

