import time
import datetime


now = time.time()
print(f"now = time.time(): {now}")
print(f"int(now): {int(now)}")
date_desc = datetime.datetime.fromtimestamp(now)
print(f"date_desc = datetime.datetime.fromtimestamp(now): {date_desc}")
date_desc.strftime("%Y%m%d_%H%M%S")
print(f"date_desc.strftime('%Y%m%d_%H%M%S'): {date_desc.strftime('%Y%m%d_%H%M%S')}")
