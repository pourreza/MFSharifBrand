
var url = "http://webproject.roohy.me/ajax/2/m&f/category/list";
var categry;
console.log("umad in tu");
$.ajax({
    url: url,
    type: 'post',
    dataType: 'json',
    success: function(data, status, xhr){
        if (data.result == 0){
            // Request error
        }else
        {

            for (var i = 0  ; i < data.categoryList.length ; i++)
            {
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
                document.getElementById("select-button").childNodes[2].nodeValue = event.target.name;
                categry=event.target.id;

            });

        }
    },


});


function product_add(){
    var namepr = document.getElementById("name-pr").value;
    var pricepr = document.getElementById("price-pr").value;
    var infopr = document.getElementById("info-pr").value;
    var imgpr = document.getElementById("pro-img").value;
//    alert();
    if ((namepr=="") || (pricepr==0) || (infopr=="")  || (categry==undefined)|| (imgpr=="")){
        alert("لطفا تمام فیلدها را پر کنید!");
    }
    else{
        var picId;
        $("#imageForm").ajaxSubmit({
            url: "http://webproject.roohy.me/ajax/2/m&f/product/uploadimage",
            type: "POST",
            dataType: 'json',
            data:'',
            success: function(data, status, xhr){
                console.log(data);
                if (data.result == 0){
                    // Request error
                }else
                {
                    picId = data.picId;
//                    alert("image load");
                    document.getElementById("img-select").src = data.picUrl;
                    document.getElementById("img-final").src = data.picUrl;
//                    $("img-select").attr("src", data.picUrl);
                }

            }
            // ...
        });
////////////////////////////////// inja bayad crop inaa check she ///////////

        $('#img-select').imgAreaSelect({ aspectRatio: '1:1', onSelectChange: preview });

        var ajaxAddPro ={
            "name": namepr,
            "description": infopr,
            "category":categry,
            "price":pricepr,
            "picId":picId,
            "x": 10,
            "y": 10,
            "w": 100,
            "h": 100
        }
        var urlAdd ="http://webproject.roohy.me/ajax/2/m&f/product/add";
        $.ajax({
            url: url,
            type: 'post',
            dataType: 'json',
            success: function(data, status, xhr){
                if (data.result == 0){
                }else
                {
                    alert("محصول جدید با موفقیت در سیستم به ثبت رسید :)");
                    $("input").val('');

                    document.getElementById("select-button").childNodes[2].nodeValue = "انتخاب دسته";

                }
            }
        });
    }}

function preview(img, selection) {
    var scaleX = 100 / (selection.width || 1);
    var scaleY = 100 / (selection.height || 1);

    $('#img-final').css({
        width: Math.round(scaleX * 400) + 'px',
        height: Math.round(scaleY * 300) + 'px',
        marginLeft: '-' + Math.round(scaleX * selection.x1) + 'px',
        marginTop: '-' + Math.round(scaleY * selection.y1) + 'px'
    });
}