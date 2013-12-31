var url = "categorylisturl";
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
            for (var i = 0  ; i < data.categoryList.length/2 + 1 ; i++)
            {
                if ( i !== 1 ){
                    var new_li = document.createElement('li');
                    new_li.setAttribute("id", "li_"+ data.categoryList[i].id);
                    new_li.setAttribute("class", "li_cat");
                    $("#dropdown_ul").append(new_li);
                    var new_a = document.createElement ('a');
                    new_a.innerHTML = data.categoryList[i].name;
                    new_a.setAttribute("id", data.categoryList[i].id);
                    new_a.setAttribute("name", data.categoryList[i].name);
                    new_a.setAttribute("href", "#");
                    $("#li_"+data.categoryList[i].id).append(new_a);
                }
                if (i === 0 || i === 7)
                {
                    var li_div = document.createElement('li');
                    li_div.setAttribute("class", "divider");
                    $("#dropdown_ul").append(li_div);
                }


            }

            var new_li = document.createElement('li');
            new_li.setAttribute("id", "li_"+ data.categoryList[1].id);
            new_li.setAttribute("class", "li_cat");
            $("#dropdown_ul").append(new_li);
            var new_a = document.createElement ('a');
            new_a.innerHTML = data.categoryList[1].name;
            new_a.setAttribute("id", data.categoryList[1].id);
            new_a.setAttribute("name", data.categoryList[1].name);
            new_a.setAttribute("href", "#");
            $("#li_"+data.categoryList[1].id).append(new_a);

            var li_div = document.createElement('li');
            li_div.setAttribute("class", "divider");
            $("#dropdown_ul").append(li_div);

            for (var i = data.categoryList.length/2 + 1  ; i < data.categoryList.length ; i++)
            {
                var new_li = document.createElement('li');
                new_li.setAttribute("id", "li_"+ data.categoryList[i].id);
                new_li.setAttribute("class", "li_cat");
                $("#dropdown_ul").append(new_li);
                var new_a = document.createElement ('a');
                new_a.innerHTML = data.categoryList[i].name;
                new_a.setAttribute("id", data.categoryList[i].id);
                new_a.setAttribute("name", data.categoryList[i].name);
                new_a.setAttribute("href", "#");
                $("#li_"+data.categoryList[i].id).append(new_a);

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
                document.getElementById("select-button").childNodes[2].nodeValue = event.target.name;
                document.getElementById("cat").value = event.target.id;
                categry=event.target.id;


            });
            data.result = 0;
        }
    }


});

function product_add(){
    var namepr = document.getElementById("name-pr").value;
    var pricepr = document.getElementById("price-pr").value;
    var infopr = document.getElementById("info-pr").value;
    var x = document.getElementById("x1").value;//$('input[name="x1"]').value;
    var y = document.getElementById("y1").value;//$('input[name="y1"]').value;
    var w = document.getElementById("w").value;//$('input[name="w"]').value;
    var h = document.getElementById("h").value;//$('input[name="h"]').value;
    var img = document.getElementById("hidden-image").value;//$('input[name="image"]').value;
    if ((namepr=="") || (pricepr==0) || (infopr=="")  || (categry==undefined))
    {
        alert("لطفا تمام فیلدها را پر کنید!");
    }
    else{
        var picId;
        if (img ==0){
            alert("لطفا ابتدا قسمت مورد نظر از عکس را جدا کنید!")
        }else{
//            alert("here");
//            $("#my-add-form").ajaxSubmit();
            //                var postData = $(this).serializeArray();
//                var formURL = $(this).attr("action");
//                $.ajax(
//                    {
            $("#my-add-form").ajaxSubmit({

                        url : "submitProduct",
                        type: "POST",
//                        data : postData,
                        success:function(data, textStatus, jqXHR)
                        {
                            if (data.result == 0){
                                alert("result 0");
                            }else{
                                alert("محصول جدید با موفقیت در سیستم به ثبت رسید :)");
                                $("input").val('');
                                $(".my-submit").val('جداکردن عکس');
                                document.getElementById("select-button").childNodes[2].nodeValue = "انتخاب دسته";
                                document.getElementById("img-final").src = '';
                                document.getElementById("img-select").src = '';
                            }
                            //data: return data from server
                        },
                        error: function(jqXHR, textStatus, errorThrown)
                        {
                            alert("error!");
                            //if fails		alert
                        }
                    });
//                e.preventDefault();	//STOP default action
//            });
//            $("#my-add-form").submit();
//            var ajaxAddPro ={
//                "name": namepr,
//                "description": infopr,
//                "category":categry,
//                "price":pricepr,
//                "picURL":img,
//                "x": x,
//                "y": y,
//                "w": w,
//                "h": h
//            }
//            var urlAdd ="submitProduct";
//            $.ajax({
//                url: urlAdd,
//                type: 'get',
//                dataType: 'json',
//                data: ajaxAddPro,
//                success: function(data, status, xhr){
//                    if (data.result == 0){
//                        alert("error!");
//                    }else
//                    {
//                        alert("محصول جدید با موفقیت در سیستم به ثبت رسید :)");
//                        $("input").val('');
//                        $(".my-submit").val('جداکردن عکس');
//                        document.getElementById("select-button").childNodes[2].nodeValue = "انتخاب دسته";
//
//                    }
//                },
//                error: function(){
//                    alert("error!!");
//                }
//            });
        }

    }
}


image_id = 0;
function crop(){
    alert("inja");

    $("#imageForm").submit();
    alert("submited");
}