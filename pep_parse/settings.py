from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FILE_FORMAT = 'csv'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': FILE_FORMAT,
        'fields': ('number', 'name', 'status')
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
