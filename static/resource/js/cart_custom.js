/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Custom Dropdown
4. Init Page Menu


******************************/

$(document).ready(function()
{
    jQuery("table#cart input[name=quantity]").change(function() {
        var _this = jQuery(this);
        var quantity = _this.val();
        var form = _this.closest("form");
        var closetTr = _this.closest("tr");
        var url = form.attr('action');
        var params = form.serialize();
        var unitPrice = form.attr('data-price');
        if (isNaN(quantity)) {
            alert("Please input number");
            _this.val("");

            return;
        }
        jQuery.ajax({
            url: url,
            dataType: 'json',
            type : 'post',
            data: params,
            beforeSend: function(){

            },
            success: function(data){
                if (data.success == true) {
                	console.log("Add to cart success");
                	console.log(data);
                	jQuery("span#total_item").text(data.total_item);
                	jQuery("span.total_price").text(data.total_price);
                    closetTr.find("span.item_price").text(unitPrice * quantity);
                }
            }
        });

    });
});