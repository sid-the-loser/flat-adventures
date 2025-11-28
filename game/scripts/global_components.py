from typing import Any

from hatred.component import GlobalComponent

class GlobalKeys(GlobalComponent):
    def __init__(self, parent_app: Any) -> None:
        super().__init__("GlobalKeys", parent_app)

    def early_update(self) -> None:
        pass