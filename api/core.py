from settings import SiteSettings
from api.utils.site_api_handler import SiteApiInterface


url = "https://aliexpress-datahub.p.rapidapi.com/item_search"

querystring = {"q": "iphone", "page": "1", "sort": "priceAsc", "locale": "ru_RU", "region": "RU", "currency": "RUB"}

site = SiteSettings()
headers = {
	"X-RapidAPI-Key": site.site_key.get_secret_value(),
	"X-RapidAPI-Host": site.site_host
}

site_api = SiteApiInterface()

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
