import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download("stopwords")
from nltk.corpus import stopwords
from collections import Counter

import matplotlib.pyplot as plt

file_name = "bryant-stories.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# Операції над не очищеним текстом
words = nltk.word_tokenize(text)
print(f"\n1. Загальна кількість слів у тексті: {len(words)}")
total_words_lower = [word.lower() for word in words]

freq_all = Counter(total_words_lower)
ten_popular = freq_all.most_common(10)
print("\n2. 10 найбільш повторюваних слів (слова, без очищення)")
for word, count in ten_popular:
    print(f"{word!r}: {count}")

words_raw = [w for w, c in ten_popular]
counts_raw = [c for w, c in ten_popular]

# Графік до очищення
plt.figure(figsize=(10, 5))
plt.bar(words_raw, counts_raw)
plt.title("Топ-10 слів без очищення")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# Операції з очищеним текстом
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


# Графік після очищення 
words_clean = [w for w, c in ten_clean]
counts_clean = [c for w, c in ten_clean]

plt.figure(figsize=(10, 5))
plt.bar(words_clean, counts_clean)
plt.title("Топ-10 слів після очищення (без пунктуації та стоп-слів)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()