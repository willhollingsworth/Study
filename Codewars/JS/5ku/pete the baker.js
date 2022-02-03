function cakes(recipe, available) {
    let output = 9999999;

    Object.keys(recipe).forEach((i) => {
        if (!Object.keys(available).includes(i)) {
            output = 0;
            return;
        }
        let requirement = recipe[i],
            amount = Math.floor(available[i] / requirement);
        output = Math.min(output, amount);
    });
    return output;
}

recipe = { flour: 500, sugar: 200, eggs: 1 };
available = { flour: 1200, sugar: 1200, eggs: 5, milk: 200 };
console.log(cakes(recipe, available), 2);

recipe = { apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100 };
available = { sugar: 500, flour: 2000, milk: 2000 };
console.log(cakes(recipe, available), 0);
