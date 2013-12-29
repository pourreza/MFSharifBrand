var cart_price = [];
if (window.localStorage && localStorage.getItem('products'))
{
    sum = 0;
    var storedNames = JSON.parse(localStorage["products"]);
    var storedPrices = JSON.parse(localStorage["prices"])
    for (var i = 0; i < storedNames.length; i++) {
        $(".my-dropdown").append('<li role="presentation" id="' + i + '"><a href="#" class="cross" onclick="exit(' + i + ')"> &#10006;<span style="font-weight: bold">' + storedNames[i] + '</span></a></li>');
        sum += parseInt(storedPrices[i]);
    }

    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + sum + '  تومان</span></span></a></li>');
}else{
    document.getElementsByClassName('my-dropdown')[0].innerHTML='<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + 0 + '  تومان</span></span></a></li>';
}

function exit(id){
    var storedNames = JSON.parse(localStorage["products"]);
    var storedIndexes = JSON.parse(localStorage["indexes"]);
    for (var i=id; i<storedNames.length; i++)
    {
        storedIndexes[i] = (parseInt(storedIndexes[i]))-1;
    }
    storedNames.splice(id,1);
    storedIndexes.splice(id,1);
    var storedPrices = JSON.parse(localStorage["prices"]);
    storedPrices.splice(id,1);

    localStorage["products"] = JSON.stringify(storedNames);
    localStorage["prices"] = JSON.stringify(storedPrices);
    localStorage["indexes"] = JSON.stringify(storedIndexes);
    sum = 0;
    for(var i=0; i<storedPrices.length; i++)
    {
        sum += parseInt(storedPrices[i]);
    }

    document.getElementById(id).remove();
    $('.my-dropdown li:last').remove();
    $('.my-dropdown li:last').remove();
    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + sum + '   تومان</a></li>');
    alert('کالای انتخاب شده از سبد خرید حذف گردید.');
}

function add_cart(name,price) {
    var storedNames = [];
    var storedPrices = [];
    var storedIndexes = [];
    if (localStorage["products"])
    {
        storedNames = JSON.parse(localStorage["products"]);
        storedPrices = JSON.parse(localStorage["prices"]);
        storedIndexes = JSON.parse(localStorage["indexes"]);
    }
    storedNames.push(name);
    storedPrices.push(price);
    storedIndexes.push((storedNames.length-1));
    localStorage["products"] = JSON.stringify(storedNames);
    localStorage["prices"] = JSON.stringify(storedPrices);
    localStorage["indexes"] = JSON.stringify(storedIndexes);
    sum = 0;
    for (var i=0; i<storedPrices.length; i++)
    {
        sum += parseInt(storedPrices[i]);
    }
    $('.my-dropdown li:last').remove();
    $('.my-dropdown li:last').remove();
    $(".my-dropdown").append('<li role="presentation" id="' + (storedNames.length-1) + '"><a href="#" class="cross" onclick="exit(' + (storedNames.length-1) + ')"> &#10006;<span style="font-weight: bold">' + name + '</span></a></li>');
    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + sum + '   تومان</a></li>');
    alert("این کالا به سبد خرید اضافه شد :)")

}