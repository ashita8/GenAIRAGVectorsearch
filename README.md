# Semantic RAG & Vector Search Assessment

A local Retrieval-Augmented Generation (RAG) pipeline implementing semantic search, vector retrieval, query expansion, and benchmarking.

## Overview

This project demonstrates:

- Semantic document retrieval using embeddings
- Local vector search using FAISS
- Query expansion for retrieval enhancement
- Mocked Vertex AI SDK components
- Benchmarking of retrieval strategies
- Pytest-based validation

The system compares two retrieval approaches:

### Strategy A — Raw Vector Search
Direct embedding similarity search using the original user query.

### Strategy B — AI-Enhanced Retrieval
Query rewriting/expansion before semantic search to improve retrieval quality.

---

# Architecture

```text
User Query
   ↓

Strategy A:
Direct Embedding Search
   ↓
FAISS Similarity Search
   ↓
Top K Results

--------------------------------

Strategy B:
Query Expansion
   ↓
Enhanced Semantic Query
   ↓
Embedding Generation
   ↓
FAISS Similarity Search
   ↓
Top K Results
```

---

# Tech Stack

| Component | Technology |
|---|---|
| Embeddings | sentence-transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| Testing | pytest |
| Language | Python 3 |

---

# Project Structure

```text
app/
├── benchmark/
├── data/
├── embedding/
├── mocks/
├── retrieval/
└── vectordb/

tests/
```

---

# Setup

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Main Application

```bash
python -m app.main
```

---

# Run Benchmark

```bash
python -m app.benchmark.benchmark_runner
```

---

# Run Tests

```bash
python -m pytest
```

---

# Similarity Metric Choice

The project uses cosine similarity for semantic retrieval.

Embeddings are normalized before indexing, allowing FAISS Inner Product search (`IndexFlatIP`) to behave as cosine similarity.

Cosine similarity is preferred over Euclidean distance for semantic embeddings because it focuses on directional similarity between vectors rather than magnitude.

---

# Mocked Vertex AI Components

The following Vertex AI SDK components are mocked:

- `TextEmbeddingModel`
- `GenerativeModel`

The query expansion layer simulates LLM-powered semantic query rewriting using deterministic rule-based expansion.

This design keeps the benchmark reproducible and fully local.

---

# Production Migration to Vertex AI Vector Search

In production, this system could migrate to Google Cloud Vertex AI Matching Engine by:

1. Replacing local FAISS indexing with Vertex AI Vector Search indexes
2. Replacing local embeddings with Vertex AI `textembedding-gecko`
3. Replacing mocked query expansion with Gemini models
4. Deploying retrieval services behind scalable APIs
5. Storing embeddings in managed vector indexes

---

# Benchmark Goal

The benchmark demonstrates how AI-enhanced query expansion improves semantic retrieval quality compared to direct vector search.