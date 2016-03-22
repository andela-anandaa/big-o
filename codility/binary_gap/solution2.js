// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    // write your code in JavaScript (Node.js 4.0.0)
    var re = /[0]+/g;
    
    N = Number(N, 10).toString(2);
    var matches = N.match(re);
    if(matches){
	// return matches.sort().slice(-1)[0].length
        return longest_string(matches);
    }
    return 0;
}

function longest_string(array) {
    var max_count = 0;
    array.forEach(function(element){
        if(element.length > max_count) {
            max_count = element.length;
        }
    });
    return max_count;
}
