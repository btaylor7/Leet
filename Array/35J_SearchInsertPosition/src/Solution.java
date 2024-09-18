class Solution {
    public int searchInsert(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Calculate the mid-point

            if (nums[mid] == target) {
                return mid; // Target found
            } else if (nums[mid] < target) {
                left = mid + 1; // Search in the right half
            } else {
                right = mid - 1; // Search in the left half
            }
        }
        // If the target is not found, left will be the insertion point
        return left;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.searchInsert(new int[] {1,3,5,6}, 5);
        System.out.println(result);
    }

}