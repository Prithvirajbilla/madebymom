$(".btn-number").click(
		function  () {
			var type_of_button = $(this).data("type");
			var quant = $(this).data("number");
			var id = "#"+$(this).data("id");
			if(type_of_button == "minus")
			{
				quant -= 1;
				if(quant < 1)
				{
					quant = 0;
					$(id+"  .rating-box").hide()
				}
				else
				{

					$(id+" .rating-box").show();
					$(id+ " .rating-box").text(quant);
					$(id+ " .btn-number").data("number",quant);
				}
			}
			else if(type_of_button == "plus")
			{
				quant+=1;
				if(quant > 10)
				{
					//
				}
				else
				{
					$(id+ " .rating-box").show();
					$(id+ " .rating-box").text(quant);
					$(id+ " .btn-number").data("number",quant);
				}
			}
		}

	)