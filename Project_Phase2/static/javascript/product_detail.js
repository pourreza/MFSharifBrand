function add(pk) {
    var comment = document.getElementById('newComment');
    var urlNewComment = "../addComment";
    var ajaxNewComment = {
        "message": comment.value,
        "name": 'ذوالفقار',
        "pro_id": pk
    }
    $.ajax({
        url: urlNewComment,
        type: 'get',
        dataType: 'json',
        data: ajaxNewComment,
        success: function (data, status, xhr) {
            if (data.result == 0) {
                alert("ajax error!");
            } else {
                var com = document.getElementById("prev-comments");
                com.innerHTML = "";
                for (var cm=0; cm< data.comments.length; cm++){
                    com.innerHTML +='<li>'+data.names[cm]+':'+data.comments[cm]+'<p>تاریخ:'+data.dates[cm]+'</p></li>';
                }
            }
        },
        error:function(){
            alert("ajax error!");
        }
        // ...
    });
    document.getElementById('newComment').value="";
}
