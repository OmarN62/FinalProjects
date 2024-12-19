const taxRate = 0.08;
const phonePrice = 100;
const accessoryPrice = 100;
const spendingThreshold = 200;
var bankBalance = 1000;
var amount = 0;

function taxCalc(amount) {
    return amount * taxRate;
}

function format(amount) {
    return "$" + amount.toFixed( 2 );
}

while (amount < bankBalance) {
    amount = amount + phonePrice;

    if (amount < spendingThreshold) {
        amount = amount + accessoryPrice;
    }
}

amount = amount + taxCalc( amount );

console.log(
    "Your purchase: " + format(amount)
);

if (amount > bankBalance) {
    console.log(
        "You can't afford this purchase. :("
    );
}