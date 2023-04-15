/*$(document).ready(function () {
    
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(ice_value,10);
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if (value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
});
*/
$(document).ready(function() {

    var form = $('#quantity-update-form');
    var quantityField = $('#id_quantity');
    var incrementButton = $('#increment-quantity');
    var decrementButton = $('#decrement-quantity');

    
    incrementButton.click(function() {
        var quantity = parseInt(quantityField.val());
        if (quantity < 10) {
            quantity++;
            quantityField.val(quantity);
            
        }
    });

    decrementButton.click(function() {
        var quantity = parseInt(quantityField.val());
        if (quantity > 1) {
            quantity--;
            quantityField.val(quantity);
            
        }
    });
    
    
});