from backend.db.database import SessionLocal
from backend.db import crud
from backend.scraper.lnbp.display import info_standings, info_stats


def main():
    db = SessionLocal()

    stat_type_map = {}  # (internal_type_id, scope) -> db_id
    try:
        # Create Standings
        crud.create_season(db, info_standings["season"])

        for team in info_standings["teams"]:
            crud.create_standings_team(db, team)

        for standing in info_standings["standings"]:
            crud.create_standing(db, standing)


        # Create Stats
        for country in info_stats["countries"]:
            crud.create_country(db, country)

        for team in info_stats["teams"]:
            crud.create_stats_team(db, team)

        for category in info_stats["categories"]:
            stat_type = crud.create_stats_type(db, category)
            key = (stat_type.internal_type_id, stat_type.scope)
            stat_type_map[key] = stat_type.id


        for athlete_entry in info_stats["entries"]["athlete_entries"]:
            key = (athlete_entry.stat_type_id, "PLAYER")
            db_stat_type_id = stat_type_map[key]
            crud.create_athlete_entry(db, athlete_entry, db_stat_type_id)

        for team_entry in info_stats["entries"]["team_entries"]:
            key = (team_entry.stat_type_id, "TEAM")
            db_stat_type_id = stat_type_map[key]
            crud.create_team_entry(db, team_entry, db_stat_type_id)


    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    print("Iniciando inserción...")
    main()
    print("Inserción finalizada.")