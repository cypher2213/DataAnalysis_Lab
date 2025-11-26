import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download("stopwords")
from nltk.corpus import gutenberg, stopwords
from collections import Counter

import matplotlib.pyplot as plt

file_name = "bryant-stories.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

words = nltk.word_tokenize(text)
print(f"\n1. Загальна кількість слів у тексті: {len(words)}")
total_words_lower = [word.lower() for word in words]

freq_all = Counter(total_words_lower)
ten_popular = freq_all.most_common(10)
print("\n2. 10 найбільш повторюваних слів (слова, без очищення)\n")
for word, count in ten_popular:
    print(f"{word!r}: {count}")

stop_words = set(stopwords.words("english"))
clean_words = [
    w for w in total_words_lower
    if w.isalpha() and w not in stop_words
]
print(f"3. Кількість слів після очищення: {len(clean_words)}")


freq_clean = Counter(clean_words)
ten_clean = freq_clean.most_common(10)

print("\n4. Топ-10 слів після очищення:\n")
for word, count in ten_clean:
    print(f"{word!r}: {count}")