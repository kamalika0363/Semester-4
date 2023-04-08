import java.util.*;

public class FIFOPageReplacement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of frames: ");
        int numberOfFrames = scanner.nextInt();

        int[] frames = new int[numberOfFrames];
        Arrays.fill(frames, -1); // Fill frames with -1 to indicate empty

        int pageFaults = 0;
        int currentIndex = 0;

        System.out.print("Enter the number of pages: ");
        int numberOfPages = scanner.nextInt();

        System.out.print("Enter the page numbers: ");
        for (int i = 0; i < numberOfPages; i++) {
            int pageNumber = scanner.nextInt();

            boolean pageHit = false;
            for (int j = 0; j < numberOfFrames; j++) {
                if (frames[j] == pageNumber) {
                    pageHit = true;
                    break;
                }
            }

            if (!pageHit) {
                frames[currentIndex] = pageNumber;
                currentIndex = (currentIndex + 1) % numberOfFrames;
                pageFaults++;
            }

            System.out.print("Page " + pageNumber + " -> ");
            for (int j = 0; j < numberOfFrames; j++) {
                if (frames[j] == -1) {
                    System.out.print("empty ");
                } else {
                    System.out.print(frames[j] + " ");
                }
            }
            System.out.println();
        }

        System.out.println("Number of page faults: " + pageFaults);
    }
}
