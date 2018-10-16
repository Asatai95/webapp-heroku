$(function () {
  $('div.header').each(function () {
    var $win = $(window),
        $winH = $win.height(),
        $connect = $(this),
        position = $connect.offset().top,
        current = 0,
        scroll;
    $win.on('load scroll', function () {
      scroll = $win.scrollTop();
      current = (1 - (position - scroll) / $winH) * 1 * 90;
      if (current > 99.9) {
        current = 100;

        $('div.header_sub').css('position', 'fixed');
        $('div.header_sub').css('background-color', 'rgba(255, 255, 255, 0.7)');
        $('div.header_sub').css('z-index', '5');
        $('div.img img').css('width', '130px');
        $('div.img img').css('height', '100px');
        $('div.img img').css('margin-top', '20px');
        $('.header_main').css('margin-top', '0');
        $('.header_main').css('margin', '25px 0 25px 0');
        $('.header_main').css('font-size', '20px');
      } else {
        $('div.header_sub').css('display', 'block');
        $('div.header_sub').css('background-color', 'rgba(255, 255, 255, 0)');
        $('div.header_sub').css('z-index', '0');
        $('div.img img').css('width', '150px');
        $('div.img img').css('height', '100px');
        $('div.img img').css('margin-top', '80px');
        $('.header_main').css('margin-top', '80px');
        $('.header_main').css('margin', '80px 0 0 0');
        $('.header_main').css('font-size', '25px');
      }
    });
  });
});

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
