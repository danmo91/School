$(function() {


    // get username
    var username;

    $.ajax({
        url: '/homepage/index.get_username/',
        success: function(data) {
            console.log('data', data)

            var username = ""
            if('first_name' in data){
                username = data['first_name']
            }

            console.log('first name:', username)

            // notify- welcome to homepage
            $.notify({

              // options
              icon: 'glyphicon glyphicon-star',
              title: '<strong>Welcome </strong>' + '<strong>' + username + '</strong>',
              message: 'to the Colonial Heritage Foundation',

            },{

              // settings
              offset: {
                x: 50,
                y: 75,
              },
              animate: {
                enter: 'animated fadeInRight',
                exit: 'animated fadeOutRight'
              },
              delay: 2500,

            }); // notify
        }

    });





  // modal to view overdue rentals
  $('#show_overdue_rentals').on('click', function(){

    event.preventDefault()
    $.loadmodal({

      url:'/manager/rentals.overdue/',
      title: 'Overdue Rentals',
      width: '600px',
    }); // Loadmodal

  }); // Click


}); // Ready
