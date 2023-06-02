from typing import Any

from aqt import mw

config: dict[str, Any] = mw.addonManager.getConfig(__name__)  # type: ignore
