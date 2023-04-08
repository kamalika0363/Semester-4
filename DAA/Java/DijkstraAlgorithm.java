import java.util.*; //imports scanner package

public class DijkstraAlgorithm {
    public static void main(String[] args) { // Main function to be called
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of vertices in the graph: ");
        int V = sc.nextInt();
        int[][] graph = new int[V][V]; // declaring graph in the form of array
        System.out.println("Enter the adjacency matrix of the graph:");
        for (int i = 0; i < V; i++) { // taking 2D matrix as input
            for (int j = 0; j < V; j++) {
                graph[i][j] = sc.nextInt();
            }
        }
        System.out.print("Enter the source vertex: ");
        int source = sc.nextInt();

        dijkstra(graph, source);
    }

    public static void dijkstra(int[][] graph, int source) {
        int V = graph.length;
        int[] dist = new int[V];
        boolean[] visited = new boolean[V];
        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
            visited[i] = false;
        }
        dist[source] = 0;
        for (int i = 0; i < V - 1; i++) { // this loop keeps on updating the shortest path
            int u = findMinDist(dist, visited);
            visited[u] = true;
            for (int v = 0; v < V; v++) {
                if (!visited[v] && graph[u][v] != 0 && dist[u] != Integer.MAX_VALUE &&
                        dist[u] + graph[u][v] < dist[v]) {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }
        printSolution(dist);
    }

    public static int findMinDist(int[] dist, boolean[] visited) {
        int minDist = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < dist.length; i++) {
            if (!visited[i] && dist[i] < minDist) {
                minDist = dist[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    public static void printSolution(int[] dist) {
        System.out.println("Vertex \t Distance from Source");
        for (int i = 0; i < dist.length; i++) {
            System.out.println(i + "\t" + dist[i]);
        }
    }
}
