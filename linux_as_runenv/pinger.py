import requests
from datetime import datetime, timedelta
import time
import logging
url_template = "https://simurg.space/gen_file?data=obs&date={date}"

day_offset = 1
delay_between_requests = 5
max_attempts = 30


while day_offset < max_attempts:
 
    yesterday = datetime.now() - timedelta(days=day_offset)
    yesterday = yesterday.strftime("%Y-%m-%d")
    url = url_template.format(date=yesterday)

    print(f"Working with URL: {url}")

    response = requests.get(url=url, stream = True)

    if response.status_code == 200:
        print(f"Data are available for {yesterday}")
        break
    else:
        print(f"Failed to get data for {yesterday}")

    day_offset += 1
    time.sleep(delay_between_requests)

if day_offset > max_attempts:
    logging.error("Failed to retrieve data after maximum attempts")
