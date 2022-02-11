function ipsBetween(start, end) {
    var start_octets = start.split('.'),
        end_octets = end.split('.');
    output = 0;

    for (let s in start_octets) {
        output += (end_octets[s] - start_octets[s]) * 256 ** (3 - s);
    }
    return output;
}

console.log(ipsBetween('10.0.0.0', '10.0.0.50'), 50);
console.log(ipsBetween('20.0.0.10', '20.0.1.0'), 246);
console.log(ipsBetween('20.0.0.0', '20.1.0.0'), 246);
