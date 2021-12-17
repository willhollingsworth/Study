var hosts = scan(getHostname()); // build an array of directly connected hosts

if (args[0] == 'hack' || !args[0]) {
    var script = 'selfhack.script';
} else if (args[0] == 'kill') {
    var k = true;
}

for (i = 0; i < hosts.length; ++i) {
    target = hosts[i];
    killall(target);
    if (k) {
        continue;
    }
    var stime = Math.round(
        // determine the number of times the script can be run
        getServerMaxRam(target) / getScriptRam(script, target)
    );
    scp(script, 'home', target); // deploy script to server
    tprint(script, ' run on ', target, ' threads ', stime);
    exec(script, target, stime); // run the script
}
