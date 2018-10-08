$(function() {
 if ($('#email').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#email').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  }

  $("#email").keyup(function() {
    if (!$('#email').val().match(/^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i)) {
      $('#submit').attr('disabled', 'disabled');
      $('.error').text('正しいメールアドレスを入力してください。')
    } else {
      $('#submit').removeAttr('disabled');
      $('.error').text('')
    }
  });
});


$(function (){
  $('#email').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.email').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.email').removeClass('input--filled');
    }
  });
});
