$(function() {

  // submit form via ajax
  $('#editform').ajaxForm(function(data){

    $('#jquery-loadmodal-js-body').html(data);

  }); // ajaxform


}); // ready
