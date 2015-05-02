var items_count = 0;
$( document ).ready(function() {
	if(typeof $.cookie('cart_basket') === 'undefined')
	{
		//no cookie

	}
	else
	{
		var cart_basket = JSON.parse($.cookie('cart_basket'));
		items_count = Object.keys(cart_basket).length;
		$("#cart_count").text(items_count);
		$("#cart_count").show();
		for (var key in cart_basket)
		{
			var id = key;
			var number =  cart_basket[key];
			if(number > 0)
			{		
				$(id+"  .rating-box").show();
				$(id+ " .rating-box").text(number);
				$(id+" .btn-number").data("number",number);
			}		
		}

	}


})


var cart_basket = {};

$(".btn-number").click(
		function  () {
			var type_of_button = $(this).data("type");
			var quant = $(this).data("number");
			var id = "#"+$(this).data("id");
			if(type_of_button == "minus")
			{
				
				$(id+" .btn-number[data-type='plus']").removeAttr("disabled");

				quant -= 1;
				if(quant == 0)
				{
					items_count-=1;
					if(items_count <= 0)
					{
						items_count=0;
						$("#cart_count").hide();
					}
					else
					{
						$("#cart_count").show();
						$("#cart_count").text(items_count);
					}
				}

				if(quant < 1)
				{
					quant = 0;
					$(id+"  .rating-box").hide()
					$(id+ " .btn-number").data("number",quant);
					$(id+" .btn-number[data-type='plus']").data("number",quant);
				}
				else
				{

					$(id+" .rating-box").show();
					$(id+ " .rating-box").text(quant);
					$(id+ " .btn-number").data("number",quant);
				}
				cart_basket[id] =quant;
				$.cookie("cart_basket",JSON.stringify(cart_basket));
			}
			else if(type_of_button == "plus")
			{

				if(quant == 0)
				{
					items_count+=1;
					$("#cart_count").show();
					$("#cart_count").text(items_count);
				}

				quant+=1;
				if(quant > 10)
				{
					$.notify("You cannot order more than 10 items of the same type!.To Bulk order, Contact us", "warn");
					$(this).attr("disabled",true);
					quant-=1;
				}
				else
				{
					$(id+ " .rating-box").show();
					$(id+ " .rating-box").text(quant);
					$(id+ " .btn-number").data("number",quant);
				}
				cart_basket[id] = quant;
				$.cookie("cart_basket",JSON.stringify(cart_basket));
			}
		}

	)