$(function() {

  // Login
  $('#show_login_modal').on('click', function(){

    event.preventDefault();
    $.loadmodal({
      url: '/homepage/index.loginform/',
      title: 'Login',
      width: '500px',
      ajax: {
            success: function() {

              $('#id_username').addClass('form-control')
              $('#id_password').addClass('form-control')
              $('#id_username').prop('placeholder','Username')
              $('#id_password').prop('placeholder','Password')

            },//
            // any other options from the regular $.ajax call (see JQuery docs)
          },
    }); // loadmodal

  }); // click


  // Show cart
  $('#show_cart').on('click', function(){

    event.preventDefault();

    $.loadmodal({
      url: '/shop/shopping_cart/',
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
    }); // load modal
  }); // click


  // Signup
  $('#show_signup_modal').on('click', function(){

    event.preventDefault();

    console.log('clicked');

    $.loadmodal({

      url: '/shop/index.signup/',
      title: 'Signup',
      width: '500px',
      ajax: {
            success: function() {

              $('#id_username').addClass('form-control')
              $('#id_password').addClass('form-control')
              $('#id_first_name').addClass('form-control')
              $('#id_last_name').addClass('form-control')
              $('#id_email').addClass('form-control')
              $('#id_phone').addClass('form-control')

              $('#id_username').prop('placeholder','Username')
              $('#id_password').prop('placeholder','Password')
              $('#id_first_name').prop('placeholder','First Name')
              $('#id_last_name').prop('placeholder','Last Name')
              $('#id_email').prop('placeholder','Email')
              $('#id_phone').prop('placeholder','Phone')



            },//
            // any other options from the regular $.ajax call (see JQuery docs)
          },
    });

  }); // click


  $('#signup_form').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


  // add to cart
  $('.add_to_cart').on('click', function(){

    var product
    var qty
    var id

    // item or product?
    if($(this).attr('data-product') === 'False') {

      // it is a rental item
      product = false

      // default 1, for items
      qty = 1

    }
    else {

      // it is a online sale product
      product = true

      // get qty
      qty = $('#quantity').val();

      if(! qty)
      {
        qty = 1
      };

    }


    // get id
    id = $(this).attr('data-id');

    $.loadmodal({

      url: '/shop/shopping_cart.add/' + id + '/' + qty + '/' + product,
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
      },


    });

  }); // Click


  // Delete from cart
  $('.delete_from_cart').on('click', function() {

    var product = $(this).attr('data-product');
    var id = $(this).attr('data-id');

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
      },
    }); // loadmodal
  }); // click


  // Search
  $('#search').on('click', function(){

    var input = $('#search_input').val()
    var options = {
      data:{

        'input': input,

      },
      success: function(data) {

        $('.items').html(data)
      },

    }

    $('#search_form').ajaxForm(options);

  }); // click

}); // ready
