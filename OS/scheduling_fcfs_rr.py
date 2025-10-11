from collections import deque
def round_robin(processes, time_quantum):
    """
    processes: list of tuples (pid, arrival_time, burst_time)
    time_quantum: int
    """
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # sort by arrival time
    remaining_bt = {pid: bt for pid, at, bt in processes}
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    response_time = {}
    start_time = {}
    gantt_chart = []

    ready_queue = deque()
    current_time = 0
    visited = [False] * n
    completed = 0
    context_switches = 0
    prev_pid = None

    while completed < n:
        # Add processes that have arrived
        for i, (pid, at, bt) in enumerate(processes):
            if at <= current_time and not visited[i]:
                ready_queue.append(pid)
                visited[i] = True

        if ready_queue:
            pid = ready_queue.popleft()
            if pid != prev_pid and prev_pid is not None:
                context_switches += 1
            prev_pid = pid
            if pid not in start_time:
                start_time[pid] = current_time
                response_time[pid] = current_time - next(at for p, at, bt in processes if p == pid)

            exec_time = min(time_quantum, remaining_bt[pid])
            gantt_chart.append((pid, current_time, current_time + exec_time))
            current_time += exec_time
            remaining_bt[pid] -= exec_time

            # Add new arrivals during execution
            for i, (p, at, bt) in enumerate(processes):
                if at <= current_time and not visited[i] and p not in ready_queue:
                    ready_queue.append(p)
                    visited[i] = True

            if remaining_bt[pid] > 0:
                ready_queue.append(pid)
            else:
                completion_time[pid] = current_time
                completed += 1
        else:
            current_time += 1  # CPU idle

    # Calculate TAT & WT
    for pid, at, bt in processes:
        turnaround_time[pid] = completion_time[pid] - at
        waiting_time[pid] = turnaround_time[pid] - bt
    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    avg_rt = sum(response_time.values()) / n

    # Print results
    print("\n--- Round Robin Scheduling ---")
    print(f"Time Quantum: {time_quantum}")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    for pid, at, bt in processes:
        print(f"{pid}\t{at}\t{bt}\t{start_time[pid]}\t{completion_time[pid]}\t"
              f"{turnaround_time[pid]}\t{waiting_time[pid]}\t{response_time[pid]}")
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")
    print(f"Context Switches: {context_switches}")

    # Print Gantt Chart
    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")

def fcfs(processes):
    processes.sort(key=lambda x: x[1])  # sort by arrival time
    n = len(processes)
    current_time = 0
    start_time = {}
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    response_time = {}
    gantt_chart = []

    for pid, at, bt in processes:
        if current_time < at:
            current_time = at
        start_time[pid] = current_time
        response_time[pid] = current_time - at
        gantt_chart.append((pid, current_time, current_time + bt))
        current_time += bt
        completion_time[pid] = current_time
        turnaround_time[pid] = completion_time[pid] - at
        waiting_time[pid] = turnaround_time[pid] - bt
    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    avg_rt = sum(response_time.values()) / n

    # Print results
    print("\n--- First-Come First-Serve (FCFS) ---")
    print("PID\tAT\tBT\tST\tCT\tTAT\tWT\tRT")
    for pid, at, bt in processes:
        print(f"{pid}\t{at}\t{bt}\t{start_time[pid]}\t{completion_time[pid]}\t"
              f"{turnaround_time[pid]}\t{waiting_time[pid]}\t{response_time[pid]}")
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Response Time: {avg_rt:.2f}")
    print("Context Switches: N/A (no preemption)")

    # Print Gantt Chart
    print("\nGantt Chart:")
    for pid, start, end in gantt_chart:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")

# Example usage
process_list = [
    (1, 0, 5),
    (2, 1, 4),
    (3, 2, 2),
    (4, 4, 1)]
fcfs(process_list.copy())
round_robin(process_list.copy(), time_quantum=2)
