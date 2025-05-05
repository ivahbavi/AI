print("FIRST COME FIRST SERVE SCHEDULING")
n = int(input("Enter number of processes: "))
d = {}

for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
    b = int(input("Enter burst time of process " + str(i + 1) + ": "))
    d[key] = [a, b]

# Sort processes by arrival time
d = sorted(d.items(), key=lambda item: item[1][0])

ET = []  # Exit time
current_time = 0  # CPU clock time

for i in range(len(d)):
    if current_time < d[i][1][0]:  # If CPU is idle
        current_time = d[i][1][0]
    
    current_time += d[i][1][1]  # Process execution
    ET.append(current_time)  # Store completion time

# Turnaround Time (TAT) = Exit Time - Arrival Time
TAT = [ET[i] - d[i][1][0] for i in range(len(d))]

# Waiting Time (WT) = Turnaround Time - Burst Time
WT = [TAT[i] - d[i][1][1] for i in range(len(d))]

# Average calculations
avg_WT = sum(WT) / n
avg_TAT = sum(TAT) / n

# Output
print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(n):
    print(f"   {d[i][0]}    |   {d[i][1][0]}   |   {d[i][1][1]}   |   {ET[i]}   |   {TAT[i]}   |   {WT[i]}   |  ")

print("Average Waiting Time: ", avg_WT)
print("Average Turnaround Time: ", avg_TAT)

