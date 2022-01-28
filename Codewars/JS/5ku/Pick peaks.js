function pickPeaks(arr) {
    result = { pos: [], peaks: [] };
    const end = arr.length - 1;
    main_loop: for (index in arr) {
        i = Number(index);
        if (i == 0 || i == end) continue;
        let current = arr[i];
        let previous = arr[i - 1];
        let next = arr[i + 1];
        if (current > previous) {
            if (current < next) continue;
            if (current == next) {
                let search = i + 1;
                while (search < end + 1) {
                    if (arr[search] < current) break;
                    if (arr[search] > current) continue main_loop;
                    if (search == end) continue main_loop;
                    search++;
                }
            }
            result['pos'].push(i);
            result['peaks'].push(current);
        }
    }
    return result;
}

// console.log(pickPeaks([5, 6, 6]));
console.log(pickPeaks([5, 6, 6, 5]));

// console.log(pickPeaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {
//     pos: [3, 7],
//     peaks: [6, 3],
// });
// console.log(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {
//     pos: [3, 7],
//     peaks: [6, 3],
// });
// console.log(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {
//     pos: [3, 7, 10],
//     peaks: [6, 3, 2],
// });
// console.log(pickPeaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {
//     pos: [2, 4],
//     peaks: [3, 2],
// });
// console.log(pickPeaks([2, 1, 3, 1, 2, 2, 2, 2]), { pos: [2], peaks: [3] });
// console.log(pickPeaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), { pos: [2], peaks: [3] });
// console.log(pickPeaks([2, 1, 3, 2, 2, 2, 2, 1]), { pos: [2], peaks: [3] });
// console.log(
//     pickPeaks([
//         1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3,
//     ]),
//     { pos: [2, 7, 14, 20], peaks: [5, 6, 5, 5] }
// );
// console.log(pickPeaks([]), { pos: [], peaks: [] });
// console.log(pickPeaks([1, 1, 1, 1]), { pos: [], peaks: [] });
