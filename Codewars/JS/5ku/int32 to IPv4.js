function int32ToIp(int32) {
    const binary = int32.toString(2);
    let octets = [];
    if (binary == 0) return '0.0.0.0';
    for (let i = 0; i < 4; i++) {
        octets.push(parseInt(binary.slice(i * 8, (i + 1) * 8), 2));
    }
    return octets.join('.');
}

console.log(int32ToIp(2154959208), '128.114.17.104');
console.log(int32ToIp(0), '0.0.0.0');
console.log(int32ToIp(2149583361), '128.32.10.1');
