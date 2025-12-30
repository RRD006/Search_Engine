import math
from index import tokenize, build_index, load_docs

def compute_idf(index, total_docs):
    idf = {}
    for term, postings in index.items():
        df = len(postings)
        idf[term] = math.log(total_docs / (1 + df))
    return idf


def cosine_similarity(vec1, vec2):
    dot = 0
    norm1 = 0
    norm2 = 0

    for k in vec1:
        norm1 += vec1[k] ** 2
        if k in vec2:
            dot += vec1[k] * vec2[k]

    for k in vec2:
        norm2 += vec2[k] ** 2

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot / (math.sqrt(norm1) * math.sqrt(norm2))


def search(query, index, idf, docs, top_k=3):
    query_tokens = tokenize(query)
    query_vec = {}

    for t in query_tokens:
        query_vec[t] = query_vec.get(t, 0) + 1
        query_vec[t] *= idf.get(t, 0)

    scores = {}

    for term in query_tokens:
        if term not in index:
            continue

        for doc_id, tf in index[term].items():
            if doc_id not in scores:
                scores[doc_id] = 0
            scores[doc_id] += tf * idf.get(term, 0)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [(doc_id, docs[doc_id]) for doc_id, _ in ranked[:top_k]]


if __name__ == "__main__":
    docs = load_docs("data/docs.txt")
    index, _ = build_index(docs)
    idf = compute_idf(index, len(docs))

    while True:
        q = input("Query (or exit): ")
        if q == "exit":
            break
        results = search(q, index, idf, docs)
        for doc_id, text in results:
            print(f"[Doc {doc_id}] {text}")

