$(function(){

      var pageTop1 = $("#page-top1");
      pageTop1.click(function () {
        $('body, html').animate({ scrollTop: 0 }, 500);
        return false;
      });
      $(window).scroll(function () {

        if($(this).scrollTop() >= 200) {
          pageTop1.css( "bottom", "30px" );
        } else {
          pageTop1.css( "bottom", "-85px" );
        }
      });
    });
//
// $(function(){
//   $(".check_box_content img").on("click", function(){
//     $(".check_box_content").fadeOut("slow");
//   });
// });
//
// $(function(){
//   var test = $(document).on('pagecontainerchange');
//     $('#submit').click(function(){
//      if (test){
//       $(".popup").fadeIn();
//      }
//    });
// });
