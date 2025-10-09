def non_preemptive_priority(processes):
    """
    processes: list of tuples (pid, arrival_time, burst_time, priority)
    Lower priority value means higher priority.
    """
    n = len(processes)
    
    # Sort by arrival time first, then priority
    processes.sort(key=lambda x: (x[1], x[3])) 
    completed = 0
    current_time = 0
    start_time = {}
    completion_time = {}
    waiting_time = {}
    turnaround_time = {}
    gantt_chart = []
    ready_queue = []
    visited = [False] * n
    
    while completed < n:
        # Add processes that have arrived by current_time
        for i in range(n):
            if processes[i][1] <= current_time and not visited[i]:
                ready_queue.append(processes[i])
                visited[i] = True

        if ready_queue:
            # Pick highest priority (lowest priority number)
            ready_queue.sort(key=lambda x: x[3])  # Sort by priority
            pid, at, bt, pr = ready_queue.pop(0)
            
            if current_time < at:
                # If no process is available to execute, CPU idles
                current_time = at
                start_time[pid] = current_time
                gantt_chart.append((pid, current_time, current_time + bt))
                current_time += bt
            else:
                # Process execution starts immediately
                start_time[pid] = current_time
                gantt_chart.append((pid, current_time, current_time + bt))
                current_time += bt

            completion_time[pid] = current_time
            turnaround_time[pid] = completion_time[pid] - at
            waiting_time[pid] = turnaround_time[pid] - bt
            completed += 1
        else:
            # CPU is idle if no processes are ready to execute
            current_time += 1
    
    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    
    # Print Results
    print("\n--- Non-preemptive Priority Scheduling ---")
    print("PID\tAT\tBT\tPriority\tST\tCT\tTAT\tWT")
    for pid, at, bt, pr in processes:
        print(f"{pid}\t{at}\t{bt}\t{pr}\t\t{start_time[pid]}\t{completion_time[pid]}\t{turnaround_time[pid]}\t{waiting_time[pid]}")
    
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    
    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")

# Example usage
processes_priority = [
    (1, 0, 5, 2),  # (PID, Arrival Time, Burst Time, Priority)
    (2, 1, 3, 1),
    (3, 2, 8, 3),
    (4, 3, 6, 2)
]
non_preemptive_priority(processes_priority)

