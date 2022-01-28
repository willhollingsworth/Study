function score(dice) {
    const potential = [1, 2, 3, 4, 5, 6],
        triples = { 1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600 };
    let counts = {},
        result = 0;

    potential.forEach((i) => (counts[i] = count(dice, i)));
    potential.forEach((i) => {
        if (counts[i] >= 3) {
            result += triples[i];
            [1, 2, 3].forEach((x) => dice.splice(dice.indexOf(i), 1));
        }
    });
    dice.forEach((i) => {
        if (i == 1) result += 100;
        if (i == 5) result += 50;
    });
    return result;
}

function count(arr, char) {
    return arr.filter((i) => i == char).length;
}

// console.log(score([1, 1, 1, 6, 2]));
// console.log(score([2, 3, 4, 6, 2]), 'Should be 0 :-(');
// console.log(score([4, 4, 4, 3, 3]), 'Should be 400');
console.log(score([2, 4, 4, 5, 4]), 'Should be 450');
