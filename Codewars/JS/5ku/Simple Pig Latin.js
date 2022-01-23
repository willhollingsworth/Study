function pigIt(str) {
    return str.replace(/(\w{1})(\w*)/g, '$2$1ay');
}
function pigItv1(str) {
    let output = [],
        punctuation = ['.', ',', '!', '#', '?'];

    str.split(' ').forEach((c) => {
        if (!punctuation.includes(c)) {
            let word = c.split('');
            output.push(word.slice(1).join('') + word.slice(0, 1) + 'ay');
        } else {
            output.push(c);
        }
    });
    return output.join(' ');
}

// console.log(pigIt('Pig latin is cool'), 'igPay atinlay siay oolcay');
// console.log(pigIt('This is my string'), 'hisTay siay ymay tringsay');
// console.log(pigIt('This is my string !'), 'hisTay siay ymay tringsay');
console.log(pigIt('O temporat o mores !'));
