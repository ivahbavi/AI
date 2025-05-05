print("SHORTEST JOB FIRST PREEMPTIVE SCHEDULING")
n = int(input("Enter number of processes: "))
d = {}

for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
    b = int(input("Enter burst time of process " + str(i + 1) + ": "))
    d[key] = [a, b, b]  # [arrival_time, burst_time, remaining_time]

processes = list(d.items())  # Convert dictionary to list of tuples

ET = {}  # Exit time (completion time)
current_time = 0
completed = 0

# Process execution timeline for visualization
timeline = []
current_process = None

while completed < n:
    # Find process with minimum remaining time among arrived processes
    min_remaining = float('inf')
    selected_process = None
    
    for process in processes:
        pid = process[0]
        arrival_time = process[1][0]
        remaining_time = process[1][2]
        
        if arrival_time <= current_time and remaining_time > 0:
            if remaining_time < min_remaining:
                min_remaining = remaining_time
                selected_process = process
    
    # If no process available, move time forward
    if selected_process is None:
        current_time += 1
        continue
    
    # Execute process for 1 time unit
    selected_process[1][2] -= 1  # Decrease remaining time
    current_time += 1
    
    # If process completes
    if selected_process[1][2] == 0:
        completed += 1
        ET[selected_process[0]] = current_time  # Store completion time

# Calculate turnaround time and waiting time for each process
TAT = {}
WT = {}

for process in processes:
    pid = process[0]
    arrival_time = process[1][0]
    burst_time = process[1][1]
    
    TAT[pid] = ET[pid] - arrival_time
    WT[pid] = TAT[pid] - burst_time

# Sort processes by ID for display
processes.sort(key=lambda x: int(x[0][1:]))

# Calculate averages
avg_TAT = sum(TAT.values()) / n
avg_WT = sum(WT.values()) / n

# Output
print("\nProcess | Arrival | Burst | Exit | Turn Around | Wait |")
for process in processes:
    pid = process[0]
    arrival_time = process[1][0]
    burst_time = process[1][1]
    
    print(f"   {pid}    |   {arrival_time}   |   {burst_time}   |   {ET[pid]}   |   {TAT[pid]}   |   {WT[pid]}   |")

print("\nAverage Waiting Time: ", avg_WT)
print("Average Turnaround Time: ", avg_TAT)