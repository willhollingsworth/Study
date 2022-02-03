function rgb(r, g, b) {
    let output = '';
    [r, g, b].forEach((i) => {
        if (i > 255) i = 255;
        if (i < 0) i = 0;
        output += dec_to_hex(i);
    });
    return output;
}

function dec_to_hex(dec) {
    const hex_chars = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' };
    let output = { first: Math.floor(dec / 16), second: dec % 16 };
    Object.keys(output).forEach((i) => {
        let char = output[i];
        if (char > 9) {
            output[i] = hex_chars[char];
        } else {
            output[i] = char.toString();
        }
    });
    return output.first + output.second;
}
console.log(rgb(0, 0, -20), '000000');
console.log(rgb(300, 255, 255), 'FFFFFF');
console.log(rgb(173, 255, 47), 'ADFF2F');
