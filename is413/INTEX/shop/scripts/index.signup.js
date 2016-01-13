$(function() {

  // add classes to signup modal
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

  // submit form via ajax
  $('#signup_form').ajaxForm(function(data){
    $('#jquery-loadmodal-js-body').html(data);
  }); // ajaxform


}); // ready
