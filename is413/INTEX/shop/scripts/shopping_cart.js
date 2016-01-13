$(function() {


    $('.modal-content').prop('data-backdrop','false')
    $('.modal-content').prop('z-index','1020')

  // Delete from cart
  $('.delete_from_cart').on('click', function() {

    var id = $(this).attr('data-id');
    var product = $(this).attr('data-product');

    $.loadmodal({

      url: '/shop/shopping_cart.delete/' + id + '/' + product,
      title: 'Shopping Cart',
      width: '800px',
      buttons: {
        "Checkout": function() {
          // do something here
          window.location.href = "/shop/checkout/";
          // a false return here cancels the automatic closing of the dialog
        },
      },
      onShow: function(dlg) {
        $('.button-panel').find('.btn').addClass('pull-right btn-warning')
        $('.button-panel').css({height: "60px"})
        $('.modal-content').modal("show")
        $('.modal-content').css('z-index','1020')
      },

    }); // loadmodal

  }); // click

}); // ready
