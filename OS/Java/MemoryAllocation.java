import java.util.Scanner;

public class MemoryAllocation {
    private static final int MAX_SIZE = 1000; // maximum size of memory block
    private static int[] memory = new int[MAX_SIZE]; // array to represent memory block
    private static int[] allocatedSizes = new int[MAX_SIZE]; // array to store allocated block sizes
    private static int numAllocatedBlocks = 0; // number of allocated memory blocks
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("Memory Allocation Menu:");
            System.out.println("1. First Fit");
            System.out.println("2. Best Fit");
            System.out.println("3. Worst Fit");
            System.out.println("4. Display Memory Usage");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    firstFit();
                    break;
                case 2:
                    bestFit();
                    break;
                case 3:
                    worstFit();
                    break;
                case 4:
                    displayMemoryUsage();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 5);
    }

    private static void firstFit() {
        System.out.print("Enter size of memory block to allocate: ");
        int size = scanner.nextInt();
        int startIndex = -1;
        int currentBlockSize = 0;
        for (int i = 0; i < MAX_SIZE; i++) {
            if (memory[i] == 0) {
                currentBlockSize++;
                if (currentBlockSize == size) {
                    startIndex = i - size + 1;
                    break;
                }
            } else {
                currentBlockSize = 0;
            }
        }
        if (startIndex == -1) {
            System.out.println("Memory block cannot be allocated.");
        } else {
            allocateMemory(startIndex, size);
            System.out.println("Memory block allocated starting at index " + startIndex);
        }
    }

    private static void bestFit() {
        System.out.print("Enter size of memory block to allocate: ");
        int size = scanner.nextInt();
        int bestFitIndex = -1;
        int bestFitSize = Integer.MAX_VALUE;
        int currentBlockSize = 0;
        for (int i = 0; i < MAX_SIZE; i++) {
            if (memory[i] == 0) {
                currentBlockSize++;
                if (currentBlockSize == size) {
                    bestFitIndex = i - size + 1;
                    bestFitSize = size;
                    break;
                }
            } else {
                currentBlockSize = 0;
            }
            if (currentBlockSize > size && currentBlockSize < bestFitSize) {
                bestFitIndex = i - currentBlockSize + 1;
                bestFitSize = currentBlockSize;
            }
        }
        if (bestFitIndex == -1) {
            System.out.println("Memory block cannot be allocated.");
        } else {
            allocateMemory(bestFitIndex, size);
            System.out.println("Memory block allocated starting at index " + bestFitIndex);
        }
    }

    private static void worstFit() {
        System.out.print("Enter size of memory block to allocate: ");
        int size = scanner.nextInt();
        int worstFitIndex = -1;
        int worstFitSize = -1;
    int currentBlockSize = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        if (memory[i] == 0) {
            currentBlockSize++;
            if (currentBlockSize == size) {
                worstFitIndex = i - size + 1;
                worstFitSize = size;
                break;
            }
        } else {
            currentBlockSize = 0;
        }
        if (currentBlockSize > size && currentBlockSize > worstFitSize) {
            worstFitIndex = i - currentBlockSize + 1;
            worstFitSize = currentBlockSize;
        }
    }
    if (worstFitIndex == -1) {
        System.out.println("Memory block cannot be allocated.");
    } else {
        allocateMemory(worstFitIndex, size);
        System.out.println("Memory block allocated starting at index " + worstFitIndex);
    }
}

private static void displayMemoryUsage() {
    int totalFree = 0;
    int totalAllocated = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        if (memory[i] == 0) {
            totalFree++;
        } else {
            totalAllocated++;
        }
    }
    System.out.println("Memory Usage:");
    System.out.println("Total memory: " + MAX_SIZE);
    System.out.println("Allocated memory: " + totalAllocated);
    System.out.println("Free memory: " + totalFree);
    System.out.println("Number of allocated memory blocks: " + numAllocatedBlocks);
    System.out.println("Allocated memory block sizes:");
    for (int i = 0; i < MAX_SIZE; i++) {
        if (allocatedSizes[i] != 0) {
            System.out.println("Block starting at index " + i + " has size " + allocatedSizes[i]);
        }
    }
}

private static void allocateMemory(int startIndex, int size) {
    for (int i = startIndex; i < startIndex + size; i++) {
        memory[i] = 1;
    }
    allocatedSizes[startIndex] = size;
    numAllocatedBlocks++;
}
}


