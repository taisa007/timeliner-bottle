トップページです。<br>

{% if uname is not none %}
    {{ uname }}さん
{% else %}
    <p><a href="/login">ログイン</a></p>
    <p><a href="/signup">新規登録</a></p>
{% endif %}


<table>
    <tr>
        <th>ID</th>
        <th>ツイート</th>
    </tr>
    {% for tweet in tweets %}
        <tr>
            <td>{{ tweet['id'] }}</td>
            <td>{{ tweet['tweet'] }}</td>
        </tr>
    {% endfor %}
</table>
