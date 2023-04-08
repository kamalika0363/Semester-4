import java.util.*;
class Edge implements Comparable<Edge> {
    int src, dest, weight;

    public int compareTo(Edge other) {
        return this.weight - other.weight;
    }
}
class Kruskal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of vertices: ");
        int V = sc.nextInt();
        System.out.print("Enter the number of edges: ");
        int E = sc.nextInt();
        Edge[] edges = new Edge[E];
        for (int i = 0; i < E; i++) {
            System.out.printf("Enter the details for edge %d (source, destination, weight): ", i+1);
            int src = sc.nextInt();
            int dest = sc.nextInt();
            int weight = sc.nextInt();
            edges[i] = new Edge();
            edges[i].src = src;
            edges[i].dest = dest;
            edges[i].weight = weight;
        }

        Arrays.sort(edges);
        int[] parent = new int[V];
        for (int i = 0; i < V; i++) {
            parent[i] = i;
        }
        int[] rank = new int[V];
        ArrayList<Edge> mst = new ArrayList<Edge>();
        for (int i = 0; i < E; i++) {
            Edge e = edges[i];
            int srcParent = find(parent, e.src);
            int destParent = find(parent, e.dest);
            if (srcParent != destParent) {
                mst.add(e);
                union(parent, rank, srcParent, destParent);
            }
        }
        System.out.println("Minimum Spanning Tree:");
        for (Edge e : mst) {
            System.out.printf("(%d, %d) -> %d\n", e.src, e.dest, e.weight);
        }
        sc.close();
    }
    static int find(int[] parent, int i) {
        if (parent[i] != i) {
            parent[i] = find(parent, parent[i]);
        }
        return parent[i];
    }
    static void union(int[] parent, int[] rank, int x, int y) {
        int xRoot = find(parent, x);
        int yRoot = find(parent, y);

        if (xRoot == yRoot) {
            return;
        }
        if (rank[xRoot] < rank[yRoot]) {
            parent[xRoot] = yRoot;
        } else if (rank[xRoot] > rank[yRoot]) {
            parent[yRoot] = xRoot;
        } else {
            parent[yRoot] = xRoot;
            rank[xRoot]++;
        }
    }
}
