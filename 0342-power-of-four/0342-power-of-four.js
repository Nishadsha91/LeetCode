/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if (n <= 0) {
        return false;
    }    
    let isPowerOfTwo = (n & (n - 1)) === 0;
    if (!isPowerOfTwo) {
        return false;
    }
    let divisibleByThree = (n - 1) % 3 === 0;
    
    if (divisibleByThree) {
        return true;
    } else {
        return false;
    }
};




 
