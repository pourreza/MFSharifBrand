


function loadProducts( whichpage, category_, search_string){
    console.log ("ejra shodi alan?!");

	var ajaxData = {
		"category": category_,
		"search": search_string,
		"page": whichpage,
		"pageSize": 8
	}

	//var url = "http://webproject.roohy.me/ajax/2/m&f/product/list";
    var url = "/loadproductitems";
    console.log ("inam ejra misheee?!");
	$.ajax({
		url: url,
		type : 'get',
		dataType: 'json',
		data: ajaxData,
		success: function (data, status, xhr){
			if (data.result !== 0){

				console.log(search_string);
				console.log(category_);
                console.log ("in chiii?!");
				setProducts(data, whichpage);


				}
				else
					console.log("nashod");


			},
        error: function(){
                                alert ('متأسفانه پاسخ مناسب از سرور دریافت نشد.');
        }


	});

	document.getElementsByClassName("next")[0].innerHTML = "بعدی";
 			document.getElementsByClassName("prev")[0].innerHTML = "قبلی";

}



		    		function setProducts(data, whichpage){
		 	       // console.log (data.productList[1].name);

		       	number_of_pages = Math.ceil(data.totalResults/data.pageSize);
			 		console.log("number_of_pages: "+ number_of_pages);

				 		// console.log (data.totalResults);

				if (data.totalResults === 0)
				{

					alert ("محصولی با مشخصات ذکر شده یافت نشد");
				}
				

				// console.log (data.productList.length);
				//  console.log(data);
				//  console.log(data.productList);
				 if (document.getElementById("carousel1") === null)
				 {
				 	var elem = document.createElement('div');
				elem.setAttribute("id","carousel1");
				elem.style.width = '700px';
				elem.style.height = '500px';
				elem.style.background = '#000';
				// elem.style.overflow = 'scroll';

				document.getElementById("items_container").appendChild(elem);
				 }


				 if ($("#carousel1").children().length > 0)
					 document.getElementById("carousel1").removeChild(document.getElementById("carousel1").childNodes[0]);

				 for (var i = 0 ; i < data.productList.length ; i++)
				 {


				var img_elem = document.createElement('img');
				img_elem.setAttribute("class","cloudcarousel");
				img_elem.setAttribute("src",data.productList[i].picUrl);
				img_elem.setAttribute("data-price",data.productList[i].price);
				img_elem.setAttribute("title",data.productList[i].name);
				img_elem.setAttribute("id", "_img_"+data.productList[i].id);
                img_elem.setAttribute("data-theid", data.productList[i].id);


				document.getElementById("carousel1").appendChild(img_elem);
      			  
			}
			// if (!document.getElementById("description_container").hasChildNodes() )
			// {
			// 	console.log("raf in tu");
			// 	var title_p = document.createElement('p');
   //          	title_p.setAttribute("id", "title-text");
            	
   //          	document.getElementById("description_container").appendChild(title_p);

   //          	var price_p = document.createElement('p');
   //          	price_p.setAttribute("id", "price");
            	
   //          	document.getElementById("description_container").appendChild(price_p);




			// }

		
		    

		    $("#carousel1").CloudCarousel(		
					{		

						xPos: 350,
						yPos: 150,
						buttonLeft: $("#left-but"),
						 buttonRight: $("#right-but"),
						priceBox: $("#price"),
						titleBox: $("#title-text"),
                        theidBox: $("#hidden_id"),

					});
		   



if (whichpage === 1)
{
		    $(function(){
$("#holder").pagination({
	pages: number_of_pages,
	 displayedPages: 5,
	cssStyle: 'light-theme',
	onPageClick: function(pageNumber, e)
 {
		// 	NO = pageNumber;
		// console.log("chanta?"+NO);
		loadProducts(pageNumber, category__, search_string__);
}, 
});
});

		    console.log ("ejra mishe asan?");
		    document.getElementsByClassName("next")[0].innerHTML = "بعدی";
 			document.getElementsByClassName("prev")[0].innerHTML = "قبلی";
		}


		}

// document.getElementById("add_to_cart_").onclick() {
// 	addRealQuick();
 //}


