import java.util.*;
public class SJF {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter number of processes: ");
    int numOfProcesses = sc.nextInt();
    int[] burstTime = new int[numOfProcesses];
    int[] waitingTime = new int[numOfProcesses];
    int[] turnaroundTime = new int[numOfProcesses];
    for (int i = 0; i < numOfProcesses; i++) {
      System.out.print("Enter burst time for process " + (i + 1) + ": ");
      burstTime[i] = sc.nextInt();
    }
    waitingTime[0] = 0;
    for (int i = 1; i < numOfProcesses; i++) {
      waitingTime[i] = 0;
      for (int j = 0; j < i; j++) {
        waitingTime[i] += burstTime[j];
      } }
    System.out.println("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time");
    for (int i = 0; i < numOfProcesses; i++) {
    turnaroundTime[i] = burstTime[i] + waitingTime[i];
      System.out.println((i + 1) + "\t\t" + burstTime[i] + "\t\t" + waitingTime[i] + "\t\t" + turnaroundTime[i]);
    }
    sc.close();
  }}
