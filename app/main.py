from embedding.embedder import Embedder

def main():
    embedder = Embedder()

    text = "Kubernetes automatically scales pods during high traffic."

    embedding = embedder.embed_text(text)

    print("Embedding shape:", embedding.shape)
    print("First 5 values:", embedding[:5])


if __name__ == "__main__":
    main()