<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/tatume.css">

  <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"> -->

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <script type="text/javascript" src="static/js/tatume_top.js"></script>
  <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.17.0/jquery.validate.min.js"></script> -->
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css" />
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->


  <title>TUBUYAKI</title>


    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
    <script src="https://apis.google.com/js/api:client.js"></script>
    <script>
      var googleUser = {};
      var startApp = function() {
        gapi.load('auth2', function() {

          auth2 = gapi.auth2.init({
            client_id: '1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com',
            cookiepolicy: 'single_host_origin',

          });
          attachSignin(document.getElementById('customBtn'));
        });
      };
      function attachSignin(element) {
      console.log(element.id);
      auth2.attachClickHandler(element, {},
          function(googleUser) {
            // document.getElementById('name').innerText = "Signed in: " +
            //     googleUser.getBasicProfile().getName();
          });
        }
    </script>
    <style type="text/css">
      #customBtn {
        display: inline-block;
        background: rgba(255, 77, 77, .9);
        color: #444;
        width: 240px;
        height: 40px;
        text-align: left;
        border-radius: 5px;
        white-space: nowrap;
        margin: 0 0 20px 0;
        border-radius: 5px;
      }

      #customBtn:hover {
        cursor: pointer;
        opacity: .9;
        box-shadow: 0 0 5px rgba(255, 77, 77);
      }

      span.icon {
        background: url('static/img/icon.png') transparent 5px 50% no-repeat;
        background-repeat: no-repeat;
        background-size: 60%;
        display: inline-block;
        vertical-align: middle;
        width: 35px;
        height: 40px;
        margin-left: 5px;
      }

      span.buttonText {
        display: inline-block;
        vertical-align: middle;
        padding-left: 10px;
        padding-right: 25px;
        font-size: 17px;
        color: white;
        font-weight: 600;
        font-family: 'Roboto', sans-serif;
      }
    </style>


</head>


   {{!base}}


</html>
