package ValidParentheses;
import java.util.Stack;

class Solution{
    public boolean isValid(String s){
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if( c == '(' || c == '[' || c == '{'){
                stack.push(c);

            } else if (c == ')' && !stack.isEmpty() && stack.peek() == '('){
                stack.pop();
            } else if (c == ']' && !stack.isEmpty() && stack.peek() == '['){
                stack.pop();
            } else if (c == '}' && !stack.isEmpty() && stack.peek() == '{'){
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }
}

public class ValidParentheses{
    public static void main(String[] args){
        Solution solution = new Solution();
        String s = "()";
        boolean result = solution.isValid(s);
        System.out.println(result);
    }
}