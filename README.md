すばらしいテーマです！🐰🍡
「うさうさ店長のログ帳」を通して **Pythonのロギング機能を実践的に理解する教材** にできますね✨

以下では、あなたの記事内の `usa_logger.py` のコードを
**1行ずつコメント付きで丁寧に解説** しました👇

---

# 🐰🍡 コード徹底解説：usa_logger.py

```python
import os
import logging
from logging.handlers import TimedRotatingFileHandler
```

🔹 **解説：**

* `os`: ファイルパスの作成やディレクトリ操作に使う標準ライブラリ。
* `logging`: Python標準のログ記録用モジュール。
* `TimedRotatingFileHandler`: 日時で自動的にログファイルを切り替える（ローテーション）ためのハンドラー。

---

```python
def setup_usausa_logger(log_dir='logs', log_name='usausa.log'):
    """
    ふわふわ大福店うさうさ店長のためのロガー設定関数 🐰🍡

    Args:
        log_dir (str): ログファイル保存ディレクトリ
        log_name (str): ベースとなるログファイル名

    Returns:
        logging.Logger: 設定済みのロガー
    """
```

🔹 **解説：**

* `setup_usausa_logger` 関数を呼ぶだけで、使いやすいロガーを一発で作れるようにしている。
* `log_dir` と `log_name` はデフォルト値付き。初心者でも設定不要で動く！

---

```python
    # ① ログディレクトリ作成（なければ作る）
    os.makedirs(log_dir, exist_ok=True)
```

🔹 **解説：**

* ログを保存するフォルダ（例：`logs/`）が存在しない場合、自動で作成。
* `exist_ok=True` にすることで、すでにフォルダがあるときもエラーにならない。

---

```python
    # ② ロガーを取得（モジュール名などで一意にする）
    logger = logging.getLogger('usausa_logger')
    logger.setLevel(logging.INFO)
```

🔹 **解説：**

* `logging.getLogger()` で新しいロガーを取得。
* `'usausa_logger'` はロガーの識別名。複数作る場合に区別できる。
* `setLevel(logging.INFO)` で「INFO以上のレベル（INFO, WARNING, ERROR, CRITICAL）」を出力対象に設定。

---

```python
    # ③ 同じログが重複しないように既存ハンドラーを削除
    if logger.hasHandlers():
        logger.handlers.clear()
```

🔹 **解説：**

* Pythonのロガーは「多重追加」しやすい。
* 同じ設定で関数を複数回呼ぶと、ログが重複して出力される問題を防ぐため、既存ハンドラーをクリア。

---

```python
    # ④ フォーマット定義
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
```

🔹 **解説：**

* 出力形式（フォーマット）を指定。
* `%()` の中はプレースホルダ：

  * `asctime`: 日時
  * `levelname`: ログレベル（INFO, ERRORなど）
  * `message`: ログ内容

📘 例：

```
2025-10-05 17:00:07,039 [INFO] - 今日のうぐいす大福は大人気でした！
```

---

```python
    # ⑤ 日付で自動分割されるログファイルハンドラー
    log_path = os.path.join(log_dir, log_name)
    file_handler = TimedRotatingFileHandler(
        filename=log_path,
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
```

🔹 **解説：**

* `TimedRotatingFileHandler` は「指定時間ごとにログファイルを自動的に切り替える」。
* `when='midnight'` → 毎日0時で切り替え。
* `interval=1` → 1日ごと。
* `backupCount=7` → 最大7日分を保存（古いログは自動削除）。
* `encoding='utf-8'` → 日本語対応。

---

```python
    file_handler.suffix = "%Y-%m-%d"  # ファイル名に日付追加
    file_handler.setFormatter(formatter)
```

🔹 **解説：**

* `suffix` を指定すると、自動生成されるファイル名に日付を追加。
  → `usausa.log.2025-10-05` のような形式になる。
* `setFormatter` で、上で定義したフォーマットを適用。

---

```python
    # ⑥ コンソール出力（画面表示）用ハンドラー
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
```

🔹 **解説：**

* ファイルだけでなく、**ターミナル（コンソール）にも同時出力**するための設定。
* ログをすぐ確認できて便利！

---

```python
    # ⑦ ロガーにハンドラーを追加
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
```

🔹 **解説：**

* ロガーに「どこに出力するか」を登録。
* この2行で「ファイル」と「画面」両方に出力するよう設定完了。

---

```python
    return logger
```

🔹 **解説：**

* 設定済みの `logger` を呼び出し元に返す。
* 以降は `logger.info()` などで自由にログを出力できる！

---

# 🧁 実行結果（例）

```bash
2025-10-05 17:00:07,039 [INFO] - 今日のうぐいす大福は大人気でした！
2025-10-05 17:00:07,039 [WARNING] - 白玉粉が残り少ないです…
2025-10-05 17:00:07,039 [ERROR] - 冷蔵庫が壊れました！！
2025-10-05 17:00:07,039 [CRITICAL] - 店舗の水道が止まりました！！！
2025-10-05 17:00:07,039 [INFO] - 在庫チェックが完了しました
```

ファイルにも同内容が記録されます👇

```
logs/usausa.log.2025-10-05
```

---

# 🐰✨ ワンポイント：可愛い絵文字ログ版

```python
formatter = logging.Formatter('🐰 %(asctime)s [%(levelname)s] 🍡 - %(message)s')
```

🎀 出力イメージ：

```
🐰 2025-10-05 17:00:07 [INFO] 🍡 - 今日のうぐいす大福は大人気でした！
```

---

# 🧭 まとめ（表）

| やりたいこと       | 実現方法                           |
| :----------- | :----------------------------- |
| 毎日ログを自動で保存   | `TimedRotatingFileHandler` を使用 |
| 画面にも表示したい    | `StreamHandler` を追加            |
| コードをスッキリさせたい | `setup_usausa_logger()` 関数化    |
| ログ重複を防ぎたい    | `logger.handlers.clear()` で初期化 |
| 日本語ログ対応      | `encoding='utf-8'`             |

---

💡 **この構成の良いところ**

* 企業システムにも使えるレベルの設計。
* 初心者でも「コピーして実行するだけ」で学べる。
* 「うさうさ店長」テーマで、技術記事が柔らかく読まれる！

---


作りましょうか？（→「はい、note用に整形して」）
