function dirReduc(arr) {
    let previous_length = 1,
        current_length = 0,
        result = arr;
    while (current_length != previous_length) {
        // keep reducing until it can't shrink anymore
        previous_length = result.length;
        result = reduce_array(result);
        current_length = result.length;
    }
    return result;
}

function reduce_array(arr) {
    let result = [];
    for (x in arr) {
        var current = arr[x],
            previous = arr[x - 1];
        if (result.length < 1 || previous != result.slice(-1)) {
            result.push(current);
            continue;
        }
        if (
            (current == 'NORTH' && previous == 'SOUTH') ||
            (current == 'SOUTH' && previous == 'NORTH') ||
            (current == 'EAST' && previous == 'WEST') ||
            (current == 'WEST' && previous == 'EAST')
        ) {
            result.pop();
        } else {
            result.push(current);
        }
    }
    return result;
}

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
console.log(
    dirReduc([
        'SOUTH',
        'NORTH',
        'WEST',
        'EAST',
        'NORTH',
        'SOUTH',
        'NORTH',
        'EAST',
        'WEST',
        'EAST',
        'NORTH',
        'SOUTH',
        'EAST',
        'WEST',
    ]),
    ['NORTH', 'EAST']
);
console.log(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'EAST', 'WEST']), []);
