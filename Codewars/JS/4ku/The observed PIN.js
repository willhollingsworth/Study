// wip

function getPINs(observed) {
    let output = [],
        length = observed.length;
    for (let x of observed.split('')) {
    }
    if (length == 1) {
        output = get_adjacent_n(observed);
        output = format_n_list(output, observed);
        return output;
    } else {
        // return all combinations
    }
}

function format_n_list(in_list, initial) {
    in_list.push(initial);
    in_list.sort();
    if (in_list.includes(0)) {
        in_list = in_list.filter((n) => n != 0);
        in_list.push(0);
    }
    in_list = in_list.map((n) => n.toString());
    return in_list;
}
function get_adjacent_n(num) {
    if (num == 1) return [2, 4];
    else if (num == 2) return [1, 3, 5];
    else if (num == 3) return [2, 6];
    else if (num == 4) return [1, 5, 7];
    else if (num == 5) return [2, 4, 6, 8];
    else if (num == 6) return [3, 5, 9];
    else if (num == 7) return [4, 8];
    else if (num == 8) return [5, 7, 9, 0];
    else if (num == 9) return [5, 7, 9, 0];
    else if (num == 0) return [8];
}

console.log(getPINs('8'), ['5', '7', '8', '9', '0']);
console.log(getPINs('11'), [
    '11',
    '22',
    '44',
    '12',
    '21',
    '14',
    '41',
    '24',
    '42',
]);
// console.log(getPINs(369), [
//     '339',
//     '366',
//     '399',
//     '658',
//     '636',
//     '258',
//     '268',
//     '669',
//     '668',
//     '266',
//     '369',
//     '398',
//     '256',
//     '296',
//     '259',
//     '368',
//     '638',
//     '396',
//     '238',
//     '356',
//     '659',
//     '639',
//     '666',
//     '359',
//     '336',
//     '299',
//     '338',
//     '696',
//     '269',
//     '358',
//     '656',
//     '698',
//     '699',
//     '298',
//     '236',
//     '239',
// ]);
