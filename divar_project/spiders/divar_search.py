import scrapy
import json
import copy

class DivarSearchSpider(scrapy.Spider):
    name = "divar_search"

    url = "https://api.divar.ir/v8/postlist/w/search"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0",
        "origin": "https://divar.ir",
        "referer": "https://divar.ir/s/mashhad/car"
    }

    def start_requests(self):

        payload = {
            "city_ids": ["3"],   # مشهد
            "search_data": {
                "form_data": {
                    "data": {
                        "category": {"str": {"value": "light"}}
                    }
                },
                "server_payload": {
                    "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
                    "additional_form_data": {
                        "data": {"sort": {"str": {"value": "sort_date"}}}
                    }
                }
            },
            "pagination_data": {
                "@type": "type.googleapis.com/post_list.PaginationData",
                "last_post_date": None,
                "page": 1,
                "layer_page": 1
            }
        }

        yield scrapy.Request(
            url=self.url,
            method="POST",
            headers=self.headers,
            body=json.dumps(payload),
            callback=self.parse_list,
            meta={"payload": payload}
        )

    def parse_list(self, response):

        data = json.loads(response.text)
        widgets = data.get("list_widgets", [])

        for w in widgets:
            if w.get("widget_type") == "POST_ROW":
                d = w.get("data", {})

                yield {
                    "token": d.get("token"),
                    "title": d.get("title"),
                    "price": d.get("middle_description_text"),
                    "mileage": d.get("top_description_text"),
                    "location": d.get("bottom_description_text"),
                    "image": d.get("image_url"),
                }

        # صفحه بعد
        next_date = data.get("pagination", {}).get("data", {}).get("last_post_date")
        if next_date:
            next_payload = copy.deepcopy(response.meta["payload"])
            next_payload["pagination_data"]["last_post_date"] = next_date

            yield scrapy.Request(
                url=self.url,
                method="POST",
                headers=self.headers,
                body=json.dumps(next_payload),
                callback=self.parse_list,
                meta={"payload": next_payload}
            )

