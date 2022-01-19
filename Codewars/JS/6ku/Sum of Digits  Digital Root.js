function digital_root(n) {
    while (n.toString().length > 1) {
        n = sum_digits(n);
    }
    return n;

    function sum_digits(digits) {
        return n
            .toString()
            .split('')
            .reduce((a, b) => +a + +b);
    }
}

console.log(digital_root(16), 7);
console.log(digital_root(456), 6);
