$(function() {
  $("input[name='log_id']").keyup(function(){
    if(!$('#text').val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)){
       $('.error').text('正しいメールアドレスを入力してください。')
       $('.ma').css('margin-bottom', '0');
       return false;
    } else {
      $('.error').text('')
      $('.ma').css('margin-bottom', '25px');
      return false;
    }
  });
  if ( $('#text').val().length == 0 ) {
    $('#submit').attr('disabled', 'disabled');

  } else if ( $('#passwd').val().length == 0 ) {
    $('#submit').attr('disabled', 'disabled');
  }
  $('#passwd').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 6 ) {
      $('#submit').removeAttr('disabled');
    } else {
      $('#submit').attr('disabled', 'disabled');
    }
  });
  $('#text').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 6 ) {
      $('#submit').attr('disabled', 'disabled');

    }
  });
});

// $(function() {
//   if ( $('#passwd').val().length == 0 ) {
//     $('#submit').attr('disabled', 'disabled');
//   }
//   $('#passwd').bind('keydown keyup keypress change', function() {
//     if ( $(this).val().length > 0 ) {
//       $('#submit').removeAttr('disabled');
//     } else {
//       $('#submit').attr('disabled', 'disabled');
//     }
//   });
// });
