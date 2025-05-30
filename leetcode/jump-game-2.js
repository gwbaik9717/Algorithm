// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {

    let prevValue = 0
    let maxValue = 0
    let answer = 0

    for (let i=0; i<nums.length; i++){
        if (i > prevValue){
            answer++
            prevValue = maxValue
        }

        maxValue = Math.max(maxValue, i + nums[i])
    }

    return answer
};