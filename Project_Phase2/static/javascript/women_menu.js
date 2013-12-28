var category_list = $('.women_list_item');

for (var i = 0; i < category_list.length; i++) {
	category_list[i].during_hover = 0;
	category_list[i].during_close = 0;
	category_list[i].start_width = $(category_list[i]).width();
	category_list[i].start_height = $(category_list[i]).height();
	category_list[i].start_left = document.getElementById('women_item_' + (i + 1)).style.left + 1;

}
//alert("didam ");
$('.women_list_item').hover(function() {

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
		}, 900, function() {
			(this).during_hover = 0;
		});

		this.childNodes[1].style.visibility = 'visible';
		$(this.childNodes[3]).fadeIn("1500");
		var menu = document.getElementsByClassName("men_menu")[0];
		menu.style.opacity = '0.3'
		// var middle2 = document.getElementsByClassName("middle")[0];
		// middle2.innerHTML = '';
		// var carousel = document.getElementById("myCarousel");
		// carousel.style.display='none';
		var menhidden = document.getElementsByClassName("men-hidden")[0];
        menhidden.style.WebkitTransition = '1.2s';
		menhidden.style.left = '860px';
		var middle = document.getElementsByClassName("middle")[0];
		middle.style.left = '860px';
		// middle.innerHTML ='';
		var men = document.getElementsByClassName("men")[0];
		men.children[0].style.opacity = '0.3';

        setTimeout(function(){
            menhidden.style.WebkitTransition = '1.7s';
        }, 1000);

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
		var men = document.getElementsByClassName("men")[0];
		men.children[0].style.opacity = '1';
		var menu = document.getElementsByClassName("men_menu")[0];
		menu.style.opacity = '1';
		var carousel = document.getElementById("myCarousel");
		carousel.style.display='visible';
		var middle = document.getElementsByClassName("middle")[0];
		middle.style.left = '545px';
		var menhidden = document.getElementsByClassName("men-hidden")[0];
		menhidden.style.left = '560px';
		// var middle2 = document.getElementsByClassName("middle")[0];
		// setTimeout(function(){
			// middle2.innerHTML = '<p id="trends">	trends</p><div class = "trend_pic"><div id="myCarousel" class="carousel slide vertical"><ol class="carousel-indicators" style="top:0%"><li data-target="#myCarousel" data-slide-to="0" class="active"></li><li data-target="#myCarousel" data-slide-to="1"></li><li data-target="#myCarousel" data-slide-to="2"></li><li data-target="#myCarousel" data-slide-to="3"></li></ol>	<!-- Carousel items -->	<div class="carousel-inner "><div class="active item"><img src="static/images/watch men.jpg" class="carousel-img"><p class="carsoul-detail">Hamilton Watch, Mens Swiss Automatic Chronograph Jazzmaster<br/><br/>$1,445</p></div><div class="item"><img src="static/images/jewlry.jpg" class="carousel-img"><p class="carsoul-detail">Pearl and Crystal Floral Bridal Jewelry Set<br/><br/>	$27,325	</p></div><div class="item"><img src="static/images/6.jpg" class="carousel-img"><p class="carsoul-detail">Aero Blue, High Platform, High Heel Shoes<br/><br/>$96.62</p></div><div class="item"><img src="static/images/perfume3.jpg" class="carousel-img"><p class="carsoul-detail">Gucci Guilty Intense by Gucci for Women 2.5 oz EDP Spray<br/><br/>$102</p></div></div><!-- Carousel nav --><a class="carousel-control left my_left" href="#myCarousel" data-slide="prev" style="top:0%; left:43%">&lsaquo;</a><a class="carousel-control right my_right" href="#myCarousel" data-slide="next"style="top:100%; left:41%">&rsaquo;</a></div></div>';
			// }, 1000); 
		// }

		$(this.childNodes[3]).fadeOut("1500");
		$(this.childNodes[1]).fadeIn("1500", function() {
			$(this.childNodes[1]).display = 'visible';
		});
	}
}); 