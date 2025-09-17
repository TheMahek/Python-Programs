from collections import deque   #import deque for efficient queue operation (used in BFS)

class Graph:
    def __init__(self,num_vertices,directed=False):
        # Initialize the graph with number of vertices and whether it's directed
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_matrix =[]  #This will be our adjacency matrix
        
        # Create a 2D matrix (list of lists) filled with 0s initially
        for i in range(num_vertices):
            row = [0] * num_vertices  #row of zeros
            self.adj_matrix.append(row)
            
    
    def add_edge(self,s,d):
        #Add an edge from s to d
        if s < 0 or s >= self.num_vertices or d < 0 or d >= self.num_vertices:
            print(f"Error: Vertex {s} or {d} is out of graph bounds.")
            return
        
        self.adj_matrix[s][d] = 1 #Set edge from s to d
        if not self.directed:
            self.adj_matrix[d][s] = 1  # If undirected, also set edge from d to s
            
    def print_matrix(self):
        # Print the adjacency matrix row by row 
        print("Adjacency Matrix: ")
        for row in self.adj_matrix:
            print(row)
            
    def bfs(self, start):
        #Breadth-FIRST Search using queue
        if start <0 or start >= self.num_vertices:
            print(f"Error: Start vertex {start} is out of graph bounds.")  
            return
        
        visited = [False] * self.num_vertices # Track visited vertices
        queue = deque() # Create a queue for BFS
        
        visited[start] = True # Marks starting vertex as visited
        queue.append(start)   # ✅ Enqueue starting vertex
        
        print("BFS traversal starting from vertex", start, ":", end=" ")
        while queue:
            vertex = queue.popleft()  #Dequeue a vertex
            print(vertex, end=" ")    #Visited the vertex
            
            #Visit all neighbours of the current vertex
            for neighbour in range(self.num_vertices ):
                #if there's an edge and neighbour not visited
                if self.adj_matrix[vertex][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True   # Mark neighbour visited
                    queue.append(neighbour)    # Enqueue neighbour
        print()

g = Graph(5, directed=False)

# Add some edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Print adjacency matrix
g.print_matrix()

# Run BFS from vertex 0
g.bfs(0)
