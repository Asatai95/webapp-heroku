% rebase('templates/base')
<div class="mypage">
  <h2>マイページ<small></small></h2>
  <ul>
    % for social in socials:
    <li>{{social.provider}}連携済み</li>
    % end
  </ul>
  <div>
    <ul>
      <li><a href="/mypage/edit">情報編集</a></li>
      <li><a href="/mypage/edit_password">パスワード編集</a></li>
      <li>
        % if current_user.stripe_id is None:
          <form action="/mypage/create_card" method="post">
            <script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
                    data-key="{{ publish_key }}"
                    data-label="カードを登録する"
                    data-email="{{current_user.email}}"
                    data-description="カードを登録する"
                    data-currency="JPY"
                    data-panel-label="カードの登録"
                    data-locale="ja"></script>
          </form>
        % else:
          <form action="/mypage/edit_card" method="post">
            <script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
                    data-key="{{ publish_key }}"
                    data-label="カードを変更する"
                    data-email="{{current_user.email}}"
                    data-description="カードを変更する"
                    data-currency="JPY"
                    data-panel-label="カードの変更"
                    data-locale="ja"></script>
          </form>
          % end
      </li>
      <li>
        % if plan is None:
          フリープラン
        % else:
          {{plan.name}} <a href="/plans">[変更する]</a> <a href="/plans/delete">[月額プランをやめる]</a>
        % end
      </li>
    </ul>
  </div>

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
