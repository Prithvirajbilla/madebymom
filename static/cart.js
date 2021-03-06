function find_total () {
	var total_price = 0;
	$(".total_price").each(
		function()
		{
			var txt = $(this).text();
			total_price+= parseInt(txt.substring(2));
		}
	);
	$("#cart-price").text("₹ "+total_price);
}

$(".remove").click(
function()
{

	var items_count = $("#cart_count").text();
	if(items_count == 1)
	{
		$("table").remove();
		$("#empty-cart").show();

	}
	//items count at the top
	items_count-=1;
	
	if(items_count == 0)
		$("#cart_count").hide();
	
	$("#cart_count").text(items_count);
	
	var id = $(this).data("id");
	$("#"+id+"-table").remove();
	
	//total price
	find_total();

	//deleting the cart basker
	var cart_basket = JSON.parse($.cookie('cart_basket'));
	delete cart_basket["#"+id];
	$.cookie('cart_basket',JSON.stringify(cart_basket));
}
);


$(".quantity").on("input",
	function ()
	{
		var id = $(this).data("id");
		var txt = $(this).val();
		console.log(txt);
		if(txt <= 10)
		{
			var url = "/check_order/"+$(this).data("id")+"/"+txt;
			$.get(url,function(data){

				if(data["result"])
				{
					if(txt >=  10)
					{
						txt = 10;
						//changing the price
						$.notify("You cannot order more than 10 items of the same type!.To Bulk order, Contact us", "warn");
						$("#"+id+"-table .total_price").val(txt);
						var cart_basket = JSON.parse($.cookie("cart_basket"));
						cart_basket["#"+id] = txt;
						$.cookie("cart_basket",JSON.stringify(cart_basket));
					}
					var price = $("#"+id+"-table .price").text();
					price = parseInt(price.substring(2));
					txt = $("#"+id+"-table .quantity").val();
					$("#"+id+"-table .total_price").text("₹ "+price*txt);

					find_total();
				}
				else
				{
					var txt = parseInt(data["quantity"]);
					$("#"+id+"-table .quantity").val(txt);
					$.notify("Only "+data["quantity"]+" left in the store", "warn");

					var price = $("#"+id+"-table .price").text();
					price = parseInt(price.substring(2));
					$("#"+id+"-table .total_price").text("₹ "+price*data["quantity"]);

					find_total();

				}



			},"json");
		}
		else
		{
			console.log("text");
			txt = 10;
			//changing the price
			$.notify("You cannot order more than 10 items of the same type!.To Bulk order, Contact us", "warn");
			$("#"+id+"-table .total_price").val(txt);
			var cart_basket = JSON.parse($.cookie("cart_basket"));
			cart_basket["#"+id] = txt;
			$.cookie("cart_basket",JSON.stringify(cart_basket));
		}

	}
);

$(".place_order").click(function()
{
	$(this).attr("disabled",true);
	$(".checkout").show();
	$("html, body").animate({ scrollTop: $(document).height()-$(window).height() });
});