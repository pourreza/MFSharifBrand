//var cart_price = [];
//if (window.localStorage && localStorage.getItem('products'))
//{
//    sum = 0;
//    var storedNames = JSON.parse(localStorage["products"]);
//    var storedPrices = JSON.parse(localStorage["prices"])
//    for (var i = 0; i < storedNames.length; i++) {
//        $(".my-dropdown").append('<li role="presentation" id="' + i + '"><a href="#" class="cross" onclick="exit(' + i + ')"> &#10006;<span style="font-weight: bold">' + storedNames[i] + '</span></a></li>');
//        sum += parseInt(storedPrices[i]);
//    }
//
//    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + sum + '  تومان</span></span></a></li>');
//}else{
//    document.getElementsByClassName('my-dropdown')[0].innerHTML='<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + 0 + '  تومان</span></span></a></li>';
//}
var url = "cartProducts";
var categry;
$.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function(data, status, xhr){
        if (data.result == 0){
            // Request error
        }else
        {
            document.getElementsByClassName("my-dropdown")[0].innerHTML = "";
            for (var i = 0; i < data.product_names.length; i++) {
                $(".my-dropdown").append('<li role="presentation" id="' + data.product_ids[i] + '"><a href="#" class="cross" onclick="exit(' + data.product_ids[i] + ')"> &#10006;<span style="font-weight: bold">' + data.product_names[i] + '('+ data.product_count[i]+' '+ data.product_unit[i]+')</span></a></li>');
            }
            if (data.sum!=0){
                $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + data.sum + '  تومان</span></span></a></li>');
            }
            else{
                $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
            }

        }
    }


});

var url = "../../cartProducts";
var categry;
$.ajax({
    url: url,
    type: 'get',
    dataType: 'json',
    success: function(data, status, xhr){
        if (data.result == 0){
            // Request error
        }else
        {

            document.getElementsByClassName("my-dropdown")[0].innerHTML = ""
            for (var i = 0; i < data.product_names.length; i++) {
                $(".my-dropdown").append('<li role="presentation" id="' + data.product_ids[i] + '"><a href="#" class="cross" onclick="exit(' + data.product_ids[i] + ')"> &#10006;<span style="font-weight: bold">' + data.product_names[i] + '('+ data.product_count[i]+' '+ data.product_unit[i]+')</span></a></li>');
            }
            if (data.sum!=0){
                $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + data.sum + '  تومان</span></span></a></li>');
            }
            else{
                $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
            }

        }
    }


});


function exit(id){

    var url = "removeCartProduct";
    var categry;
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        data : {'id':id},
        success: function(data, status, xhr){
            if (data.result == 0){
                // Request error
            }else
            {
                document.getElementById(id).remove();
                $('.my-dropdown li:last').remove();
                $('.my-dropdown li:last').remove();
                if (data.sum!=0){
                    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + data.sum + '   تومان</a></li>');
                }else{
                    $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
                }
                alert('کالای انتخاب شده از سبد خرید حذف گردید.');
            }
        }


    });

    var temp = "tr_"+id;
    var tr = document.getElementById(temp);
    if (tr!=undefined){
        tr.parentNode.removeChild(tr);
    }


    var url = "../../removeCartProduct";
    var categry;
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        data : {'id':id},
        success: function(data, status, xhr){
            if (data.result == 0){
                // Request error
            }else
            {
                document.getElementById(id).remove();
                $('.my-dropdown li:last').remove();
                $('.my-dropdown li:last').remove();
                if (data.sum!=0){
                    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + data.sum + '   تومان</a></li>');
                }else{
                    $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
                }
                alert('کالای انتخاب شده از سبد خرید حذف گردید.');
            }
        }


    });

}

function add_cart(id) {

    var url = "../../addCartProduct";
    var categry;
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        data : {'id':id},
        success: function(data, status, xhr){
            if (data.result == 0){
                // Request error
            }else
            {
                document.getElementsByClassName("my-dropdown")[0].innerHTML = ""
                for (var i = 0; i < data.product_names.length; i++) {
                    $(".my-dropdown").append('<li role="presentation" id="' + data.product_ids[i] + '"><a href="#" class="cross" onclick="exit(' + data.product_ids[i] + ')"> &#10006;<span style="font-weight: bold">' + data.product_names[i] + '('+ data.product_count[i]+' '+ data.product_unit[i]+')</span></a></li>');
                }
                if (data.sum!=0){
                    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + data.sum + '  تومان</span></span></a></li>');
                }
                else{
                    $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
                }
                alert("این کالا به سبد خرید اضافه شد :)")
            }
        }


    });

}