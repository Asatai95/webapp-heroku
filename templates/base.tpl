<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link rel="stylesheet" href="{{ url('static_file', filepath='css/style.css') }}">
    <title>Webapp2-sample</title>
    
</head>
<body>
    <nav>
        <div class="nav-wrapper">
            <a href="/" class="brand-logo">webapp2</a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                % if current_user is None:
                    <li><a href="#">{{current_user}}</a></li>
                % else:
                    <li><a href="#">{{current_user.email}}</a></li>
                % end
                <li><a href="#">Link1</a></li>
                <li><a href="#">Link2</a></li>
                % if current_user:
                    <li><a href="/users/logout">ログアウト</a></li>
                % else:
                    <li><a href="/users/login">ログイン</a></li>
                    <li><a href="/users/sign_up">登録</a></li>
                % end
            </ul>
            <ul id="slide-out" class="sidenav">
                % if current_user is None:
                    <li><a href="#">{{current_user}}</a></li>
                % else:
                    <li><a href="#">{{current_user.email}}</a></li>
                % end
                <li><a href="#">Link1</a></li>
                <li><a href="#">Link2</a></li>
                % if current_user:
                    <li><a href="/users/logout">ログアウト</a></li>
                % else:
                    <li><a href="/users/login">ログイン</a></li>
                    <li><a href="/users/sign_up">登録</a></li>
                % end
            </ul>
            <a href="#" data-target="slide-out" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        </div>
    </nav>

    {{!base}}

    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.17.0/jquery.validate.min.js"></script>
    <script src="{{ url('static_file', filepath='js/script.js') }}"></script>
</body>
</html>
