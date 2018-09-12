

$(function(){
  $(document).on('click', function(e) {

    if(!$(e.target).closest('.main_text').length && !$(e.target).closest('.login_sub').length) {
        $('.main_text').fadeOut();
        $('div.back').css('position', 'inherit');
    }else if($(e.target).closest('.login_sub').length){

        if($('.main_text').css('display') == 'none'){
            $('.main_text').fadeIn(800);
            $('div.back').css('background-color', 'rgba(0,0,0,.5)');
            $('div.back').css('position', 'absolute');
        }else{
            $('.main_text').fadeOut(800);
            $('div.back').css('position', 'inherit');
        }
    }
  });
});

//
// $(function(){
//   $('li.login_sub').on('click', function() {
//     $('div.main_text').fadeIn(800);
//     $('div.back').css('background-color', 'rgba(0,0,0,.5)');
//     $('div.back').css('position', 'absolute');
//
//   });
//   $('.main').on('click', function(){
//     $('div.main_text').fadeOut(800);
//   });
// }
// });

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
