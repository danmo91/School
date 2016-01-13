$(function() {

    // show login modal
  $('#show_login_modal').on('click', function(){
    event.preventDefault()

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

            },
            // any other options from the regular $.ajax call (see JQuery docs)
          },
    }); // loadmodal
  }); // Click

  // submit login form via ajax
  $('#loginform').ajaxForm(function(data){
    $('#jquery-loadmodal-js-body').html(data);
  }); // ajaxForm

}); // Ready
