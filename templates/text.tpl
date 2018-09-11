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

  <div id="fb-root"></div>
  <script>
    (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      js = d.createElement(s);
      js.id = id;
      js.src = 'https://connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v3.1&appId=704097009951110&autoLogAppEvents=1';
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
  </script>

  <script type="text/javascript">
    // Client ID and API key from the Developer Console
    var CLIENT_ID = '593034558997-1rq8bnc2o3lm0gc1ko0dgtc4du0kr4c7.apps.googleusercontent.com';
    var API_KEY = 't11YjCZt6lPxgv0msKQxqLLF';

    // Array of API discovery doc URLs for APIs used by the quickstart
    var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/gmail/v1/rest"];

    // Authorization scopes required by the API; multiple scopes can be
    // included, separated by spaces.
    var SCOPES = 'https://www.googleapis.com/auth/gmail.readonly';

    var authorizeButton = document.getElementById('authorize_button');
    var signoutButton = document.getElementById('signout_button');

    /**
     *  On load, called to load the auth2 library and API client library.
     */
    function handleClientLoad() {
      gapi.load('client:auth2', initClient);
    }

    /**
     *  Initializes the API client library and sets up sign-in state
     *  listeners.
     */
    function initClient() {
      gapi.client.init({
        apiKey: API_KEY,
        clientId: CLIENT_ID,
        discoveryDocs: DISCOVERY_DOCS,
        scope: SCOPES
      }).then(function() {
        // Listen for sign-in state changes.
        gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

        // Handle the initial sign-in state.
        updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
        authorizeButton.onclick = handleAuthClick;
        signoutButton.onclick = handleSignoutClick;
      });
    }

    /**
     *  Called when the signed in status changes, to update the UI
     *  appropriately. After a sign-in, the API is called.
     */
    function updateSigninStatus(isSignedIn) {
      if (isSignedIn) {
        authorizeButton.style.display = 'none';
        signoutButton.style.display = 'block';
        listLabels();
      } else {
        authorizeButton.style.display = 'block';
        signoutButton.style.display = 'none';
      }
    }

    /**
     *  Sign in the user upon button click.
     */
    function handleAuthClick(event) {
      gapi.auth2.getAuthInstance().signIn();
    }

    /**
     *  Sign out the user upon button click.
     */
    function handleSignoutClick(event) {
      gapi.auth2.getAuthInstance().signOut();
    }

    /**
     * Append a pre element to the body containing the given message
     * as its text node. Used to display the results of the API call.
     *
     * @param {string} message Text to be placed in pre element.
     */
    function appendPre(message) {
      var pre = document.getElementById('content');
      var textContent = document.createTextNode(message + '\n');
      pre.appendChild(textContent);
    }

    /**
     * Print all Labels in the authorized user's inbox. If no labels
     * are found an appropriate message is printed.
     */
    function listLabels() {
      gapi.client.gmail.users.labels.list({
        'userId': 'me'
      }).then(function(response) {
        var labels = response.result.labels;
        appendPre('Labels:');

        if (labels && labels.length > 0) {
          for (i = 0; i < labels.length; i++) {
            var label = labels[i];
            appendPre(label.name)
          }
        } else {
          appendPre('No Labels found.');
        }
      });
    }
  </script>


  <script async defer src="https://apis.google.com/js/api.js" onload="this.onload=function(){};handleClientLoad()" onreadystatechange="if (this.readyState === 'complete') this.onload()">
  </script>

  <script type="text/javascript">


  function signinCallback(authResult) {
    if (authResult['access_token']) {
      // 正常に承認されました
      // ユーザーが認証されたのでログイン ボタンを非表示にします。例:
      document.getElementById('signinButton').setAttribute('style', 'display: none');

  	//追加部分--------------
  	var info = document.getElementById('info');
  	var textNode = document.createTextNode("Google+にログインできた。");
  	info.appendChild(textNode);
  	//---------追加部分終わり


    } else if (authResult['error']) {
      // エラーが発生しました。
      // 可能性のあるエラー コード:
      //   「access_denied」 - ユーザーがアプリへのアクセスを拒否しました
      //   「immediate_failed」 - ユーザーを自動的にログインできませんでした
      // console.log（「There was an error: 」 + authResult[「エラー」]）;
     }
   }

    </script>


</head>

<body>


  <div class='main_text'>
    <div class='title'>
      <p class='title_text'>ログイン</p>
    </div>
    <div class='main_content'>

      <div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type='login_with' data-show-faces="false" data-auto-logout-link="false" data-use-continue-as="false" data-width="200px" data-height='50px'></div>
      <button id="authorize_button" style="display: none;">Authorize</button>
      <button id="signout_button" style="display: none;">Sign Out</button>

      <span id="signinButton">
        <span
          class="g-signin"
          data-callback="signinCallback"
          data-width="200px"
          data-height='50px'
          data-size="large"
          data-clientid="1079133430628-rhbrhpfsoc59u3hqiv86tj9qe08piu3j.apps.googleusercontent.com"
          data-cookiepolicy="single_host_origin"
          data-requestvisibleactions="http://schemas.google.com/AddActivity"
          data-scope="https://www.googleapis.com/auth/plus.login">

        </span>
      </span>

      <div id="info"></div>

      <script type="text/javascript">
        (function() {
          var po = document.createElement('script');
          po.type = 'text/javascript';
          po.async = true;
          po.src = 'https://apis.google.com/js/client:plusone.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(po, s);
        })();
      </script>

    </div>
    <p class='ma'><span class='sen'><img src="static/img/sen.jpeg" alt=""></span> または
      <span class='sen'><img src="static/img/sen.jpeg" alt=""></span>
    </p>
    <div class='login'>
      <form action="/" method="GET">
        <p class='login_mail'><input type="text" name="log_id" maxlength="32" autocomplete="OFF" placeholder='メールアドレス' /></p>
        <p class='login_pass'><input type="password" name="passwd" maxlength="32" autocomplete="OFF" placeholder='パスワード' /></p>
        <p class="submit"><input type="submit" value="ログイン" /></p>
      </form>
    </div>
  </div>

</body>

</html>
