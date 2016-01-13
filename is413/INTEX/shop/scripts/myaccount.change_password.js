$(function() {

  // set class attributes
  $('#id_old_password').addClass('form-control')
  $('#id_new_password').addClass('form-control')
  $('#id_reenter_password').addClass('form-control')

  $('#id_old_password').prop('placeholder','Old Password')
  $('#id_new_password').prop('placeholder','New Password')
  $('#id_reenter_password').prop('placeholder','Confirm Password')

  // submit form via ajax
  $('#change_password_form').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


}); // ready
