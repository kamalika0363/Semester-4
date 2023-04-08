print("Welcome to FCFS & SJF Scheduling Algorithm")
print("===========================================")
n = int(input("Enter the number of processes:"))
print("Enter the Process ID and burst time of each process")
bt = []
pid = []
for i in range(n):
    pid.append(int(input("Process id:")))
    bt.append(int(input("Burst Time:")))
print("===========================================")
print("FCFS Scheduling Algorithm")
print("===========================================")
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
wt = []
tat = []
wt.append(0)
tat.append(bt[0])
for i in range(1, n):
    wt.append(wt[i-1]+bt[i-1])
    tat.append(wt[i]+bt[i])
for i in range(n):
    print(pid[i], "\t\t\t", bt[i], "\t\t\t", wt[i], "\t\t\t", tat[i])
print("Avg. Waiting Time:{}ms".format(sum(wt)/n))
print("Avg. Turnaround Time:{}ms".format(sum(tat)/n))
print("===========================================")
print("===========================================")
print("Shortest Job First Scheduling Algorithm")
print("===========================================")
for i in range(n):
    for j in range(i+1, n):
        if bt[i] > bt[j]:
            temp = bt[i]
            bt[i] = bt[j]
            bt[j] = temp
            temp = pid[i]
            pid[i] = pid[j]
            pid[j] = temp
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
wt = []
tat = []
wt.append(0)
tat.append(bt[0])
for i in range(1, n):
    wt.append(wt[i-1]+bt[i-1])
    tat.append(wt[i]+bt[i])
for i in range(n):
    print(pid[i], "\t\t\t", bt[i], "\t\t\t", wt[i], "\t\t\t", tat[i])
print("Avg. Waiting Time:{}ms".format(sum(wt)/n))
print("Avg. Turnaround Time:{}ms".format(sum(tat)/n))
print("===========================================")
