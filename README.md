# Mini Search Engine (Core Implementation)

## Objective
To implement the core components of a text search engine from scratch, focusing on inverted indexing and TF-IDF based ranking without using external search or ML libraries.

## Architecture
- Document ingestion from plain text
- Tokenization and stopword removal
- Inverted index construction
- TF-IDF weighting
- Cosine similarity based ranking

## How It Works
Each document is tokenized and indexed using an inverted index mapping terms to document IDs.
Queries are processed similarly and ranked against documents using TF-IDF scores.

## Demo
Example query and ranked output:

![Search Demo](screenshots/search_demo.png)

## Limitations
- No stemming or lemmatization
- No phrase or proximity search
- Entire index is memory-based

## Future Improvements
- Disk-based indexing
- Phrase search support
- Query caching
- Performance benchmarking
