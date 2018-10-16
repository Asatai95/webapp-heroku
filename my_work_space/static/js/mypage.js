$(function() {
  $(document).on('click', function(e) {

    if (!$(e.target).closest('.check_main').length && !$(e.target).closest('.button_delete').length) {

      $('.check_main').animate({
        'opacity': '0'
      }, 800);
      $('.check_main').animate({
        'top': '0'
      }, 800);
    } else if ($(e.target).closest('.button_delete').length) {

      if ($('.check_main').css('opacity') == 0) {
        $('.check_main').animate({
          'top': '200px'
        }, 800);
        $('.check_main').css('opacity', '1.0');
      } else {
        $('.check_main').animate({
          'top': '0'
        }, 800);
        $('.check_main').animate({
          'opacity': '0'
        }, 800);
      }
    }
  });
});


// $(function() {
//   $(document).on('click', function(e) {
//
//     if (!$(e.target).closest('.box').length && !$(e.target).closest('button[name=submit]').length) {
//       $('.box').fadeOut(500);
//     } else if ($(e.target).closest('button[name=submit]').length) {
//       if ($('.box').css('display') == 'none') {
//         $('.box').fadeIn(100);
//         $('.check_main').animate({
//           'opacity': '0'
//         }, 100);
//         $('.check_main').animate({
//           'top': '0'
//         }, 100);
//       } else {
//         $('.box').fadeOut(800);
//       }
//     }
//   });
// });

$(function() {
  $("input[name='email']").keyup(function() {
    if (!$('#email').val().match(/^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/i)) {
      $('.error_text').text('正しいメールアドレスを入力してください。');
      return false;
    } else {
      $('.error_text').text('');
      return false;
    }
  });
  if ($('#password').val().length == 0) {
    $('#button').attr('disabled', 'disabled');
  } else if ($('#email').val().length == 0) {
    $('#button').attr('disabled', 'disabled');
  }
  $('#email').bind('keydown keyup keypress change', function() {
    if ($(this).val().length < 6) {
      $('#button').attr('disabled', 'disabled');
    }
  });
  $('#password').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 6) {
      $('.error_text').text('');
      $('#button').removeAttr('disabled');
    } else {
      $('.error_text').text('パスワードは６文字以上です。');
      $('#button').attr('disabled', 'disabled');
    }
  });
});
