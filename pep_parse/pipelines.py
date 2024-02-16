from collections import Counter
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, FILE_FORMAT, RESULTS


class PepParsePipeline:
    def __init__(self):
        self.status_counter = Counter()
        self.total_statuses = 0
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counter[status] += 1
            self.total_statuses += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime(DATETIME_FORMAT)
        filename = (f'{self.results_dir}'
                    f'/status_summary_{current_time}.{FILE_FORMAT}')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.status_counter.items():
                f.write(f'{status}, {count}\n')
            f.write(f'Total,{str(self.total_statuses)}\n')
