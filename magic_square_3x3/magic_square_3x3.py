import time
startTime = time.time()

for a in range(2,10,2):
    for b in range(1,10,2):
	    for c in range(2,10,2):
		    for d in range(1,10,2):
			    for e in range(5,6): # e==5
				    for f in range(1,10,2):
					    for g in range(2,10,2):
						    for h in range(1,10,2):
							    for i in range(2,10,2):
								    if (a%2==0 and c%2==0 and g%2==0 and i%2==0) and (a!=c and c!=g and g!=i and i!=a) and (b%2!=0 and d%2!=0 and f%2!=0 and h%2!=0) and (b!=d and d!=f and f!=h and h!=b) and (a+b+c == e+f+d == a+b+c == g+h+i == a+d+g == b+e+h == a+d+g == c+f+i==a+e+i==c+e+g==15): 
									    print(a,b,c,d,e,f,g,h,i)
print(time.time() - startTime)