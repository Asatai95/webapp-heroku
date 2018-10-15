// // 戻るボタン
// function goBack() {
//     window.history.back();
// }
// 戻るボタン

$(document).ready(function(){
    $('.modal').modal();
});

$(function(){
  $('a.waves-effect.my_plan').click(function(e){
    e.preventDefault();
  });
});

$(function(){

    // Materialize mobile menu
    $(document).ready(function(){
        $('.sidenav').sidenav({
            closeOnClick: true,
            edge: 'right',
        });
    });

    // form のバリデーション
    $.extend($.validator.messages, {
        email: '正しいメールアドレスを入力して下さい。',
        equalTo: 'もう一度同じ値を入力して下さい。',
        minlength: '{0}文字以上入力して下さい。',
        required: '入力して下さい。',
        digits: '整数を入力してください',
    });

    $('form').validate({
        rules: {
            email: {
                required: true,
                email: true,
            },
            password1: {
                required: true,
                minlength: 8,
            },
            password2: {
                equalTo: '[name=password1]'
            },
            name: {
                maxlength: 200,
            },
            age: {
                digits: true,
                min: 0,
            },
        },
        messages: {
            password1: {
              required: 'パスワードを入力して下さい。',
              minlength: 'パスワードは{0}文字以上入力して下さい。',
            },
            password2: {
                required: '確認パスワードを入力して下さい。',
                equalTo: 'パスワードが一致しません。',
            },
            email: {
                required: 'メールアドレスは必須です。',
                email: '正しいメールアドレスを入力してください。',
            },
            name: {
                maxlength: '名前はは200文字以内です。',
            },
            age: {
                digits: '年齢は整数を入力してください'
            },
        },
        errorContainer: $(".form-error"),
        errorLabelContainer: $(".form-error ul#error-messages"),
        wrapper: 'li',
    });

});
