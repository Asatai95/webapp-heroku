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
    if (!$('#text').val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)) {
      $('.error').text('正しいメールアドレスを入力してください。')
      $('.ma').css('margin-bottom', '0');
      return false;
    } else {
      $('.error').text('')
      $('.ma').css('margin-bottom', '25px');
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

$(function() {
  $(document).on('click', function(e) {

    if (!$(e.target).closest('.main_create').length && !$(e.target).closest('#new').length) {

      $('.main_create').fadeOut(500);
      $('div.back_create').css('position', 'inherit');
      $('.main_create').animate({
        'top': '0'
      }, 500);
      $('div.back_create').css('width', '0');
      $('div.back_create').css('height', '0');
      $('div.back').css('width', '100%');
      $('div.back').css('height', '735px');

    } else if ($(e.target).closest('#new').length) {

      if ($('.main_create').css('display') == 'none') {
        $('.main_create').animate({
          'top': '100px'
        }, 800);
        $('.main_create').fadeIn(500);
        $('div.back_create').css('background-color', 'rgba(0,0,0,.5)');
        $('div.back_create').css('position', 'relative');
        $('div.back_create').css('width', '100%');
        $('div.back_create').css('height', '735px');
        $('div.back').css('width', '0');
        $('div.back').css('height', '0');
        $('.main_text').animate({
          'opacity': '0'
        }, 500);
        $('div.back').css('position', 'inherit');
        $('.main_text').animate({
          'top': '0'
        }, 500);
      } else {
        $('.main_create').animate({
          'top': '0'
        }, 500);
        $('.main_create').fadeOut(500);
        $('div.back_create').css('position', 'inherit');
        $('div.back_create').css('width', '0');
        $('div.back_create').css('height', '0');
        $('div.back').css('width', '100%');
        $('div.back').css('height', '735px');
      }
    }

  });
});

$(function() {
  $("input[name='log_id_new']").keyup(function() {
    if (!$('#text_new').val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)) {
      $('.error').text('正しいメールアドレスを入力してください。')
      $('.ma').css('margin-bottom', '0');
      return false;
    } else {
      $('.error').text('')
      $('.ma').css('margin-bottom', '25px');
      return false;
    }
  });
  if ($('#text_new').val().length == 0) {
    $('#submit_new').attr('disabled', 'disabled');

  } else if ($('#passwd_new').val().length == 0) {
    $('#submit_new').attr('disabled', 'disabled');

  } else if ($('#user_name').val().length == 0) {
    $('#submit_new').attr('disabled', 'disabled');

  }


  $('#text_new').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 6) {
      $('#submit_new').attr('disabled', 'disabled');
    }
  });
  $('#user_name').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 4) {
      $('#submit_new').attr('disabled', 'disabled');
      $('.error').text('');
    } else {
      $('.error').text('ユーザー名は5文字以上入力してください。');
      $('.ma').css('margin-bottom', '25px');
    }
  });
  $('#passwd_new').bind('keydown keyup keypress change', function() {
    if ($(this).val().length > 6) {
      $('#submit_new').removeAttr('disabled');
      $('.error').text('');
    } else if ($(this).val().match(/^[A-Za-z0-9]*$/) && $(this).val().length < 6) {
      $('#submit_new').attr('disabled', 'disabled');
      $('.error').html('パスワードは6文字以上、<br/>半角英数字で入力してください。')
    }
  });

});

// $(function() {
//   var jqxhr;
//
//   $('form').submit(function(e) {
//       // if (!flag) {
//         // e.preventDefault();
//         var user = $('#user_name').val();
//         jqxhr = $.ajax({
//           type: "GET",
//           url: "static/user.json",
//           dataType: 'json',
//           success: function(json) {
//             var len = json.length;
//             $('#test').text(user);
//             var user = $('#user_name').val();
//             for (var i = 0; i < len; i++) {
//               if (json[i].user_name === user) {
//
//                 $('.error').text('すでに登録されているユーザー名です。');
//                 return false;
//
//               } else if (json[i].user_name != user) {
//                 jqxhr.abort();
//
//                 return true;
//               }
//             }
//           }
//         });
//        }
//       });
// });
