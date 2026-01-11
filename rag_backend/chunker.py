import os
import math

def chunk_text(text, chunk_size=1000, overlap=200):
    """
    Splits text into chunks of chunk_size with optional overlap.
    """
    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # overlap ensures context continuity

    return chunks

def save_chunks(chunks, filename):
    os.makedirs("data/chunks", exist_ok=True)
    base_name = os.path.splitext(filename)[0]
    chunk_paths = []

    for i, chunk in enumerate(chunks):
        path = f"data/chunks/{base_name}_chunk_{i}.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(chunk)
        chunk_paths.append(path)

    return chunk_paths

