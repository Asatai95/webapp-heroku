% rebase('templates/base')
<h1>index</h1>

<!-- % if current_user:
<main>
    <div class="goods">
        % for num in range(1,11):
        <div class="card">
            <div class="card-image waves-effect waves-block waves-light">
                <img class="activator" src="{{ url('static_file', filepath='img/office.jpg') }}">
            </div>
            <div class="card-content">
                <span class="card-title activator grey-text text-darken-4">商品{{num}}</span>
                <p>￥{{num*980}}</p>
                <p>
                    <form action="/charge" method="post">
                        <input type="hidden" name="amount" value="{{num*980}}">
                        <input type="hidden" name="description" value="商品{{num}}の支払い">
                        <script src="https://checkout.stripe.com/checkout.js" class="stripe-button"
                                data-key="{{ publish_key }}"
                                data-label="購入する"
                                data-description="商品{{num}}購入"
                                data-currency="JPY"
                                data-amount="{{num*980}}"
                                data-panelLabel="購入する"
                                data-locale="ja"></script>
                    </form>
                </p>
            </div>
            <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">商品{{num}}<i class="material-icons right">close</i></span>
                <p>テキストテキストテキストテキストテキスト。テキストテキストテキストテキスト。</p>
            </div>
        </div>
        % end
    </div>
</main>
% end -->