function addRealQuick() {

	if (document.getElementById("title-text").innerHTML !== "")
		{
		//id ro bezaram in 
		var temp_array_ = document.getElementsByClassName("cloudcarousel");
		for (var i = 0 ; i < temp_array_.length ; i++)
		{
			if (temp_array_[i].title === document.getElementById("title-text").innerHTML )
				{
					pro_name = document.getElementById("title-text").innerHTML;
					id_string = temp_array_[i].id;
					console.log(id_string);
					pro_id = id_string.substring(5);
					
					console.log ("pro_id:"+ pro_id);
					// var pro_price = parseInt(temp_array_[i].data-price);
					// console.log(pro_price);
					pro_price = parseInt(document.getElementById("price").innerHTML);
					console.log (pro_price);
					console.log(cart_price);
					add_cart(pro_id);
				}
		}
		}
}


//function add_cart() {
////        alert(pro_id);
//        var urlNewComment = "http://webproject.roohy.me/ajax/2/m&f/cart/add";
//        var ajaxNewComment = {
//            "productId": pro_id,
//        }
//        $.ajax({
//            url: urlNewComment,
//            type: 'get',
//            dataType: 'json',
//            data: ajaxNewComment,
//            success: function (data, status, xhr) {
//                if (data.result == 0) {
//                    // Request error
////                    alert("resid");
//                } else {
////                    alert("resid");
//                }
//            },
//            // ...
//        });
//        var temp = [pro_id, pro_price];
//        cart_price.push(temp);
//        $('.my-dropdown li:last').remove();
//        $('.my-dropdown li:last').remove();
//        console.log("++"+pro_id);
//        $(".my-dropdown").append('<li role="presentation" id="' +pro_id + '"><a href="#" class="cross" onclick="exit(' + pro_id + ')"> &#10006;<span style="font-weight: bold">' + pro_name + '</span></a></li>');
//
//       sum += pro_price;
//       $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع:' + sum + '   تومان</a></li>');
//
//}
//
//function add_cart(id) {
//
//    var url = "../../addCartProduct";
//    var categry;
//    $.ajax({
//        url: url,
//        type: 'get',
//        dataType: 'json',
//        data : {'id':id},
//        success: function(data, status, xhr){
//            if (data.result == 0){
//                // Request error
//            }else
//            {
//                document.getElementsByClassName("my-dropdown")[0].innerHTML = ""
//                for (var i = 0; i < data.product_names.length; i++) {
//                    $(".my-dropdown").append('<li role="presentation" id="' + data.product_ids[i] + '"><a href="#" class="cross" onclick="exit(' + data.product_ids[i] + ')"> &#10006;<span style="font-weight: bold">' + data.product_names[i] + '('+ data.product_count[i]+' '+ data.product_unit[i]+')</span></a></li>');
//                }
//                if (data.sum!=0){
//                    $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + data.sum + '  تومان</span></span></a></li>');
//                }
//                else{
//                    $(".my-dropdown").append('<li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold"> سبد خرید خالیست.</a></li>');
//                }
//                alert("این کالا به سبد خرید اضافه شد :)")
//            }
//        }
//
//
//    });
//
//}
function load_current_cart(){


var urlCartList = "http://webproject.roohy.me/ajax/2/m&f/cart/list";
$.ajax({
    url: urlCartList,
    type: 'get',
    dataType: 'json',
    success: function (data, status, xhr) {
        if (data.result == 0) {
            // Request error
        } else {
            sum = 0;
            for (var i = 0; i < data.cart.length; i++) {
                $(".my-dropdown").append('<li role="presentation" id= "' + data.cart[i].id + '"><a href="#" class="cross" onclick="exit(' + data.cart[i].id + ')"> &#10006;<span style="font-weight: bold">' + data.cart[i].name + '</span></a></li>');
                var temp = [data.cart[i].id, data.cart[i].price];
//                if (pro_id===data.cart[i].id){
//                    added = false;
//                    document.getElementById("my-cart-add").innerHTML = "به سبد اضافه شده";
//                }
                cart_price.push(temp);
//                    var value = data.cart[i].price;
//                    cart_price[i] = { temp : value};
                sum += data.cart[i].price;
            }

            for (var prp in cart_price) {
                console.log(cart_price[prp][0]);
            }
//                alert(sum);
            $(".my-dropdown").append('<li role="presentation" class="divider"></li><li role="presentation"><a role="menuitem" tabindex="-1" href="#" style="font-weight: bold">مجموع: <span style="font-weight: bold">' + sum + '  تومان</span></span></a></li>');
        }
    },
    // ...
});
}


function exit(id){
    var urlNewComment = "http://webproject.roohy.me/ajax/2/m&f/cart/remove";
    var ajaxNewComment = {
        "productId": id
    }
    $.ajax({
        url: urlNewComment,
        type: 'get',
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