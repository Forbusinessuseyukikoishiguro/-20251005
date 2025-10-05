import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_usausa_logger(log_dir='logs', log_name='usausa.log'):
    """
    ふわふわ大福店うさうさ店長のためのロガー設定関数 🐰🍡

    Args:
        log_dir (str): ログファイル保存ディレクトリ
        log_name (str): ベースとなるログファイル名

    Returns:
        logging.Logger: 設定済みのロガー
    """

    # ① ログディレクトリ作成（なければ作る）
    os.makedirs(log_dir, exist_ok=True)

    # ② ロガーを取得（モジュール名などで一意にする）
    logger = logging.getLogger('usausa_logger')
    logger.setLevel(logging.INFO)

    # ③ 同じログが重複しないように既存ハンドラーを削除
    if logger.hasHandlers():
        logger.handlers.clear()

    # ④ フォーマット定義
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')

    # ⑤ 日付で自動分割されるログファイルハンドラー
    log_path = os.path.join(log_dir, log_name)
    file_handler = TimedRotatingFileHandler(
        filename=log_path,
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    file_handler.suffix = "%Y-%m-%d"  # ファイル名に日付追加
    file_handler.setFormatter(formatter)

    # ⑥ コンソール出力（画面表示）用ハンドラー
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ⑦ ロガーにハンドラーを追加
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

#ロガーのトレーニング
#実行：py main.py
# PS C:\Users\ほげほげ\desktop\excel\usausalog> py main.py
# 2025-10-05 17:00:07,039 [INFO] - 今日のうぐいす大福は大人気でした！
# 2025-10-05 17:00:07,039 [WARNING] - 白玉粉が残り少ないです…
# 2025-10-05 17:00:07,039 [ERROR] - 冷蔵庫が壊れました！！
# 2025-10-05 17:00:07,039 [CRITICAL] - 店舗の水道が止まりました！！！
# 2025-10-05 17:00:07,039 [INFO] - 在庫チェックが完了しました