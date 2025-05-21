// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    let prev = nums[0]
    let k = 1

    for (let i = 1; i < nums.length; i++){
        if (nums[i] > prev){
            nums[k] = nums[i]
            prev = nums[i]
            k++
        }
    }

    return k
};