from usa_logger import setup_usausa_logger

logger = setup_usausa_logger()

logger.info("今日のうぐいす大福は大人気でした！")
logger.warning("白玉粉が残り少ないです…")
logger.error("冷蔵庫が壊れました！！")
logger.debug("在庫チェックを開始します")
logger.critical("店舗の水道が止まりました！！！")
logger.info("在庫チェックが完了しました")
