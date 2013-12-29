var url = "categorylisturl";

	console.log("umad in tu");
	$.ajax({
		url: url,
		type: 'get',
		dataType: 'json',
		success: function(data, status, xhr){
		    if (data.result == 0){
		       // Request error
                console.log ("Error shod alan?");
		    }else 
		    {
                console.log ("javabe ajax umad");

		    	//data__ = data.categoryList;
		     for (var i = 0  ; i < data.categoryList.length ; i++)
				     {
				     	// console.log("data: "+data);
				     	// console.log(data.categoryList);
				     var new_li = document.createElement('li');
				     new_li.setAttribute("id", "li_"+data.categoryList[i].id);
				     new_li.setAttribute("class", "li_cat");
				     $("#dropdown_ul").append(new_li);
				     var new_a = document.createElement ('a');
				     new_a.innerHTML = data.categoryList[i].name;
				     new_a.setAttribute("id", data.categoryList[i].id);
				     new_a.setAttribute("name", data.categoryList[i].name);
				     new_a.setAttribute("href", "#");
				     $("#li_"+data.categoryList[i].id).append(new_a);
						     if (i === 1 || i === 0)
						     {
						     	var li_div = document.createElement('li');
						     	li_div.setAttribute("class", "divider");
						     	$("#dropdown_ul").append(li_div);
						     }
				     

				     }



				console.log($("li_cat"));

				$('.li_cat').click( function(event){
				prim_str = event.target.id;
				console.log("hello world again!");
				 console.log(event.target);
				 console.log(prim_str);
				category__ = parseInt(prim_str);
				id_str= prim_str.substring(3);
				console.log(id_str);
				loadProducts(1, category__, search_string__); 
				$("#selected_category").text(event.target.name) ;

				});

			}
		},

		// ...

});


