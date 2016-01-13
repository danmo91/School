$(function() {

  $('#search_form').ajaxForm(function(data){

    $('.items').html(data);

  }); // ajaxform

}); // ready
