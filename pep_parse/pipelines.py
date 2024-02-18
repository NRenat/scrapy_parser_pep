import csv
from collections import Counter
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, FILE_FORMAT, RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_counter = Counter()

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counter[status] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(exist_ok=True)
        current_time = datetime.now().strftime(DATETIME_FORMAT)
        filename = (f'{results_dir}'
                    f'/status_summary_{current_time}.{FILE_FORMAT}')

        self.total_statuses = sum(self.status_counter.values())

        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_counter.items())
            writer.writerow(['Total', str(self.total_statuses)])
