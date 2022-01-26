function humanReadable(seconds) {
    let h = seconds > 60 * 60 ? seconds % (60 * 60 * 60) : 0,
        m = seconds > 59 ? seconds % (60 * 60) : 0,
        s = seconds % 60;
    [h, m, s] = [h, m, s].map((n) => n.toString().padStart(2, 0));
    return h + ':' + m + ':' + s;
}

console.log(humanReadable(0), '00:00:00');
console.log(humanReadable(59), '00:00:59');
console.log(humanReadable(60), '00:01:00');
console.log(humanReadable(90), '00:01:30');
console.log(humanReadable(3599), '00:59:59');
console.log(humanReadable(3600), '01:00:00');
console.log(humanReadable(45296), '12:34:56');
console.log(humanReadable(86399), '23:59:59');
console.log(humanReadable(86400), '24:00:00');
console.log(humanReadable(359999), '99:59:59');
