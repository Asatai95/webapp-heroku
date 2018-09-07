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
      current = (1 - (position - scroll) / $winH) * 1.1 * 100;
      if (current > 99.9) {
        current = 100;
        $('div.header_sub').css('position', 'fixed');
        $('div.header_sub').css('background-color', 'rgba(255, 255, 255, 0.7)');
        $('div.header_sub').css('z-index', '5');
        $('div.img img').css('width', '130px');
        $('div.img img').css('height', '80px');
        $('div.img img').css('margin-top', '20px');
        $('.header_main').css('margin-top', '0');
        $('.header_main').css('margin', '25px 0 25px 0 25px');
        $('.header_main').css('font-size', '20px');
      }
    });
  });
});
