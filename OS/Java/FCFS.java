import java.util.*;
public class FCFS{
        public static void main(String[] args)
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the number of process");
            int Process = Integer.parseInt(sc.nextLine());
            System.out.println("Enter the Burst Time");
            int Burst = Integer.parseInt(sc.nextLine());
            System.out.println("Enter Arrival Time");
            int Arrival = Integer.parseInt(sc.nextLine());
            System.out.println("Enter Completion Time");
            int Completion = Integer.parseInt(sc.nextLine());
            int Turnaround = Completion - Arrival;
            int Waiting = Turnaround - Burst;
            System.out.println("The Turn Around Time is "+Turnaround);
            System.out.println("The Waiting time is "+Waiting);
        }
}
