$(function(){
  $('html').fadeIn(800);
});

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
      $('.class_text').text(position);
      $('.class_text').text(scroll);
      $('.class_text').text($winH);
      current = (1 - (position - scroll) / $winH) * 0.5 * 100;
      $('.class_text').text(current);
      if (current > 99.9) {
        current = 100;

      }
      if (scroll > position - $winH) {
        $('div.header_sub').css('position', 'fixed');
        $('div.header_sub').css('background-color', 'rgba(255, 255, 255, 0.7)');
        $('div.header_sub').css('z-index', '5');
      }
    });
  });
});
