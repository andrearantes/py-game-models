import json
from pathlib import Path
from db.models import Player, Race, Guild, Skill


def main() -> None:
    BASE_DIR = Path(__file__).resolve().parent
    players_file = BASE_DIR / "data" / "players.json"
    with open(players_file) as f:
        players_data = json.load(f)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(name=player_data["race"])

        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(name=guild_data)
        else:
            guild = None

        for skill in player_data.get("skills", []):
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)

        Player.objects.create(
            nickname=player_data["nickname"],
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild)


if __name__ == "__main__":
    main()
