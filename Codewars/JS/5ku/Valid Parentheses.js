function validParentheses(parens) {
    let total = 0;
    for (let c of parens.split('')) {
        c == '(' ? total++ : c == ')' ? total-- : 0;
        if (total < 0) return false;
    }
    return total == 0;
}
function validParentheses_v1(parens) {
    // basic matcher just checks if total of each brackets are the same
    // fails on items like ))((
    let opening = (parens.match(/\(/g) || []).length,
        closing = (parens.match(/\)/g) || []).length;
    return opening == closing;
}

console.log(validParentheses('((s(e))'), false);
console.log(validParentheses(')('), false);
console.log(validParentheses('((()))'), true);
console.log(validParentheses(')'), false);
console.log(validParentheses(''), true);
console.log(validParentheses('()'), true);
console.log(validParentheses('())'), false);
