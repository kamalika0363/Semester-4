import java.util.*;

public class longest_sequence {
    public static String findLCS(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        // Create a table to store the lengths of LCSs of substrings of s1 and s2
        int[][] table = new int[m + 1][n + 1];
        // Fill the table with LCS lengths
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    table[i][j] = table[i - 1][j - 1] + 1;
                } else {
                    table[i][j] = Math.max(table[i - 1][j], table[i][j - 1]);
                }
            }
        }
        // Traverse the table to construct the LCS
        StringBuilder lcs = new StringBuilder();
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                lcs.append(s1.charAt(i - 1));
                i--;
                j--;
            } else if (table[i - 1][j] > table[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }
        // Reverse the LCS to get the correct order of characters
        return lcs.reverse().toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String 1");
        String s1 = sc.next();
        System.out.println("Enter String 2");
        String s2 = sc.next();
        String lcs = findLCS(s1, s2);
        System.out.println("Longest Common Subsequence: " + lcs);
    }
}
