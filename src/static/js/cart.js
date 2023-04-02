button = document.getElementById("add");

button.addEventListener('click', (e) => {
    let type = e.target.classList[3]; // type is added to the class list
    let currentAmount = localStorage.getItem(type);
    if (currentAmount === null) { //update cart amounts accordingly
        localStorage.setItem(type, 1);
    }
    else {
        localStorage.setItem(type, (parseInt(currentAmount) + 1));
    }
    alert("Added 1 " + type + " to cart");
});
