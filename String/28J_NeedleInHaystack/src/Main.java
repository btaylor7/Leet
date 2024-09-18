public class Main {
    public static void main(String[] args) {
        String haystack = "sadbutsad";
        String needle = "sad";
        int result = strStr(haystack, needle);
        System.out.println(result); // Output: 0
    }

    public static int strStr(String haystack, String needle) {
        // Edge case: if needle is an empty string, return 0
        if (needle.isEmpty()) {
            return 0;
        }

        // Edge case: if needle is longer than haystack, return -1
        if (needle.length() > haystack.length()) {
            return -1;
        }

        // Loop through the haystack up to the point where needle could fit
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            // Check if the substring of haystack starting at i matches needle
            if (haystack.startsWith(needle, i)) {
                return i; // Return the starting index of the first occurrence
            }
        }

        // If no match is found, return -1
        return -1;
    }
}
