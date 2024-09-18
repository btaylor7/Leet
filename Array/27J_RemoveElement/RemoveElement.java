package RemoveElement#27;
class Solution {
    public int removeElement(int[] nums, int val){
        int index = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
    
}
//Note this does not actually remove the element from the list.
//It just moves the elements that are not equal to val to the front of the list, and returns a count.

public class RemoveElement {
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] nums = {3, 2, 2, 3};
        int val = 3;
        int result = solution.removeElement(nums, val);
        System.out.println(result);
    }
}