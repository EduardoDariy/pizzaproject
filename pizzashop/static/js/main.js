$(document).ready(function () {
    // orderForm
    var orderForm = $('#order-form');
    orderForm.on('submit', function (e) {
        e.preventDefault();
        var count = $('#count').val();
        var submitBtn = $('#submit-btn');
        var itemId = submitBtn.data('item_id');
        var itemName = submitBtn.data('name');
        var itemPrice = submitBtn.data('price');
        console.log(itemId + ' ' + itemName + ' ' + itemPrice);



        var data = {};
        data.itemId = itemId;
        data.count = count;
        var csrf_token = $('#order-form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = orderForm.attr('action');

        console.log(data);
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");

             },
             error: function(){
                 console.log("error")
             }
         });



        $('.basket__ul').append('<li class="basket__item">' + itemName + ' ' + count + ' ' + 'шт. ' + (itemPrice * count) + ' руб. '
            + '<a class="delete-item" href="">x</a>' + '</li>');

    });



    $('.basket__text').on('click', function (e) {
        e.preventDefault();
        $('.basket').toggleClass('hidden');
    });

    $(document).on('click',  '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    });
});