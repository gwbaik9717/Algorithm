// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    
    let res = nums[0]
    let cnt = 0

    for (const num of nums){
        
        if (cnt === 0){
            res = num
            cnt++
            continue
        }

        if (res === num){
            cnt++
        }else{
            cnt--
        }
    }
    
    return res
};