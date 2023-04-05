function itemHTML(type, amount) { //formatted HTML for an order item
    let price = '$' + (amount * 6).toString() + '.00'
    return "<div class=\"item\"><p>" + type + " </p>, " + amount + "<b>, " + price + "</b></p></div>"
}

const order = {
    echeveria: localStorage.getItem('echeveria'),
    snakeplant: localStorage.getItem('snakeplant'),
    moneytree: localStorage.getItem('moneytree'),
    pothos: localStorage.getItem('pothos'),
    cactus: localStorage.getItem('cactus'),
    airplant: localStorage.getItem('airplant'),
};

/* format order and add it to the page */

let total = 0
let orderHTML = "";

for (const key in order) { //display order to the user
    if(order[key] != null) {
        orderHTML += itemHTML(key, Number(order[key]));
        total += Number(order[key]);
    }
}

orderHTML += "<h2><b>Total: $" + (total * 6).toString() + ".00</b></h2>";

const div = document.getElementsByClassName('invoice')[0];
div.innerHTML = orderHTML;

/* submission code */

const submit = document.getElementById('submit');
const form = document.getElementById('info');

submit.addEventListener('click', () => { //submit order
    const data = new FormData(form);
    if (total === 0) {
        alert('Cart cannot be empty');
        return;
    }
    const name = data.get('name');
    const email = data.get('email');
    const phone = data.get('phoneNo.');
    if (name === '' || email === '' || phone === '') {
        alert("Incomplete form!");
        return;
    }
    localStorage.clear();
    alert("Order successful!")
    fetch("/checkout/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            email: email,
            phone: phone,
            echeveria: order.echeveria != null ? order.echeveria : 0,
            snakeplant: order.snakeplant != null ? order.snakeplant : 0,
            moneytree: order.moneytree != null ? order.moneytree : 0,
            pothos: order.pothos != null ? order.pothos : 0,
            cactus: order.cactus != null ? order.cactus : 0,
            airplant: order.airplant != null ? order.airplant : 0
        })
    })
});