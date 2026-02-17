from backend.scraper.lnbp.scraper_models import StandingsTeamDTO, StandingDTO, SeasonDTO, CountryDTO, StatsTeamDTO, StatDTO, AthleteEntryDTO, TeamEntryDTO, StatsTypeDTO
from backend.helpers.id_generator import generate_type_id



def parse_team(raw_team):
    return StandingsTeamDTO(
        id= raw_team.get("id"),
        name= raw_team.get("name"),
        description= raw_team.get("description"),
        logo_url= raw_team.get("url_logo"),
        color= raw_team.get("team_color")
        )

def parse_standing(raw):

    return StandingDTO(
        games_total= raw.get("games"),
        games_lost= raw.get("games_lost"),
        games_won= raw.get("games_won"),
        position= raw.get("place"),
        points= raw.get("points"),
        points_against= raw.get("points_against"),
        points_in_favor= raw.get("points_in_favor"),
        team_id= raw.get("id_team"),
        season_id= raw.get("id_season")
    )

def parse_season_standings(data):
    season_raw = data["item_season"]
    standing_raw = data["items_standing"]

    standings = []
    teams = []

    for s in standing_raw:
        standing = parse_standing(s)
        team = parse_team(s["team"])

        # Append a los arrays donde se almacenara cada dato aparte
        standings.append(standing)
        teams.append(team)

    # Obj de Season
    season = SeasonDTO(
        id= season_raw.get("id"),
        name= season_raw.get("name")
    )

    return {
        "season": season,
        "standings": standings,
        "teams": teams
    }

def parse_countries(raw_country):
    countries = []
    for c in raw_country:
        country = CountryDTO(
            id = c.get("id"),
            name = c.get("name")
        )
        countries.append(country)
    return countries

def parse_stats_teams(raw_stats_teams):
    teams = []
    for t in raw_stats_teams:
        team = StatsTeamDTO(
            id = t.get("id"),
            name = t.get("name")
        )
        teams.append(team)
    return teams


def parse_stats(raw_stat, type_id):
    if not raw_stat:
        return []

    stat_data = raw_stat[0]

    return StatDTO(
        stat_type_id= type_id,
        external_type_id= stat_data.get("typeId"),
        value= stat_data.get("value")
    )


def parse_athletes_entries(raw_athletes_entries, type_id):
    athlete_entries = []
    for a_e in raw_athletes_entries:
        entity = a_e["entity"]
        stats = parse_stats(a_e["stats"], type_id)

        entry = AthleteEntryDTO(
            country_id = entity.get("countryId"),
            name = entity.get("name"),
            short_name = entity.get("shortName"),
            athlete_id=entity.get("id"),
            team_id = entity.get("competitorId"),
            position_name = entity.get("positionName"),
            position_short_name = entity.get("positionShortName"),
            stat_type_id= type_id,
            stats= stats
        )

        athlete_entries.append(entry)
    return athlete_entries


def parse_athletes_categories(raw_athletes_categories):
    athlete_categories = []
    athlete_entries = []

    for a_s in raw_athletes_categories:
        type_id = generate_type_id()
        entries_per_category = parse_athletes_entries(a_s["rows"], type_id)
        athlete_category = StatsTypeDTO(
            stat_type_id= type_id,
            external_type_id=   a_s["statsTypes"][0]["typeId"],
            name= a_s["name"],
            scope= "PLAYER"
        )
        athlete_entries.extend(entries_per_category)
        athlete_categories.append(athlete_category)

    return athlete_categories, athlete_entries


def parse_team_entries(raw_team_entries, type_id):
    team_entries = []

    for t_e in raw_team_entries:
        entity = t_e["entity"]
        stats = parse_stats(t_e["stats"], type_id)

        team_entry = TeamEntryDTO(
            position= t_e.get("position"),
            team_id= entity.get("competitorId"),
            country_id= entity.get("countryId"),
            team_name= entity.get("name"),
            stat_type_id= type_id,
            stats= stats
        )
        team_entries.append(team_entry)

    return team_entries


def parse_team_categories(raw_team_categories):
    team_categories = []
    team_entries = []

    for t_c in raw_team_categories:
        type_id = generate_type_id()
        entries_per_category = parse_team_entries(t_c["rows"], type_id)
        team_category = StatsTypeDTO(
            stat_type_id= type_id,
            external_type_id= t_c["statsTypes"][0]["typeId"],
            name= t_c["name"],
            scope="TEAM"
        )
        team_entries.extend(entries_per_category)
        team_categories.append(team_category)

    return team_categories, team_entries


def parse_stats_categories(raw_stats):
    athlete_categories, athlete_entries = parse_athletes_categories(raw_stats["athletesStats"])
    team_categories, team_entries = parse_team_categories(raw_stats["competitorsStats"])

    categories = []
    entries = {
        "athlete_entries": athlete_entries,
        "team_entries": team_entries
    }

    categories.extend(athlete_categories)
    categories.extend(team_categories)

    return categories, entries

def parse_stats_data(data):
    countries = parse_countries(data["countries"])
    categories, entries = parse_stats_categories(data["stats"])
    teams = parse_stats_teams(data["competitors"])
    return {
        "countries": countries,
        "categories": categories,
        "teams": teams,
        "entries": entries
    }
