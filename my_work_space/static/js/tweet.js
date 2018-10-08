$(function(){
  $('#tweet_button').on('click', function(){
    $('.tweet_content').fadeIn(800);
    $('.tweet_main').fadeOut(500);
  });
});

$(function(){
  //画像ファイルプレビュー表示のイベント追加 fileを選択時に発火するイベントを登録
  $('form').on('change', 'input[type="file"]', function(e) {
    var file = e.target.files[0],
        reader = new FileReader(),
        $preview = $(".img_view");
        t = this;

    // 画像ファイル以外の場合は何もしない
    if(file.type.indexOf("image") < 0){
      return false;
    }

    // ファイル読み込みが完了した際のイベント登録
    reader.onload = (function(file) {
      return function(e) {
        //既存のプレビューを削除
        $preview.empty();
        // .prevewの領域の中にロードした画像を表示するimageタグを追加
        $preview.append($('<img>').attr({
                  src: e.target.result,
                  width: "80px",
                  class: "preview",
                  title: file.name
              }));
      };
    })(file);

    reader.readAsDataURL(file);
  });
});
//
// $(function(){
//   var pageTop1 = $("#page-top1");
//   $(window).scroll(function () {
//
//         if($('body, html').scrollTop() >= 50) {
//           pageTop1.css( "bottom", "30px" );
//         } else {
//           pageTop1.css( "bottom", "-85px" );
//         }
//       });
//     $("a[href^='#']").click(function(){
//
//         //data-box属性がない場合は通常のスムーズスクロール
//             $("body,html").stop().animate({
//                 scrollTop:$('.main').offset().top
//               });
//         //data-box属性がある場合はdata-box内をスムーズスクロー
//             var dist = $('.main').position().top - $('.header').position().top;
//             $('.header').stop().animate({
//                 scrollTop: $('.header').scrollTop() + dist
//             });
//         return false;
//     });
// });
