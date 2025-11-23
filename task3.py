import nltk
from nltk.corpus import gutenberg, stopwords
from collections import Counter
import matplotlib.pyplot as plt

file_name = "bryant-stories.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

total_words = len(text)
print(f"\n1. Загальна кількість слів у тексті: {total_words}")
total_words_lower = [word.lower() for word in total_words]

freq_all = Counter(total_words_lower)
ten_popular = freq_all.most_common(10)
print("10 найчастотніших слів (усі слова, без очищення)\n")
for word, count in ten_popular:
    print(f"{word!r}: {count}")