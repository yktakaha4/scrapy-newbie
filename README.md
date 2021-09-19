# scrapy-newbie

以下を poetry で写経

https://qiita.com/Chanmoro/items/f4df85eb73b18d902739

```
$ poetry install
$ ./scripts/dev.bash

# アクセスすると実行状況が確認できる
# http://localhost:6800

$ curl http://localhost:6800/schedule.json -d project=app -d spider=zenn_my_article_spider
```
