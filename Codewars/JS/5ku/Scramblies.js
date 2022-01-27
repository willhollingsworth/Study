function scramble(str1, str2) {
    for (let x of str2) {
        if (count(str2, x) > count(str1, x)) {
            return false;
        }
    }
    return true;
}

function count(arr, char) {
    let reg = new RegExp(char, 'g'),
        count = (arr.match(reg) || []).length;
    return count;
}

console.log(scramble('rkqodlw', 'world'), true);
console.log(scramble('rkqodlw', '1world'), false);
console.log(scramble('cedewaraaossoqqyt', 'codewars'), true);
console.log(scramble('katas', 'steak'), false);
console.log(scramble('scriptjava', 'javascript'), true);
console.log(scramble('scriptingjava', 'javascript'), true);
console.log(scramble('scriptsjava', 'javascripts'), true);
console.log(scramble('jscripts', 'javascript'), false);
console.log(scramble('aabbcamaomsccdd', 'commas'), true);
