from collections import Counter
from datetime import datetime


class PepParsePipeline:
    def __init__(self):
        self.status_counter = Counter()
        self.total_statuses = 0

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counter[status] += 1
            self.total_statuses += 1
        return item

    def close_spider(self, spider):
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'results/status_summary_{current_time}.csv'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.status_counter.items():
                f.write(f'{status}, {count}\n')
            f.write(f'Total,{str(self.total_statuses)}\n')
