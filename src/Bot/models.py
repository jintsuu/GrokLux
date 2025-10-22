from dataclasses import dataclass, field

@dataclass
class Champion:
    name: str
    role: str | None = field(default="")
    elo: str | None = field(default="")
    opponent: str | None = field(default="")


@dataclass
class Result:
    champ: Champion
    with_opponent: bool
    win_rate: str | None
    match_count: str | None
    final_string: str = field(default="")