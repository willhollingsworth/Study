/** @param {NS} ns **/
export async function main(ns) {
    let hosts = ns.scan(ns.getHostname()); // build an array of directly connected hosts
    let hack_chance = 0,
        hack_secs,
        hack_amount,
        money_percent,
        money_total,
        hack_money_per_sec;
    let column = 20;
    var headers = () => {
        table([
            'target',
            'hack chance',
            'hack secs',
            'hack $',
            'h $/s',
            '$ total',
            '$ %',
        ]);
    };

    var table = (a) => {
        // displays data in a spreadsheet like table format for easier reading, currently has fixed width
        let string = '',
            pad = 0,
            length = 0;
        for (let x of a) {
            length = (x + '').length; // convert to string
            pad = column - length;
            pad = Array(pad + 1).join(' '); // pad ending with spaces
            string = string.concat(x);
            string = string.concat(pad);
        }
        ns.tprint(string);
    };
    headers();
    for (let target of hosts) {
        // loop over each host
        hack_chance = Math.round(ns.hackAnalyzeChance(target) * 100);
        hack_secs = Math.round(ns.getHackTime(target) / 1000);
        hack_amount = Math.round(
            ns.hackAnalyze(target) * ns.getServerMoneyAvailable(target)
        );
        money_total = Math.round(ns.getServerMoneyAvailable(target));
        money_percent = Math.round(
            (ns.getServerMoneyAvailable(target) /
                ns.getServerMaxMoney(target)) *
                100
        );
        hack_money_per_sec = Math.round(
            (hack_amount / hack_secs) * (hack_chance / 100)
        );
        table([
            target,
            hack_chance,
            hack_secs,
            hack_amount,
            hack_money_per_sec,
            money_total,
            money_percent,
        ]);
    }
}
