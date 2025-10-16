def fcfs_scheduling(processes):
    """
    processes: list of tuples (pid, arrival_time, burst_time)
    """
    processes.sort(key=lambda x: x[1])  # sort by arrival time

    start_time = []
    completion_time = []
    waiting_time = []
    turnaround_time = []

    current_time = 0
    gantt_chart = []

    for pid, arrival, burst in processes:
        if current_time < arrival:
            current_time = arrival  # CPU idle until process arrives

        start_time.append(current_time)
        gantt_chart.append((pid, current_time, current_time + burst))
        current_time += burst
        completion_time.append(current_time)

        tat = completion_time[-1] - arrival
        wt = tat - burst
        turnaround_time.append(tat)
        waiting_time.append(wt)

    avg_wt = sum(waiting_time) / len(processes)
    avg_tat = sum(turnaround_time) / len(processes)

    print("\n--- FCFS Scheduling ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{start_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")

# Example usage
processes = [
    (1, 0, 5),
    (2, 2, 3),
    (3, 4, 1)
]

fcfs_scheduling(processes)
