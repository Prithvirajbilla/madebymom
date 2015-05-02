var items_count = 0;
var cart_basket = {};
$( document ).ready(function() {
	if(typeof $.cookie('cart_basket') === 'undefined')
	{
		//no cookie

	}
	else
	{
		cart_basket = JSON.parse($.cookie('cart_basket'));
		console.log(cart_basket);
		items_count = Object.keys(cart_basket).length;
		for (var key in cart_basket)
		{
			var id = key;
			var number =  cart_basket[key];
			if(number > 0)
			{
				cart_basket[id] = number;
				$(id+"  .rating-box").show();
				$(id+ " .rating-box").text(number);
				$(id+" .btn-number").data("number",number);
			}
			else
				items_count-=1;
		}
		if(items_count > 0)
		{
			$("#cart_count").text(items_count);
			$("#cart_count").show();
		}


	}

	var total_price = 0;
	console.log(total_price);
	$(".total_price").each(
		function()
		{
			var txt = $(this).text();
			total_price+= parseInt(txt.substring(2));
		}
	);
	$("#cart-price").text("₹ "+total_price);
})



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
				if(quant != 0)
					cart_basket[id] =quant;
				else
					delete cart_basket[id];
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
				var pay = quant+1;
				var url = "/check_order/"+$(this).data("id")+"/"+pay;
				$.get(url,function(data){
					if(data["result"])
					{
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
					else
					{
						$.notify("only "+quant+" left in the store", "warn");

					}
				},"json");
			}
		}

	)