$(function() {
  $("input[name='email']").keyup(function(){
    if(!$('#email').val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)){
       $('.error').text('正しいメールアドレスを入力してください。');
       return false;
    } else {
      $('.error').text('');
      return false;
    }
  });

  if ($('#name').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#email').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#passwd').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');

  }

  $('#passwd').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 6 ) {
      $('#submit').removeAttr('disabled');
      $('.error').text('');
    } else if ($(this).val().match(/^[A-Za-z0-9]*$/) && $(this).val().length < 6) {
      $('#submit').attr('disabled', 'disabled');
      $('.error').text('パスワードは半角英数字、６文字以上で設定してください。')
    }
  });
  $('#email').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('#submit').attr('disabled', 'disabled');
    }
  });
  $('#name').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('#submit').attr('disabled', 'disabled');
    }
  });
});


$(function (){
  $('#name').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.name').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.name').removeClass('input--filled');
    }
  });
  $('#email').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.email').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.email').removeClass('input--filled');
    }
  });
  $('#passwd').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 0 ) {
      $('.input__label-content--hoshi.password').addClass('input--filled');
    } else {
      $('.input__label-content--hoshi.password').removeClass('input--filled');
    }
  });
});
