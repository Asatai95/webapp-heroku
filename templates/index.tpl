% rebase('templates/base')
<h1>index</h1>

% if current_user:
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
                <!-- Modal Trigger -->
                <a class="waves-effect waves-light btn modal-trigger" href="/products/{{num}}">詳細を見る</a>
            </div>
            <div class="card-reveal">
                <span class="card-title grey-text text-darken-4">商品{{num}}<i class="material-icons right">close</i></span>
                <p>テキストテキストテキストテキストテキスト。テキストテキストテキストテキスト。</p>
            </div>
        </div>
        % end
    </div>
</main>
% end
