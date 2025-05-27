import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Solution {

    public boolean areOccurrencesEqual(String s) {

        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {

            char currentChar = s.charAt(i);

            if (map.containsKey(currentChar)) {

                map.put(currentChar, map.get(currentChar) + 1);
            } else {

                map.put(currentChar, 1);
            }
        }

        Set<Integer> valueSet = new java.util.HashSet<>(map.values());

        if (valueSet.size() == 1) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {

        Solution test = new Solution();
        boolean result = test.areOccurrencesEqual("abcabc");
        System.out.println(result);

        boolean result2 = test.areOccurrencesEqual("abbcde");
        System.out.println(result2);

    }
}