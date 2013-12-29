var pro_id ;
var pro_price;
var pro_name;

var cart_price = [];
var ajaxData = {
    category: 17,
    search: "",
    page: 1,
    pageSize: 10
}
var url = "http://webproject.roohy.me/ajax/2/m&f/product/list";

$.ajax({
    url: url,
    type: 'post',
    dataType: 'json',
    data: ajaxData,
    success: function (data, status, xhr) {
        if (data.result == 0) {
            // Request error
        } else {
//            pro_id = data.productList[0].id;
            pro_name = data.productList[0].name;
            pro_price = data.productList[0].price;
//            $(".pr-name").html(data.productList[0].name);
//            $("#pr-info").html(data.productList[0].name);
//            $("#pr-info-price").html(data.productList[0].price + "   تومان");
//            $("#pr-image").attr('src', data.productList[0].picUrl);//src(data.productList[0].picUrl);
//            $("#pr-image-big").attr('src', data.productList[0].picUrl);//

        }
    }
    // ...
});
var ajaxComment = {
    category: 17,
    search: "",
    page: 1,
    pageSize: 10
}
var urlComment = "http://webproject.roohy.me/ajax/2/m&f/comment/list";
$.ajax({
    url: urlComment,
    type: 'post',
    dataType: 'json',
    data: ajaxComment,
    success: function (data, status, xhr) {
        if (data.result == 0) {
            // Request error
        } else {
//            for (var i = 0; i < data.commentList.length; i++) {
//                $("#prev-comments").append('<li>' + data.commentList[i].name + ' :  ' + data.commentList[i].message + '</li>');
//            }
        }
    }
    // ...
});


var urlCartList = "http://webproject.roohy.me/ajax/2/m&f/cart/list";
$.ajax({
    url: urlCartList,
    type: 'post',
    dataType: 'json',
    data: ajaxComment,
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

function add(pk) {
    alert(pk);
    var comment = document.getElementById('newComment');
//    $("#prev-comments").append('<li>ذوالفقار: ' + comment.value + '</li>');
    var urlNewComment = "../addComment";
    var ajaxNewComment = {
        "message": comment.value,
        "name": 'هادی',
        "pro_id": pk
    }
    $.ajax({
        url: urlNewComment,
        type: 'get',
        dataType: 'json',
        data: ajaxNewComment,
        success: function (data, status, xhr) {
            if (data.result == 0) {
                // Request error
            } else {
                alert("resid");
//                $("#prev-comments").innerHTML = "";
//                for (var cm in data.comments){
//                    $("#prev-comments").append('<li>'+cm.name+':'+cm.comment+'<p>تاریخ:'+cm.date+'</p></li>');
//                }
            }
        }
        // ...
    });
    document.getElementById('newComment').value="";
}

function add_cart() {
        var urlNewComment = "http://webproject.roohy.me/ajax/2/m&f/cart/add";
        var ajaxNewComment = {
            "productId": pro_id
        }
        $.ajax({
            url: urlNewComment,
            type: 'post',
            dataType: 'json',
            data: ajaxNewComment,
            success: function (data, status, xhr) {
                if (data.result == 0) {
                    // Request error
//                    alert("resid");
                } else {
//                    alert("resid");
                }
            }
            // ...
        });
        var temp = [pro_id, pro_price];
        cart_price.push(temp);
        $('.my-dropdown li:last').remove();
        $('.my-dropdown li:last').remove();
    $(".my-dropdown").append('<li role="presentation" id="' +pro_id + '"><a href="#" class="cross" onclick="exit(' + pro_id + ')"> &#10006;<span style="font-weight: bold">' + pro_name + '</span></a></li>');
        sum += pro_price;
        $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + sum + '   تومان</a></li>');
//        document.getElementById("my-cart-add").innerHTML = "به سبد اضافه شده";
    alert("این کالا به سبد خرید اضافه شد :)")

}
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