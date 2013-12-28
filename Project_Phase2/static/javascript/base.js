var cart_price = [];
var urlCartList = "http://webproject.roohy.me/ajax/2/m&f/cart/list";
$.ajax({
    url: urlCartList,
    type: 'post',
    dataType: 'json',
    data: '',
    success: function (data, status, xhr) {
        if (data.result == 0) {
            // Request error
        } else {
            sum = 0;
            for (var i = 0; i < data.cart.length; i++) {
                $(".my-dropdown").append('<li role="presentation" id="' + data.cart[i].id + '"><a href="#" class="cross" onclick="exit(' + data.cart[i].id + ')"> &#10006;<span style="font-weight: bold">' + data.cart[i].name + '</span></a></li>');
                var temp = [data.cart[i].id, data.cart[i].price];
                cart_price.push(temp);
                sum += data.cart[i].price;
            }

            for (var prp in cart_price) {
                console.log(cart_price[prp][0]);
            }
            $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + sum + '  تومان</span></span></a></li>');
        }
    }
});

function exit(id){
    var urlNewComment = "http://webproject.roohy.me/ajax/2/m&f/cart/remove";
    var ajaxNewComment = {
        "productId": id
    }
    $.ajax({
        url: urlNewComment,
        type: 'post',
        dataType: 'json',
        data: ajaxNewComment,
        success: function (data, status, xhr) {
            if (data.result == 0) {
            } else {
            }
        }
        // ...
    });
    document.getElementById(id).remove();
    $('.my-dropdown li:last').remove();
    $('.my-dropdown li:last').remove();
    var index = 0;
    var temp = [];
    for (var prp in cart_price){
        temp.push(cart_price[prp][0]);
    }

    var i = temp.indexOf(id);
    if (i!=-1){
        sum -= cart_price[i][1];
        cart_price.splice(i, 1);
    }
    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + sum + '   تومان</a></li>');
}