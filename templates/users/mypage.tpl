% rebase('templates/base')
<div class="mypage">
  <h2>マイページ<small></small></h2>
  <ul>
    % for social in socials:
    <li>{{social.provider}}連携済み</li>
    % end
  </ul>
  <a href="/mypage/edit">情報編集</a>
  <a href="/mypage/edit_password">パスワード編集</a>
  <ul>
      <li>名前:{{current_user.name}}</li>
      % if current_user.age is not None:
      <li>年齢:{{current_user.age}}</li>
      % else:
      <li>年齢：</li>
      % end
      <li>メールアドレス:{{current_user.email}}</li>
  </ul>
</div>
