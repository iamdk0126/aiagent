from typing import Dict, List

class FormatPreset:
    """影視體裁時間結構設定"""
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.name}: {self.duration} 分鐘"

class FormatPresets:
    """六大影視體裁的時間結構設定"""
    def __init__(self):
        self.presets: Dict[str, FormatPreset] = {
            "SHORT_1MIN": FormatPreset("1 分鐘短片", 1),
            "SHORT_3MIN": FormatPreset("3 分鐘短片", 3),
            "MINI_SERIES_10MIN": FormatPreset("10 分鐘迷你影集", 10),
            "TV_DRAMA_60MIN": FormatPreset("60 分鐘電視劇", 60),
            "FEATURE_FILM_90MIN": FormatPreset("90 分鐘電影", 90)
        }

    def get_preset(self, name: str) -> FormatPreset:
        """獲取指定影視體裁的時間結構設定"""
        return self.presets.get(name, None)

    def get_all_presets(self) -> List[FormatPreset]:
        """獲取所有影視體裁的時間結構設定"""
        return list(self.presets.values())
