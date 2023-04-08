import java.util.*;

public class lru {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of page frames: ");
        int numFrames = sc.nextInt();
        System.out.print("Enter the sequence of page requests: ");
        String sequence = sc.next();
        int pageFaults = 0;
        ArrayList<Integer> frames = new ArrayList<>();
        for (int i = 0; i < sequence.length(); i++) {
            int pageNumber = Character.getNumericValue(sequence.charAt(i));
            if (!frames.contains(pageNumber)) {
                if (frames.size() < numFrames) {
                    frames.add(pageNumber);
                } else {
                    int indexToRemove = 0;
                    int longestTime = -1;
                    for (int j = 0; j < frames.size(); j++) {
                        int pageFrame = frames.get(j);
                        int lastReference = sequence.lastIndexOf(Integer.toString(pageFrame), i - 1);
                        if (lastReference == -1) {
                            indexToRemove = j;
                            break;
                        }
                        if (lastReference > longestTime) {
                            longestTime = lastReference;
                            indexToRemove = j;
                        }
                    }
                    frames.set(indexToRemove, pageNumber);
                }
                pageFaults++;
            }
        }
        System.out.println("Page faults: " + pageFaults);
    }
}
