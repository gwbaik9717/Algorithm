// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    let prev = nums[0]
    let prevFull = false

    let k = 1

    for (let i=1; i<nums.length; i++){
        if (nums[i] === prev){
            if (!prevFull){
                nums[k] = nums[i]
                k++
                prevFull = true
            }
        }else{
            nums[k] = nums[i]
            k++
            prevFull = false
            prev = nums[i]
        }
    }

    return k
};