function count_occurrences(list, number) {
    count = list.filter((a) => a == number);
    count = count.length;
    return count;
}
function findOdd(numbers) {
    for (let digit of numbers) {
        if (count_occurrences(numbers, digit) % 2 == 1) {
            return digit;
        }
    }
    return 0;
}
// console.log(count([1, 1, 1], 1));

console.log(
    findOdd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]),
    5
);
console.log(findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);
console.log(findOdd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5);
console.log(findOdd([10]), 10);
console.log(findOdd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);
console.log(findOdd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);
