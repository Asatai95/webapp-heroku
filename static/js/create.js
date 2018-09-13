$(function(){
  $(document).on('click', function(e) {

    if(!$(e.target).closest('.main_create').length && !$(e.target).closest('#new').length) {

      $('.main_create').animate({'opacity': '0'}, 500);
      $('div.back_create').css('position', 'inherit');
      $('.main_create').animate({'top': '0'}, 800);


    } else if($(e.target).closest('#new').length){

        if($('.main_create').css('opacity') == 0){
          $('.main_create').animate({'top': '100px'},800);
          $('.main_create').css('opacity', '1.0');
          $('div.back_create').css('background-color', 'rgba(0,0,0,.5)');
          $('div.back_create').css('position', 'relative');
        }else{
          $('.main_create').animate({'top': '0'},800);
          $('.main_create').animate({'opacity': '0'},500);
          $('div.back_create').css('position', 'inherit');
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
  $('#user_name').bind('keydown keyup keypress change', function() {
    if ( $(this).val().length > 5 ) {
      $('#submit').removeAttr('disabled');
    } else {
      $('#submit').attr('disabled', 'disabled');
    }
  });
});
