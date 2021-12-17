var hosts = scan(getHostname()); // build an array of directly connected hosts
var success_threshold = 75;
var money_threshold = 50;

var script = '';
hack_chance = 0;
if (args[0] == 'hack' || !args[0]) {
    // if argument is blank or hack then standard behavior
    script = 'selfhack.script';
} else if (args[0] == 'kill') {
    // if kill argument then shut down all active programs via a kill all
    var k = true;
}

for (i = 0; i < hosts.length; ++i) {
    // loop over each host
    target = hosts[i];
    hack_chance = Math.round(hackAnalyzeChance(target) * 100);
    killall(target);
    money_percent = Math.round(
        (getServerMoneyAvailable(target) / getServerMaxMoney(target)) * 100
    );
    tprint('money percent ', money_percent, '%');
    if (k) {
        continue;
    }

    var stime = Math.round(
        // determine the number of times the script can be run
        getServerMaxRam(target) / getScriptRam(script, target)
    );
    if (hack_chance < success_threshold) {
        tprint('hack chance to low ', hack_chance);
        script = 'selfgrow.script';
    }

    scp(script, 'home', target); // deploy script to server
    tprint(script, ' run on ', target, ' threads ', stime);
    exec(script, target, stime); // run the script
}
