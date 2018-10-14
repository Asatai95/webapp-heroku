$(function() {
  $(document).on('click', function(e) {

    if (!$(e.target).closest('.main_text').length && !$(e.target).closest('.login_sub').length) {

      $('.main_text').animate({
        'opacity': '0'
      }, 500);
      $('div.back').css('position', 'inherit');
      $('.main_text').animate({
        'top': '0'
      }, 500);


    } else if ($(e.target).closest('.login_sub').length) {

      if ($('.main_text').css('opacity') == 0) {
        $('.main_text').animate({
          'top': '100px'
        }, 500);
        $('.main_text').css('opacity', '1.0');
        $('div.back').css('background-color', 'rgba(0,0,0,.5)');
        $('div.back').css('position', 'relative');
      } else {
        $('.main_text').animate({
          'top': '0'
        }, 500);
        $('.main_text').animate({
          'opacity': '0'
        }, 500);
        $('div.back').css('position', 'inherit');
      }
    }

  });
});

$(function() {
  $("input[name='log_id']").keyup(function() {
    if (!$('#text').val().match(/^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i)) {
      $('.error').text('正しいメールアドレスを入力してください。')
      $('.ma').css('margin-bottom', '15px');
      return false;
    } else {
      $('.error').text('')
      $('.ma').css('margin-bottom', '15px');
      return false;
    }
  });
  if ($('#text').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');

  } else if ($('#passwd').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  } else if ($('#user_name').val().length == 0) {
    $('#submit').attr('disabled', 'disabled');
  }

  $('#passwd').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 6) {
      $('#submit').removeAttr('disabled');
    } else {
      $('#submit').attr('disabled', 'disabled');
    }
  });
  $('#text').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 6) {
      $('#submit').attr('disabled', 'disabled');

    }
  });

});
