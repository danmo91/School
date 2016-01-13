$(function() {

    // submits forgot password form via ajax
  $('#forgot_password_form').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform

}); // Ready
