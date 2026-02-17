from dataclasses import dataclass
from typing import Optional, List



# Clases standings lnbp
@dataclass
class StandingsTeamDTO:
    id: int
    name: str
    description: Optional[str]
    logo_url: Optional[str]
    color: Optional[str]

@dataclass
class StandingDTO:
    games_total: Optional[int]
    games_lost: Optional[int]
    games_won: Optional[int]
    position: Optional[int]
    points: Optional[int]
    points_against: Optional[int]
    points_in_favor: Optional[int]
    team_id: int # Ref a StandingsTeam id, viene api
    season_id: int # Ref a Season id, viene api

@dataclass
class SeasonDTO:
    id: int
    name: str


# Clases stats LNBP
@dataclass
class CountryDTO:
    id: int
    name: str

@dataclass
class StatsTeamDTO:
    id: int
    name: str

@dataclass
class StatDTO:
    stat_type_id: int
    external_type_id: int
    value: str

@dataclass
class AthleteEntryDTO:
    country_id: int # Ref a Country id, si viene en  api
    name: str
    short_name: Optional[str]
    athlete_id: int
    team_id: int # Ref a StatsTeam id, si viene api
    position_name: str
    position_short_name: Optional[str]
    stat_type_id: int
    stats: List[StatDTO]

@dataclass
class TeamEntryDTO:
    position: Optional[int]
    team_id: int
    country_id: int
    team_name: str
    stat_type_id: int
    stats: List[StatDTO]

@dataclass
class StatsTypeDTO:
    stat_type_id: int
    external_type_id: int
    name: str
    scope: str


