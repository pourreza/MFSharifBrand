var category_list = $('.men_list_item');

for (var i = 0; i < category_list.length; i++) {
    category_list[i].during_hover = 0;
    category_list[i].during_close = 0;
    category_list[i].start_width = $(category_list[i]).width();
    category_list[i].start_height = $(category_list[i]).height();
    category_list[i].start_left = document.getElementById('men_item_' + (i + 1)).style.left - 1;
}

$('.men_list_item').hover(function() {

    if ((this).during_hover === 0) {
        if (this.during_close !== 0) {
            $(this).stop();
            this.during_close = 0;
        }

        (this).during_hover = 1;
        $(this).animate({
            left : this.start_left * 40,
            width : this.start_width * 1.5,
            height : this.start_height * 5
        }, 1500, function() {
            (this).during_hover = 0;
        });
        var middle = document.getElementsByClassName("middle")[0];
        middle.innerHTML = '';
        middle.style.width = '0px';
        var menu = document.getElementsByClassName("women_menu")[0];
        menu.style.opacity = '0.3';
        var men = document.getElementsByClassName("women")[0];
        men.children[0].style.opacity = '0.3';

        this.childNodes[1].style.visibility = 'visible';
        $(this.childNodes[3]).fadeIn("1500");

    }
}, function() {

    if (this.during_close === 0) {
        if (this.during_hover !== 0) {
            $(this).stop();
            this.during_hover = 0;
        }
        this.during_close = 1;
        $(this).animate({
            left : this.start_left,
            width : this.start_width,
            height : this.start_height
        }, 1500, function() {
            this.during_close = 0;
        });

        var p_arrays = document.getElementsByTagName('p');

        $(this.childNodes[3]).fadeOut("1500");
        $(this.childNodes[1]).fadeIn("1500", function() {
            $(this.childNodes[1]).display = 'visible';
        });


        var men = document.getElementsByClassName("women")[0];
        men.children[0].style.opacity = '1';
        var menu = document.getElementsByClassName("women_menu")[0];
        menu.style.opacity = '1';

        var middle = document.getElementsByClassName("middle")[0];
        middle.style.width = '300px';
        // $('.middle').
        if (this.during_hover === 0) {
            setTimeout(function(){
                middle.innerHTML = '<p id="trends">                محصولات پرطرفدار</p><div class = "trend_pic"><div id="myCarousel" class="carousel slide vertical"><ol class="carousel-indicators" style="top:0%"><li data-target="#myCarousel" data-slide-to="0" class="active"></li><li data-target="#myCarousel" data-slide-to="1"></li><li data-target="#myCarousel" data-slide-to="2"></li><li data-target="#myCarousel" data-slide-to="3"></li></ol><!-- Carousel items --><div class="carousel-inner "><div class="active item"><img src="static/images/watch%20men.jpg" class="carousel-img" ><p dir="rtl" class="carsoul-detail">ساعت همیلتون، ساخته شده در کشور سوئیس، وارد کننده: علی خردمند<br/><br/>3,250,000 تومان<br/><br/><a href="ProductDetail.html" class="btn-mini add-cart"> مشخصات محصول</a></p></div><div class="item"><img src="static/images/jewlry.jpg" class="carousel-img"><p dir="rtl" class="carsoul-detail">برای آنان که قصد عروسی دارند!!<br/>ست مرواریدبا تخفیفی باورنکردنی<br/><br/>50365000تومان<br/><br/><a href="ProductDetail.html"  class="btn-mini add-cart"> مشخصات محصول</a></p></div><div class="item"><img src="static/images/6.jpg" class="carousel-img"><p dir="rtl" class="carsoul-detail">بگذارید راز بلندی قد شما همیشه بین خودتان و کفشتان بماند!!<br/>کفش‌های پاشنه بلند ایرو بلو<br/>265000 تومان<br/><br/><a href="ProductDetail.html"  class="btn-mini add-cart"> مشخصات محصول</a></p></div> <div class="item"><img src="static/images/perfume3.jpg" class="carousel-img"><p dir="rtl" class="carsoul-detail">عطر گوچی 100 میلی لیتری مناسب برای خانم ها در تمامی سنین<br/><br/>325000 تومان<br/><br/><a  href="ProductDetail.html"  class="btn-mini add-cart"> مشخصات محصول</a></p></div></div><!-- Carousel nav --><a class="carousel-control left my_left" href="#myCarousel" data-slide="prev" style="top:0%; left:43%">&lsaquo;</a><a class="carousel-control right my_right" href="#myCarousel" data-slide="next"style="top:100%; left:41%">&rsaquo;</a><div></div>';
            }, 1000);
        }

    }
}); 