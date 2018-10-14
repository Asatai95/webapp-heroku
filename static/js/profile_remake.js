$(function() {
  $("input[name='email']").keyup(function() {
    if (!$('#email_text').val().match(/^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i)) {
      $('.error').text('正しいメールアドレスを入力してください。')
      return false;
    } else {
      $('.error').text('')
      return false;
    }
  });
  if ($('#comment_text').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');

  } else if ($('#email_text').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#name_text').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  }

  $('#comment_text').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 1) {
      $('#submit').removeAttr('disabled');
    } else {
      $('#submit').attr('disabled', 'disabled');
    }
  });


});
