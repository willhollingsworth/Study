var hosts = scan(getHostname()); // build an array of directly connected hosts
var success_threshold = 75;
var money_threshold = 50;

var script = '';
var threads = 0;

var hack_chance = 0;
var money_percent = 0;
var log = false;

if (args[0] == 'log') {
    log = true;
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
    if (k) {
        continue;
    }
    if (hack_chance < success_threshold) {
        if (log) {
            tprint(target, ': hack chance too low ', hack_chance);
        }
        script = 'selfweakenloop.script';
    } else if (money_percent < money_threshold) {
        if (log) {
            tprint(target, ' : money remaining too low ', money_percent);
        }
        script = 'selfgrowloop.script';
    } else {
        script = 'selfhackloop.script';
    }
    threads = Math.floor(
        // determine the number of times the script can be run
        getServerMaxRam(target) / getScriptRam(script, target)
    );
    scp(script, 'home', target); // deploy script to server
    if (log) {
        tprint(target, ': run ', script, ' - threads ', threads);
    }
    exec(script, target, threads); // run the script
}
