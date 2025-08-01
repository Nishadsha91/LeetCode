/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let sl = s.toLowerCase();
    let sum=0;
    for(let i=0; i < sl.length-1 ; i++){
        sum += Math.abs(sl.charCodeAt(i) - sl.charCodeAt(i+1))
    }
    return sum
};