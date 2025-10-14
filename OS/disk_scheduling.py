import random
class DiskScheduling:
    def __init__(self, requests, head, disk_size=200):
        self.requests = requests[:]  # make a copy to preserve the original list
        self.head = head
        self.disk_size = disk_size

    def fcfs(self):
        distance = 0
        head = self.head
        order = []
        for req in self.requests:
            distance += abs(head - req)
            order.append(req)
            head = req
        return order, distance

    def sstf(self):
        distance = 0
        head = self.head
        requests = self.requests[:]
        order = []
        while requests:
            closest = min(requests, key=lambda x: abs(x - head))
            distance += abs(head - closest)
            order.append(closest)
            head = closest
            requests.remove(closest)
        return order, distance

    def cscan(self):
        distance = 0
        head = self.head
        requests = sorted(self.requests)
        order = []
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]

        # Go rightwards till the end
        for r in right:
            distance += abs(head - r)
            order.append(r)
            head = r

        # Jump to the beginning of the disk and service left
        if left:
            distance += abs(self.disk_size - 1 - head)  # Go to end
            distance += self.disk_size - 1  # Jump to beginning
            head = 0

            for r in left:
                distance += abs(head - r)
                order.append(r)
                head = r
        return order, distance

    def clook(self):
        distance = 0
        head = self.head
        requests = sorted(self.requests)
        order = []
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]

        # Service right side
        for r in right:
            distance += abs(head - r)
            order.append(r)
            head = r

        # Jump to the smallest request on the left side
        if left:
            distance += abs(head - left[0])
            head = left[0]

            # Service left side
            for r in left:
                distance += abs(head - r)
                order.append(r)
                head = r
        return order, distance
    def rss(self):
        distance = 0
        head = self.head
        requests = self.requests[:]
        order = []
        random.shuffle(requests)

        for r in requests:
            distance += abs(head - r)
            order.append(r)
            head = r
        return order, distance

# Example Usage
if __name__ == "__main__":
    requests = [82, 170, 43, 140, 24, 16, 190]
    head = 50
    disk_size = 200
    algo = DiskScheduling(requests, head, disk_size)

    fcfs_order, fcfs_distance = algo.fcfs()
    print(f"FCFS order: {fcfs_order}")
    print(f"FCFS total distance: {fcfs_distance}")

    sstf_order, sstf_distance = algo.sstf()
    print(f"SSTF order: {sstf_order}")
    print(f"SSTF total distance: {sstf_distance}")

    clook_order, clook_distance = algo.clook()
    print(f"C-LOOK order: {clook_order}")
    print(f"C-LOOK total distance: {clook_distance}")

    cscan_order, cscan_distance = algo.cscan()
    print(f"C-SCAN order: {cscan_order}")
    print(f"C-SCAN total distance: {cscan_distance}")

    rss_order, rss_distance = algo.rss()
    print(f"RSS order: {rss_order}")
    print(f"RSS total distance: {rss_distance}")

