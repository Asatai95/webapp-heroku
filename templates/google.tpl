<!DOCTYPE html>

<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain" ; charset="UTF-8" ; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/text.css">

  <script src="static/js/jquery-3.1.1.min.js"></script>
  <!-- <script type="text/javascript" src="static/js/tatume.js"></script> -->
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick.css" />
  <link rel="stylesheet" type="text/css" href="static/js/slick-1.8.1/slick/slick-theme.css" />
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/slick-1.8.1/slick/slick.min.js"></script> -->


  <title>TATUME</title>
</head>

<body>
  <div id="google-plus-button">Google+ Sign In</div>

  <script src="https://apis.google.com/js/api:client.js"></script>

  <script type="text/javascript">
    gapi.load('auth2', function() {
      var auth2;

      auth2 = gapi.auth2.init({
        client_id: "1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com",
        scope: "https://www.googleapis.com/auth/bigquery.readonly"
      });

      auth2.then(function() {
        var button = document.getElementById("google-plus-button");
        console.log("User is signed-in in Google+ platform?", auth2.isSignedIn.get() ? "Yes" : "No");

        auth2.attachClickHandler(button, {}, function(googleUser) {
          // Send access-token to backend to finish the authenticate
          // with your application

          var authResponse = googleUser.getAuthResponse();
          var $form;
          var $input;

          $form = $("<form>");
          $form.attr("action", "/complete/google-plus");
          $form.attr("method", "post");
          $input = $("<input>");
          $input.attr("name", "id_token");
          $input.attr("value", authResponse.id_token);
          $form.append($input);
          // Add csrf-token if needed
          $(document.body).append($form);
          $form.submit();
        });
      });
    });
  </script>

  <div id="google-plus-button">Google+ Sign In</div>

</body>

</html>
