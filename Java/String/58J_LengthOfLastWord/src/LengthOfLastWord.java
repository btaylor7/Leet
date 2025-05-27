class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        // Trim any trailing spaces
        s = s.trim();
        // If the string is empty after trimming, return 0
        if (s.isEmpty()) {
            return 0;
        }
        // Split the string into words based on spaces
        String[] words = s.split(" ");
        // Return the length of the last word
        return words[words.length - 1].length();// -1 because of 0 index.
    }
    public static void main(String[]args){
        LengthOfLastWord test = new LengthOfLastWord();
        int print = test.lengthOfLastWord("Hello World");
        System.out.println(print);
    }
}


