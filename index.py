import math
from collections import defaultdict

STOPWORDS = {
    "the", "is", "and", "a", "an", "of", "to", "in", "on", "for", "with"
}

def tokenize(text):
    text = text.lower()
    tokens = []
    word = ""

    for ch in text:
        if ch.isalnum():
            word += ch
        else:
            if word:
                tokens.append(word)
                word = ""
    if word:
        tokens.append(word)

    return [t for t in tokens if t not in STOPWORDS]


def build_index(docs):
    inverted_index = defaultdict(dict)
    doc_lengths = {}

    for doc_id, text in enumerate(docs):
        tokens = tokenize(text)
        doc_lengths[doc_id] = len(tokens)

        freq = defaultdict(int)
        for token in tokens:
            freq[token] += 1

        for token, count in freq.items():
            inverted_index[token][doc_id] = count

    return inverted_index, doc_lengths


def load_docs(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == "__main__":
    docs = load_docs(r"C:\Users\91949\Documents\Search_Engine\data\docs.txt")
    index, lengths = build_index(docs)

    print(f"Documents indexed: {len(docs)}")
    print(f"Unique terms: {len(index)}")

