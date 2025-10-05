/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let dup = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (dup.has(nums[i])) {  
            return nums[i];     
        }
        dup.add(nums[i]);        
    }
};
