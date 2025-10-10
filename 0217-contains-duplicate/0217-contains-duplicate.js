/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

    let dup = new Set(nums)
    if(nums.length != dup.size){
        return true
    }else{
        return false
    }
    
};