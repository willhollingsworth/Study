function findOutlier(integers) {
    let sample = integers
        .slice(0, 3)
        .map((a) => Math.abs(a))
        .map((a) => a % 2)
        .reduce((a, b) => a + b);
    if (sample > 1) {
        return integers.filter((a) => a % 2 == 0)[0];
    } else {
        return integers.filter((a) => a % 2)[0];
    }
}

console.log(findOutlier([0, 1, 2]), 1);
console.log(findOutlier([1, 2, 3]), 2);
console.log(findOutlier([2, 6, 8, 10, 3]), 3);
console.log(findOutlier([0, 0, 3, 0, 0]), 3);
console.log(findOutlier([1, 1, 0, 1, 1]), 0);
// console.log(
//     findOutlier([
//         -16505242, 53038198, 65376258, -27199196, -152708208, -117809892,
//         161439554, 61725990, 176933342, -116776280, 180187546, -152991754,
//         174235240,
//     ]),
//     0
// );
