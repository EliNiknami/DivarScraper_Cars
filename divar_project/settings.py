BOT_NAME = "divar_project"

SPIDER_MODULES = ["divar_project.spiders"]
NEWSPIDER_MODULE = "divar_project.spiders"

ADDONS = {}

# مهم
ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    "divar_project.pipelines.DivarProjectPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
