from backend.scraper.lnbp.parse import parse_season_standings, parse_stats_data
from backend.scraper.lnbp.api_client import standings_data, stats_data


# ID     Temporada
# 34 --> 25 Varonil
# 33 --> 25 Femenil
# 32 --> 24 Varonil
# 31 --> 24 Femenil
# 29 --> 23 Varonil
# 28 --> 23 Femenil

info_standings = parse_season_standings(standings_data)

info_stats = parse_stats_data(stats_data)
