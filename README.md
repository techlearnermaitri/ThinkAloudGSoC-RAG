<<<<<<< HEAD
InsightPop: Agentic RAG for KnowledgeSpace
InsightPop is an intelligent AI agent designed for KnowledgeSpace, facilitating cross-document QA and deep research. By leveraging Retrieval-Augmented Generation (RAG), it transforms static research papers and metadata into a dynamic, conversational knowledge base.


Problem Statement
All research generates massive volumes of complex literature and data. Finding specific, cross-referenced information across diverse datasets is manually intensive. InsightPop solves this by:

Bridging Data Silos: Querying across multiple documents simultaneously.

Ensuring Accuracy: Using RAG to ground LLM responses 
\System Architecture
The system follows a modular RAG pipeline integrated into the Google Cloud ecosystem:

Ingestion: Documents are chunked and embedded into high-dimensional vectors.

Retrieval: LangGraph agents decide whether to query Elasticsearch or Vertex AI Vector Search.

Augmentation: Top-k relevant snippets are fused with the user query.

Generation: Gemini 1.5 Pro (or similar) generates a grounded, scientific response.

Tech Stack:

Layer,Technology
Backend,"Python, FastAPI"
AI Orchestration,"LangChain, LangGraph"
LLM / Embeddings,"Google Vertex AI (Gemini 2.0, Text-Embedding-004)"
Vector Store,Vertex AI Vector Search / Elasticsearch
Frontend,"React.js, TailwindCSS"
DevOps,"Docker, Google Cloud Platform (GCP)"

Installation & Setup
Prerequisites

Python 3.10+

Google Cloud Project with Vertex AI enabled

Node.js & npm (for frontend)

1. Clone & Environment
    git clone https://github.com/your-username/InsightPop.git
    cd InsightPop
2. Backend Setup
   cd backend
   pip install -r requirements.txt
   python main.py


   Usage Example
User Query: "How does dopamine regulation in the striatum differ between Parkinson's and Huntington's disease based on recent papers?"

InsightPop Response:

"Based on 4 retrieved documents from KnowledgeSpace: In Parkinson's, dopamine depletion occurs primarily in the substantia nigra... [Source: Smith et al., 2024]. Conversely, in Huntington's..."
   
   








=======
# ThinkAloudGSoC-RAG
A RAG-based AI using the ThinkAloud dataset for cognitive analysis
python3 -m venv myenv
myenv/scripts/activate
>>>>>>> ff8b6d2 (imported neccesary files and create a myenv)
