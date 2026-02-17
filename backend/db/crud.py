from sqlalchemy.orm import Session
from backend.db.db_models import StandingsTeam,Standing, Season, Country, StatsTeam, AthleteEntry, TeamEntry, StatsType

# Standings
def create_standings_team(db: Session, data):
    team = db.query(StandingsTeam).filter(StandingsTeam.id == data.id).first()

    if team:
        team.name = data.name
        team.description = data.description
        team.logo_url = data.logo_url
        team.color = data.color
    else:
        team = StandingsTeam(
            id=data.id,
            name=data.name,
            description=data.description,
            logo_url=data.logo_url,
            color=data.color
        )
        db.add(team)

    db.commit()
    db.refresh(team)
    return team


def create_standing(db: Session, data):
    standing = Standing(
        games_total=data.games_total,
        games_lost=data.games_lost,
        games_won=data.games_won,
        position=data.position,
        points=data.points,
        points_against=data.points_against,
        points_in_favor=data.points_in_favor,
        team_id=data.team_id,
        season_id=data.season_id
    )

    db.add(standing)
    db.commit()
    db.refresh(standing)
    return standing


def create_season(db: Session, data):
    season = db.query(Season).filter(Season.id == data.id).first()

    if season:
        season.name = data.name
    else:
        season = Season(id=data.id, name=data.name)
        db.add(season)

    db.commit()
    db.refresh(season)
    return season


# Stats
def create_country(db: Session, data):
    country = db.query(Country).filter(Country.id == data.id).first()

    if country:
        country.name = data.name
    else:
        country = Country(id=data.id, name=data.name)
        db.add(country)

    db.commit()
    db.refresh(country)
    return country


def create_stats_team(db: Session, data):
    team = db.query(StatsTeam).filter(StatsTeam.id == data.id).first()

    if team:
        team.name = data.name
    else:
        team = StatsTeam(id=data.id, name=data.name)
        db.add(team)

    db.commit()
    db.refresh(team)
    return team


def create_stats_type(db: Session, data):
    stat_type = (
        db.query(StatsType)
        .filter(
            StatsType.internal_type_id == data.stat_type_id,
            StatsType.scope == data.scope
        )
        .first()
    )

    if stat_type:
        stat_type.name = data.name
    else:
        stat_type = StatsType(internal_type_id=data.stat_type_id, external_type_id=data.external_type_id, name=data.name, scope=data.scope)
        db.add(stat_type)

    db.commit()
    db.refresh(stat_type)
    return stat_type


def create_athlete_entry(db: Session, data, stat_type_db_id):
    entry = AthleteEntry(
        athlete_id=data.athlete_id,
        name=data.name,
        short_name=data.short_name,
        position_name=data.position_name,
        position_short_name=data.position_short_name,
        country_id=data.country_id,
        team_id=data.team_id,
        stat_type_id=stat_type_db_id,
        stat_value=data.stats.value # convertido a string
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def create_team_entry(db: Session, data, stat_type_db_id):
    entry = TeamEntry(
        position=data.position,
        team_id=data.team_id,
        country_id=data.country_id,
        team_name=data.team_name,
        stat_type_id=stat_type_db_id,
        stat_value=data.stats.value # convertido a string
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry