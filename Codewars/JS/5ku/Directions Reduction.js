function dirReduc(arr) {
    // not working
    // misread the question, can not fully reduce directions down, reductions can only be applied to previous direction
    var converted = [0, 0];
    var total = [0, 0];
    for (i of arr) {
        converted = convert_text_coords(i);
        total[0] += converted[0];
        total[1] += converted[1];
        console.log(i, converted, total);
    }
    // console.log(total);
    return convert_coords_test(total);
}

function convert_text_coords(item) {
    switch (item) {
        case 'NORTH':
            return [0, 1];
        case 'EAST':
            return [1, 0];
        case 'SOUTH':
            return [0, -1];
        case 'WEST':
            return [-1, 0];
    }
}

function convert_coords_test(arr) {
    var result = [],
        loop = Math.abs(arr[0]);
    if (arr[0] > 0) {
        while (loop > 0) {
            result.push('EAST');
            loop--;
        }
    } else if (arr[0] < 0) {
        while (loop > 0) {
            result.push('WEST');
            loop--;
        }
    }
    loop = Math.abs(arr[1]);
    if (arr[1] > 0) {
        while (loop > 0) {
            result.push('NORTH');
            loop--;
        }
    } else if (arr[1] < 0) {
        while (loop > 0) {
            result.push('SOUTH');
            loop--;
        }
    }
    return result;
}

// console.log(dirReduc(['NORTH', 'WEST', 'WEST', 'NORTH', 'WEST']));
console.log(
    dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']),
    ['WEST']
);
console.log(dirReduc(['NORTH', 'WEST', 'SOUTH', 'EAST']), [
    'NORTH',
    'WEST',
    'SOUTH',
    'EAST',
]);
console.log(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'EAST', 'WEST']), []);
