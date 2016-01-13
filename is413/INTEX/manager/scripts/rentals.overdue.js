$(function() {

    // send email to users with overdue rentals
    $('.email_button').on('click', function(){

        // 30, 60, or 90 days overdue
        var batch = $(this).attr('data-id')

        // send email via ajax
        $.ajax({url: "/manager/return.send_email/" + batch, success: function(result){
            // if email is sent
            if(result == "1"){

                // notify
                $.notify({
                      // options
                      icon: 'glyphicon glyphicon-star',
                      title: '<strong>Overdue Emails:</strong>',
                      message: 'Sent',
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

            // email failed
            else {
                // notify
                $.notify({
                      // options
                      icon: 'glyphicon glyphicon-star',
                      title: '<strong>Overdue Emails:</strong>',
                      message: 'Failed',
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
        }}); // ajax

    }); // email_button

}); // Ready
