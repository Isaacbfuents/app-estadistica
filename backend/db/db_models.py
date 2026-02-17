from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey,
    UniqueConstraint, Index, Boolean, DateTime, Text
)
from sqlalchemy.orm import relationship
from backend.db.database import Base


# Standing classes
class StandingsTeam(Base):
    __tablename__ = "standings_team"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    color = Column(String, nullable=True)

    def __repr__(self):
        return f"<StandingsTeam id={self.id} name={self.name}"


class Standing(Base):
    __tablename__ = "standing"

    id = Column(Integer, primary_key=True, autoincrement=True)

    games_total = Column(Integer, nullable=True)
    games_lost = Column(Integer, nullable=True)
    games_won = Column(Integer, nullable=True)
    position = Column(Integer, nullable=False)
    points = Column(Integer, nullable=True)
    points_against = Column(Integer, nullable=True)
    points_in_favor = Column(Integer, nullable=True)

    team_id = Column(Integer, ForeignKey("standings_team.id"), nullable=False)
    season_id = Column(Integer, ForeignKey("season.id"), nullable=False)

    team = relationship("StandingsTeam")
    season = relationship("Season")

    def __repr__(self):
        return f"<Standing team_id={self.team_id} season_id={self.season_id} pos={self.position}>"


class Season(Base):
    __tablename__ = "season"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Season id={self.id} name={self.name}>"


# Stats classes
class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Country id={self.id} name={self.name}>"


class StatsTeam(Base):
    __tablename__ = "stats_team"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<StatsTeam id={self.id} name={self.name}>"


class AthleteEntry(Base):
    __tablename__ = "athlete_entry"

    id = Column(Integer, primary_key=True, autoincrement=True)

    athlete_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    short_name = Column(String, nullable=True)
    position_name = Column(String, nullable=False)
    position_short_name = Column(String, nullable=True)

    country_id = Column(Integer, ForeignKey("country.id"), nullable=True)
    team_id = Column(Integer, ForeignKey("stats_team.id"), nullable=True)
    stat_type_id = Column(Integer, ForeignKey("stats_type.id"), nullable=False)

    stat_value = Column(String, nullable=False)  # <<< valor del Stat

    country = relationship("Country")
    team = relationship("StatsTeam")
    stat_type = relationship("StatsType")

    def __repr__(self):
        return f"<AthleteEntry athlete={self.athlete_id} stat={self.stat_value}>"


class TeamEntry(Base):
    __tablename__ = "team_entry"

    id = Column(Integer, primary_key=True, autoincrement=True)

    position = Column(Integer, nullable=True)
    team_id = Column(Integer, ForeignKey("stats_team.id"), nullable=False)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=True)
    team_name = Column(String, nullable=False)

    stat_type_id = Column(Integer, ForeignKey("stats_type.id"), nullable=False)
    stat_value = Column(String, nullable=True)

    country = relationship("Country")
    team = relationship("StatsTeam")
    stat_type = relationship("StatsType")

    def __repr__(self):
        return f"<TeamEntry team={self.team_name} stat={self.stat_value}>"


class StatsType(Base):
    __tablename__ = "stats_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    internal_type_id = Column(Integer, nullable=False, unique=True)
    external_type_id = Column(Integer, nullable=True)
    name = Column(String, nullable=False)
    scope = Column(String, nullable=False) # "PLAYER" or "TEAM"

    def __repr__(self):
        return f"<StatsType id={self.id} code={self.internal_type_id} scope={self.scope}>"
