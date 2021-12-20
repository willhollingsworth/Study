export async function main(ns) {
    var hosts = ns.scan(ns.getHostname()); // build an array of directly connected hosts
    var hack_chance = 0;
    var hack_secs = 0;
    var hack_amount = 0;
    var money_percent = 0;
    var hack_money_per_sec = 0;
    for (let target of hosts) {
        // loop over each host
        hack_chance = Math.round(ns.hackAnalyzeChance(target) * 100);
        hack_secs = Math.round(ns.getHackTime(target) / 1000);
        hack_amount = Math.round(
            ns.hackAnalyze(target) * ns.getServerMoneyAvailable(target)
        );
        money_percent = Math.round(
            (ns.getServerMoneyAvailable(target) /
                ns.getServerMaxMoney(target)) *
                100
        );
        hack_money_per_sec = Math.round(
            (hack_amount / hack_secs) * (hack_chance / 100)
        );
        ns.tprint(
            target,
            ' : ',
            hack_chance,
            '% success - ',
            hack_secs,
            ' secs - $',
            hack_amount,
            ' total gained - $',
            hack_money_per_sec,
            ' per sec - ',
            money_percent,
            '% remaining'
        );
    }
}
