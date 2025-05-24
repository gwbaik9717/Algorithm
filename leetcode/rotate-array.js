// TC: O(n)
// SC: O(1)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {

    const rotate = (start) => {
        let current = start
        let prevValue = nums[start]

        do {
            const newIndex = (current + k) % nums.length
            const temp = nums[newIndex]

            nums[newIndex] = prevValue
            prevValue = temp
            current = newIndex
        } while (current !== start)
    }

    const gcd = (a, b) => {
        while (b != 0) {
            let r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
    
    const val = gcd(nums.length, k)

    for (let i = 0; i < val; i++) {
        rotate(i)
    }
};