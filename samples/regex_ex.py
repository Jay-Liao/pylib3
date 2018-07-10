import re

sample = "I am from 美国。We should be friends. 朋友。"

# strategy 1
print("Strategy 1")
chinese_reg = re.compile("[\u4e00-\u9fff]+")
for matched_text in chinese_reg.findall(sample):
    print(matched_text)

# strategy 2
print("Strategy 1")
for matched_text in re.findall("[\u4e00-\u9fff]+", sample):
    print(matched_text)
