$(function() {

  // submit return form via ajax
  $('#returnform').ajaxForm(function(data){
    $('#jquery-loadmodal-js-body').html(data);
  }); // ajaxform

  // load bootstrap switch
  $(".my-checkbox").bootstrapSwitch({
      size: 'small',
  }); // bootstrap switch

  // load bootstrap selectpicker
  $('.selectpicker').selectpicker();

}); // Ready
