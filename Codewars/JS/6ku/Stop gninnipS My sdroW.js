function spinWords(string) {
    return string
        .split(' ')
        .map((word) =>
            word.length > 4 ? word.split('').reverse().join('') : word
        )
        .join(' ');
}
function spinWords_v1(string) {
    const words = string.split(' ');
    let output = [];
    for (let word of words) {
        if (word.length > 4) {
            let temp = '';
            word.split('').forEach((letter) => (temp = letter + temp));
            output.push(temp);
        } else {
            output.push(word);
        }
    }
    return output.join(' ');
}

// console.log(spinWords('Welcome'), 'emocleW');
console.log(spinWords('Hey fellow warriors'), 'Hey wollef sroirraw');
// console.log(spinWords('This is a test'), 'This is a test');
// console.log(spinWords('This is another test'), 'This is rehtona test');
// console.log(
//     spinWords('You are almost to the last test'),
//     'You are tsomla to the last test'
// );
// console.log(
//     spinWords('Just kidding there is still one more'),
//     'Just gniddik ereht is llits one more'
// );
// console.log(
//     spinWords('Seriously this is the last one'),
//     'ylsuoireS this is the last one'
// );
