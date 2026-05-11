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

This project uses **Cosine Similarity** for semantic retrieval.

The embedding vectors are normalized before indexing, allowing FAISS Inner Product search (`IndexFlatIP`) to behave equivalently to cosine similarity.

## Why Cosine Similarity?

Cosine similarity measures the angle between embedding vectors rather than their absolute distance. This is particularly effective for semantic search because sentence embeddings primarily encode meaning through vector direction instead of magnitude. :contentReference[oaicite:0]{index=0}

Advantages of cosine similarity for semantic retrieval:

- Better semantic comparison for high-dimensional embeddings
- Less sensitive to vector magnitude differences
- Works well for varying sentence lengths
- Commonly used with transformer-based embeddings
- Preferred for semantic search and Retrieval-Augmented Generation systems

The cosine similarity score ranges from:
- `1` → highly similar semantic meaning
- `0` → unrelated content
- `-1` → opposite semantic meaning

---

## Why Not Euclidean Distance?

Euclidean distance measures the straight-line distance between vectors in embedding space.

While Euclidean distance can still work for vector search, it is generally less suitable for semantic retrieval because it is sensitive to vector magnitude and high-dimensional scaling effects. :contentReference[oaicite:1]{index=1}

In semantic embeddings:
- Two vectors may represent similar meaning even if their magnitudes differ
- Cosine similarity focuses only on semantic orientation
- Euclidean distance can become less interpretable in high-dimensional vector spaces

For normalized embeddings, cosine similarity and Euclidean distance produce equivalent rankings mathematically, but cosine similarity remains more interpretable for semantic relevance scoring. :contentReference[oaicite:2]{index=2}

---

# Production Migration to Vertex AI Vector Search

In production, this architecture could be migrated to Google Cloud Vertex AI Vector Search (Matching Engine) for scalable distributed semantic retrieval.

## Proposed Migration Architecture

```text
User Query
   ↓
Gemini / Query Expansion Layer
   ↓
Vertex AI Embedding Model (textembedding-gecko)
   ↓
Vertex AI Vector Search Index
   ↓
Top-K Semantic Retrieval
   ↓
RAG Application / API Layer
```

---

## Migration Steps

### 1. Replace Local Embeddings

Current local model:

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

Production replacement:

```python
vertexai.language_models.TextEmbeddingModel
```

using Vertex AI `textembedding-gecko`.

---

### 2. Replace Local FAISS Index

Current implementation uses:

```python
faiss.IndexFlatIP
```

Production deployment would use:

- Vertex AI Vector Search indexes
- Approximate Nearest Neighbor (ANN) retrieval
- Managed distributed vector infrastructure

This enables:
- low-latency large-scale retrieval
- horizontal scaling
- managed index updates
- high availability

---

### 3. Replace Mock Query Expansion

Current implementation uses a mocked deterministic query expansion layer.

Production architecture would replace this with:
- Gemini models
- prompt-based query rewriting
- semantic reformulation pipelines

This would improve retrieval recall and semantic understanding.

---

### 4. Deploy Retrieval API Layer

The retrieval system could be exposed through:
- FastAPI
- Cloud Run
- GKE
- API Gateway

allowing scalable Retrieval-Augmented Generation workflows.

---

### 5. Add Production Enhancements

Additional production improvements could include:

- hybrid retrieval (BM25 + vector search)
- reranking models
- metadata filtering
- document chunking pipelines
- embedding caching
- observability and tracing
- index versioning
- asynchronous ingestion pipelines

---

## Why Vertex AI Vector Search?

Vertex AI Matching Engine is designed for:
- billion-scale vector search
- low-latency ANN retrieval
- managed infrastructure
- distributed semantic retrieval workloads

It provides a production-ready managed alternative to local FAISS-based indexing.

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