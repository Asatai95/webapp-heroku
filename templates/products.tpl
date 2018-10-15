% rebase('templates/base')
<h2>商品{{product_id}}</h2>
<div class="container" style="width:50%;">
    <div class="card">
        <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="{{ url('static_file', filepath='img/office.jpg') }}">
        </div>
        <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">商品{{product_id}}</span>
            <p>￥{{product_id*980}}</p>
            <!-- Modal Trigger -->
            <a class="waves-effect waves-light btn modal-trigger" href="#modal1">購入する</a>
            <!-- Modal Structure -->
            <div id="modal1" class="modal">
                <div class="modal-content">
                <h4>購入しますか？</h4>
                </div>
                <div class="modal-footer">
                <form action="/products/charge" method="post">
                    <a href="#!" class="modal-close waves-effect waves-red btn-flat">キャンセル</a>
                    <input type="hidden" name="amount" value="{{product_id*980}}">
                    <input type="hidden" name="description" value="商品{{product_id}}の支払い">
                    <button class="waves-effect waves-light btn modal-trigger">購入する</button>
                </form>
                </div>
            </div>
        </div>
        <div class="card-reveal">
            <span class="card-title grey-text text-darken-4">商品{{product_id}}<i class="material-icons right">close</i></span>
            <p>テキストテキストテキストテキストテキスト。テキストテキストテキストテキスト。</p>
        </div>
    </div>
</div>
