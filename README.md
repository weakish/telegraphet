This is the available [telegraph API][api]:

- createAccount
- createPage
- editAccountInfo
- editPage
- getAccountInfo
- getPage
- getPageList
- getViews
- revokeAccessToken

[api]: https://telegra.ph/api

First, I do not care about page views, so I remove the `getViews` API.

Second, remove the account concept:

- createPage
- editPage
- getPage

Hmm, `deletePage` is missing.
And `editPage` requires an account or a special token.
Thus I make page immutable,
and remove `editPage`.
Thus only two API interfaces are left:

- createPage
- getPage

Since I only care about page content, then `getPage` is unnecessary (just go the url in browser).

Therefore I wrote this simple script to post content to telegraph.

```shell script
echo '<p>Hello world!</p>' | telegraphet hello
```

I still need to create an account beforehand though.
telegraph requires an account to create a new page.

```shell script
telegraph --init PICKUP_A_USERNAME
```

If you already has a telegraph, you can setup the access token via environment variable or configuration file.

```shell script
# config file
mkdir -p ~/.config/telegraphet
echo '{ "token": "YOUR_TOKEN" }' > ~/.config/telegraphet/config.json
# environment variable
echo '<p>hi</p>' | TELEGRAPH_TOKEN=YOUR_TOKEN telegraphet hi
```

