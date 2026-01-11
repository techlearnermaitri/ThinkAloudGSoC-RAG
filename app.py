import gradio as gr
import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -------------------
# Load transcripts safely
# -------------------
TRANSCRIPT_DIR = "data/transcripts"
all_sentences = []

if os.path.exists(TRANSCRIPT_DIR):
    for fname in os.listdir(TRANSCRIPT_DIR):
        if fname.endswith("_task-thinkaloud_transcript.txt"):
            path = os.path.join(TRANSCRIPT_DIR, fname)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                # Split into sentences
                all_sentences.extend([s.strip() for s in text.split('.') if s])
else:
    print(f"Warning: {TRANSCRIPT_DIR} does not exist. Please run download_dataset.py first.")

if not all_sentences:
    print("No transcripts found. The chatbot will not work until you download the dataset.")

# -------------------
# Embeddings
# -------------------
if all_sentences:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(all_sentences, convert_to_numpy=True)

    # -------------------
    # FAISS index
    # -------------------
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # -------------------
    # Chatbot function
    # -------------------
    def respond(message, history):
        q_vec = model.encode([message], convert_to_numpy=True)
        D, I = index.search(q_vec, k=3)  # top 3 similar sentences
        context = "\n".join([all_sentences[i] for i in I[0]])
        reply = f"🧠 Relevant transcript context:\n{context}"
        return history + [(message, reply)]

    # -------------------
    # Launch Gradio
    # -------------------
    gr.ChatInterface(respond).launch(server_name="0.0.0.0", server_port=10000)
else:
    print("No transcripts loaded. Please check your dataset folder.")
