if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'))
}
$(document).on('click', '.add-to-cart', function() {
    var item_id = this.id.toString();

    if (cart[item_id] != undefined) {
        qty = cart[item_id][0] + 1;
        cart[item_id][0] = qty;
    } else {
        qty = 1;
        item_name = document.getElementById("name-" + item_id).innerHTML;
        item_price = document.getElementById("price-" + item_id).innerHTML;
        cart[item_id] = [qty, item_name, item_price];
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById("cart").innerHTML = "Cart(" + Object.keys(cart).length + ")";
});
/*document.getElementByClass('add-to-cart').addEventListener("click", addToCart);

function addToCart()
$(function () {
    $('[data-toggle="popover"]').popover();
    document.getElementById("cart").setAttribute('data-content', '<h5>This is your cart</h5>')
})*/

function displayCart(cart) {
    var cartString = "";
    cartString += '<h3 class="text-right">Cart Items</h3><hr>';
    var cartIndex = 1;

    let cartObject = JSON.parse(localStorage.getItem('cart'));

    for (item in cartObject) {
        cartString += cartIndex + ": ";
        cartString += cartObject[item][1] + "| <b>Qty: </b>" + cartObject[item][0] + "</br><hr>";
        cartIndex += 1;
        /*if (document.getElementById("name-" + x) !== null) {
            cartString += document.getElementById("name-" + x).innerHTML + " | <b>Qty: </b>" + cart[x][0] + "</br><hr>";
        }*/

    }
    cartString += "<a href='/checkout'><button class='btn btn-success checkout' id='checkout'>Checkout</button></a></br>";
    cartString += "</br><button class='btn btn-warning clear-cart' id='clear-cart' onclick='clearCart()'>Clear Cart</button></br>";

    document.getElementById("cart").setAttribute('data-content', cartString);
    $('[data-toggle="popover"]').popover();
}

function clearCart() {
    localStorage.clear();
}

displayCart(cart);

if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'))
}
var itemString = "";
var total = 0;
for (var item in cart) {
    let name = cart[item][1];
    let quantity = cart[item][0];
    let price = cart[item][2] * quantity;
    total += parseFloat(price);
    //<span class="badge badge-primary badge-pill">${quantity}</span>

    itemString = `<li class="list-group-item d-flex justify-content-between align-items-center">${name} <br/> Qty: ${quantity}<span class="badge price">$ ${price}</span></li>`;
    $('#item_list').append(itemString);
}

$('#items').val(JSON.stringify(cart));

showTotal = `<li class="list-group-item d-flex justify-content-between align-items-center"><b class="b-total">Total: </b><span class="badge total-price">$ ${total.toFixed(2)}</span></li>`;
$('#show-total').append(showTotal);

$('#total').val(total.toFixed(2));