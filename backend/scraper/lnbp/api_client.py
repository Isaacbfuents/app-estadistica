import requests


# ID     Temporada
# 34 --> 25 Varonil
# 33 --> 25 Femenil
# 32 --> 24 Varonil
# 31 --> 24 Femenil
# 29 --> 23 Varonil
# 28 --> 23 Femenil

standings_url = 'https://lnbpback.truewisdom.co/sports/standings/season'
stats_url = 'https://webws.365scores.com/web/stats'

season_id = 34
standings_payload = {
    "id_season": season_id
}

phase_num = -1 # Única fase válida para stats
stats_payload = {
"appTypeId": 5,
"langId": 29,
"timezoneName": "America/Mazatlan",
"userCountryId": 31,
"competitions": 404, # Id de la LNBP
"phaseNum": phase_num,
"withSeasons": True
}

headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "es-419,es;q=0.9,en;q=0.8",
        "Origin": "https://www.lnbp.mx",
        "Referer": "https://www.lnbp.mx/",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}


def fetch_data(url, method, payload, headers):

    methods = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "DELETE": requests.delete,
        "PATCH": requests.patch
    }
    http_method = methods[method.upper()]

    # Argumentos dinámicamente
    kwargs = {
        "headers": headers,
        "timeout": 10
    }

    # Si es GET → usar params
    if method.upper() == "GET":
        kwargs["params"] = payload
    else:
        kwargs["data"] = payload

    try:
        r = http_method(url, **kwargs)
        r.raise_for_status()

        data = r.json()

        return data
    except requests.exceptions.HTTPError as e:
        print("HTTP error: ", e)
        print("Status code: ", e.response.status_code)
        print("Error body: ", e.response.text)


standings_data = fetch_data(standings_url, 'POST', standings_payload, headers)
stats_data = fetch_data(stats_url, 'GET', stats_payload, headers)
