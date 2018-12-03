'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

arrival_time=[]

burst_time=[]

ch=int(input("Enter number of processes:"))

i=0

while i<ch:
    
    a=int(input("Enter arrival time:"))
    b=int(input("Enter burst time:"))
    arrival_time.insert(i,a)
    burst_time.insert(i,b)
    i=i+1

print("Process Arrival Time  Burst Time ")
print(arrival_time,burst_time)

for i in range(ch):
	for j in range(0, ch-i-1):
		if arrival_time[j] > arrival_time[j+1] :
		    arrival_time[j], arrival_time[j+1] = arrival_time[j+1], arrival_time[j]
		    
for k in range(ch):
	for l in range(0, ch-k-1):
		if burst_time[l] > burst_time[l+1] :
		    burst_time[l], burst_time[l+1] = burst_time[l+1], burst_time[l]
		    
print(arrival_time)  
print(burst_time)

k=0

print("Gantt Chart")

while k<ch:
    if k==0:
        sum=arrival_time[k]+burst_time[k]      
        print(arrival_time[k],"--------",sum,end=" ")
    
    elif k>0:
 
        sum1=sum+burst_time[k]    
        print("---------",sum1,end=" ")
        sum=sum1
   
    k=k+1
        
    



