/*Given a string s, find the length of the longest
substring without repeating characters.*/

import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> charSet = new HashSet<>();

        int maxLength = 0;
        int left = 0;

        for(int right = 0; right<s.length(); right++){
            while(charSet.contains(s.charAt(right))){
                charSet.remove(s.charAt(left));
                left+=1;
            }

            charSet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right-left +1);

        }
        
        return maxLength;
    }
}