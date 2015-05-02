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
		if(txt >=  10)
		{
			txt = 10;
			//changing the price
			$.notify("You cannot order more than 10 items of the same type!.To Bulk order, Contact us", "warn");
			$(this).val(txt);
			var cart_basket = JSON.parse($.cookie("cart_basket"));
			cart_basket["#"+id] = txt;
			$.cookie("cart_basket",JSON.stringify(cart_basket));
		}
		console.log(id);
		var price = $("#"+id+"-table .price").text();
		price = parseInt(price.substring(2));
		$("#"+id+"-table .total_price").text("₹ "+price*txt);

		console.log(txt);

		find_total();
	}
);