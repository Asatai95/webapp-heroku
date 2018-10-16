$(function() {
 if ($('#passwd1').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#passwd1').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  }

  $('#passwd1').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 6 ) {
      $('.error').text('');
    } else if ($(this).val().match(/^[A-Za-z0-9]*$/) && $(this).val().length < 6) {
      $('#submit').attr('disabled', 'disabled');
      $('.error').text('パスワードは半角英数字、６文字以上で設定してください。')
    }
  });
  $('#passwd2').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 6 ) {
      $('#submit').removeAttr('disabled');
    }
  });
});

$(function (){
  $('#passwd1').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.password.1').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.password.1').removeClass('input--filled');
    }
  });
  $('#passwd2').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.password.2').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.password.2').removeClass('input--filled');
    }
  });
});
