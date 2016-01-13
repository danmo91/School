$(function() {

  // load data-table
  $('#data-table').DataTable();


  // overdue rentals
  $('#show_overdue_rentals').on('click', function(){

    event.preventDefault();
    $.loadmodal({

      url:'/manager/rentals.overdue/',
      title: 'Overdue Rentals',
      width: '600px',
    }); // Loadmodal

  }); // Click


  // Rental Return
  $('.return').on('click', function(){

      event.preventDefault();

      // get rental id
      id = $(this).attr('data-id');

      $.loadmodal({
          url:'/manager/return.return_form/' + id,
          title:'Return',
          width: '600px',
      }); //Loadmodal

  }); // click

  // Submit return form
  $('#returnform').ajaxForm(function(data){
    $('#jquery-loadmodal-js-body').html(data);
  }); // ajaxform

}); // Ready
