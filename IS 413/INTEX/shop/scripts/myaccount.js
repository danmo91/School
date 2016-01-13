$(function() {

  // Edit User
  $('#edit_user_modal').on('click', function(){

    event.preventDefault();
    $.loadmodal({
      url: '/shop/myaccount.edit/',
      title: 'Edit',
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

  }); // Click


  $('#editform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxForm


  // Change password
  $('#change_password_modal').on('click', function(){

    event.preventDefault();

    $.loadmodal({

      url: '/shop/myaccount.change_password/',
      title: 'Change Password',
      width: '500px',
      ajax: {
            success: function() {

              $('#id_old_password').addClass('form-control')
              $('#id_new_password').addClass('form-control')
              $('#id_reenter_password').addClass('form-control')

              $('#id_old_password').prop('placeholder','Old Password')
              $('#id_new_password').prop('placeholder','New Password')
              $('#id_reenter_password').prop('placeholder','Confirm Password')



            },//
            // any other options from the regular $.ajax call (see JQuery docs)
          },

    }); // loadmodal

  }); // Click


  $('#change_password_form').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


  // Login
  $('#show_login_modal').on('click', function(){

    event.preventDefault();

    $.loadmodal('/homepage/index.loginform/')


  }); // click


}); // ready
