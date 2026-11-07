# Generative and Agentic AI with Arif Butt

[![Course](https://img.shields.io/badge/Course-GenAI%20%26%20Agentic%20AI-blue.svg)](http://arifbutt.me/cources)
[![Notebooks](https://img.shields.io/badge/Notebooks-56-informational.svg)](#-lecture-catalog)
[![Python](https://img.shields.io/badge/Python-3.12-yellow.svg)](https://www.python.org/downloads/)
[![Package Manager](https://img.shields.io/badge/env-uv-purple.svg)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#-license)

The companion repository of the **Generative and Agentic AI** course by Dr. Muhammad Arif Butt (Department of Data Science, University of the Punjab). It contains **56 hands-on Jupyter notebooks** (Lec_00 to Lec_54, plus Lec_11A) that take you from your first API call to a large language model, through the internals of Transformers, fine-tuning and Retrieval-Augmented Generation, all the way to building, securing, deploying and connecting AI agents with MCP, skills, sub-agents, the A2A protocol and agent frameworks.

Every notebook is self-contained, runs top to bottom, and uses **free tiers wherever possible** (Groq, Hugging Face, Google AI Studio, OpenRouter).

---

## 📑 Table of Contents

1. [What You Will Learn](#-what-you-will-learn)
2. [Lecture Catalog](#-lecture-catalog)
3. [Repository Structure](#-repository-structure)
4. [Prerequisites](#-prerequisites)
5. [Quick Start (TL;DR)](#-quick-start-tldr)
6. [Detailed Setup](#-detailed-setup)
7. [API Keys: Accounts and Setup](#-api-keys-accounts-and-setup)
8. [Optional Tools for Specific Lectures](#-optional-tools-for-specific-lectures)
9. [Running the Notebooks on Google Colab](#-running-the-notebooks-on-google-colab)
10. [Free Tiers, Rate Limits and Shared Servers](#-free-tiers-rate-limits-and-shared-servers)
11. [Daily Workflow](#-daily-workflow)
12. [Troubleshooting](#-troubleshooting)
13. [Learning Approach](#-learning-approach)
14. [Meet Your Instructor](#-meet-your-instructor)
15. [License](#-license)

---

## 🎯 What You Will Learn

The course is organized in eleven parts. Each part builds on the previous one.

| Part | Lectures | Theme | Highlights |
|:--:|:--|:--|:--|
| 0 | Lec_00 | **Lab set-up** | `uv`, the course environment, hardware and library health checks |
| 1 | Lec_01 – Lec_04 | **Frontier models and prompting** | OpenAI, Anthropic and Google SDKs; prompt and context engineering; prompt injection |
| 2 | Lec_05 – Lec_12, Lec_11A | **Open-source models and LLM apps** | Colab, Hugging Face Hub, Groq/HF/OpenRouter routers, Ollama, Gradio, HF Spaces, conversational agents, coding agents, `transformers.pipeline()` |
| 3 | Lec_13 – Lec_15 | **Multi-modality and evaluation** | image, audio and video in and out; metrics, benchmarks and leaderboards |
| 4 | Lec_16 – Lec_21 | **Under the hood** | tokenization, embeddings, neural network recap, the Transformer architecture, KV cache, MoE, `AutoModel` |
| 5 | Lec_22 – Lec_26 | **Fine-tuning** | LoRA, quantization, QLoRA; fine-tuning TinyLlama with PEFT, TRL and Unsloth |
| 6 | Lec_27 – Lec_29 | **Databases** | SQL, NoSQL and vector databases: MySQL, SQLite, MongoDB, ChromaDB |
| 7 | Lec_30 – Lec_38 | **LangChain and RAG** | models, prompts, memory, chains, loaders, splitters, vector stores, retrievers; vectorized and vectorless RAG |
| 8 | Lec_39 – Lec_43 | **AI agents and their safety** | from LLM apps to agents, tool calling, ReAct; permissions, guardrails, hooks; sandboxing with containers and microVMs |
| 9 | Lec_44 – Lec_48 | **Model Context Protocol (MCP)** | MCP in Claude Desktop, MCP concepts, building and deploying MCP servers, MCP clients in Python, deploying an agent as a web service |
| 10 | Lec_49 – Lec_54 | **Skills, multi-agent systems and frameworks** | agent skills, sub-agents and the A2A protocol; LangChain agents, Deep Agents and the OpenAI Agents SDK |

```mermaid
flowchart LR
    A["Part 0-1<br/>Set-up and<br/>frontier models"] --> B["Part 2-3<br/>Open-source models,<br/>apps, multi-modality"]
    B --> C["Part 4-5<br/>Transformers and<br/>fine-tuning"]
    C --> D["Part 6-7<br/>Databases, LangChain<br/>and RAG"]
    D --> E["Part 8<br/>AI agents and<br/>agent safety"]
    E --> F["Part 9<br/>MCP"]
    F --> G["Part 10<br/>Skills, multi-agent,<br/>A2A, frameworks"]
```

### 🔗 Course Resources

- **Lecture slides:** <http://arifbutt.me/cources>
- **Video lectures:** [Learn with Arif on YouTube](https://youtube.com/learnwitharif)
- **Level:** undergraduate and graduate
- **Language:** Python 3.12

---

## 📚 Lecture Catalog

All notebooks live in [`Notebooks/`](Notebooks). The **Keys** column lists the API keys a notebook reads from `keys/.env` (see [API Keys](#-api-keys-accounts-and-setup)); a dash means none.

### Part 0 and 1: Set-up, Frontier Models and Prompting

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 00 | [Setting up Lab Environment](Notebooks/Lec_00_%28Setting_up_Lab_Environment%29.ipynb) | Jupyter recap, building the course environment with `uv`, hardware check, a 51-library health check, the road from LLM apps to agentic systems | – |
| 01 | [Hello to OpenAI Text-Based Models](Notebooks/Lec_01_%28Hello_to_OpenAI_Text_Based_Models%29.ipynb) | The OpenAI SDK and the `Responses` API, its arguments, hands-on examples | OpenAI |
| 02 | [Hello to Anthropic Text-Based Models](Notebooks/Lec_02_%28Hello_to_Anthropic_Text_Based_Models%29.ipynb) | The Anthropic SDK and the Claude family of models | Anthropic |
| 03 | [Hello to Google Text-Based Models](Notebooks/Lec_03_%28Hello_to_Google_Text_Based_Models%29.ipynb) | The Google Gen AI SDK and the Gemini family of models | Google |
| 04 | [Prompt Engineering and Injection Attacks](Notebooks/Lec_04_%28Prompt_Engineering_Injection_Attacks%29.ipynb) | Prompt and context engineering, prompt templates, zero/one/few-shot, reasoning models, CoT and ToT, anti-hallucination techniques, prompt injection | OpenAI |

### Part 2: Open-Source Models and LLM Apps

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 05 | [A Hello to Google Colab](Notebooks/Lec_05_%28A_Hello_to_Google_Colab%29.ipynb) | GPU platforms, Google Colab, secrets in Colab, opening notebooks from GitHub and Google Drive | – |
| 06 | [A Walk-Through of the Hugging Face Hub](Notebooks/Lec_06_%28A_Walk_Through_of_Hugging_Face_Hub%29.ipynb) | The Hugging Face ecosystem: models, datasets, Spaces and Buckets | HF |
| 07 | [Accessing OS LLMs via Groq, HF and OpenAI-Compatible APIs](Notebooks/Lec_07_%28Accessing_OS_LLMs_via_Groq_HF_OpenAI_Inference_API%29.ipynb) | The Hugging Face router, Groq and OpenRouter, with native SDKs and the OpenAI Chat Completions and Responses APIs | Groq, HF, OpenRouter |
| 08 | [Accessing OS LLMs using Ollama](Notebooks/Lec_08_%28Accessing_OS_LLMs_using_Ollama%29.ipynb) | Local LLM runtimes, Ollama GUI/CLI/API, agent harnesses on Ollama, GGUF and llama.cpp, vLLM and AirLLM, building your own inference server | – |
| 09 | [Developing LLM Apps using Gradio](Notebooks/Lec_09_%28Developing_LLM_Apps_using_Gradio%29.ipynb) | Gradio components and twelve LLM apps: Q/A bots on files, papers, YouTube transcripts and web pages | Groq, Anthropic |
| 10 | [Deploying LLM Apps on HF Spaces](Notebooks/Lec_10_%28Deploying_LLM_Apps_on_HF_Spaces%29.ipynb) | Deploying Gradio apps on Hugging Face Spaces and Render; AI-based security apps (traffic, malware and phishing classifiers) | Groq, HF |
| 11 | [Designing Conversational AI Agents](Notebooks/Lec_11_%28Designing_Conversational_AI_Agents%29.ipynb) | Stateless vs. stateful chatbots with the Chat Completions and Responses APIs, short- and long-term memory | OpenAI |
| 11A | [Coding Agents](Notebooks/Lec_11A_%28Coding_Agents%29.ipynb) | Agentic coding assistants, Claude Code, slash commands, context management, `CLAUDE.md`, the `.claude/` directory, spec-driven development | – |
| 12 | [Accessing OS LLMs using HF Transformers Pipeline](Notebooks/Lec_12_%28Accessing_OS_LLMs_using_HF_Transformers_Pipeline%29.ipynb) | `transformers.pipeline()` for NLP tasks and chat templates | – |

### Part 3: Multi-Modality and Evaluation

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 13 | [Multi-Modality of AI Models I](Notebooks/Lec_13_%28Multi_Modality_of_AI_Models_I%29.ipynb) | Image understanding, classification, generation and segmentation | OpenAI, Anthropic, Google, Groq, HF |
| 14 | [Multi-Modality of AI Models II](Notebooks/Lec_14_%28Multi_Modality_of_AI_Models_II%29.ipynb) | Speech recognition and generation, cross-modal chaining, video generation and understanding | OpenAI, Anthropic, Google, Groq, HF |
| 15 | [From ML Metrics to LLM Evaluation](Notebooks/Lec_15_%28From_ML_Metrics_to_LLM_Evaluation_Benchmarks_and_Leaderboards%29.ipynb) | Choosing a model, scaling laws, classical metrics, why LLM evaluation differs, evaluation tiers, benchmarks and leaderboards | OpenAI |

### Part 4: Under the Hood

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 16 | [Hands-on Tokenization](Notebooks/Lec_16_%28Hands_on_Understanding_of_Tokenization%29.ipynb) | Classical and LLM tokenizers, Hugging Face tokenizers for base and chat models | – |
| 17 | [Hands-on Vectorization](Notebooks/Lec_17_%28Hands_on_Understanding_of_Vectorization%29.ipynb) | Frequency- and prediction-based vectorization, SentenceTransformers and OpenAI embeddings, t-SNE | OpenAI |
| 18 | [Recap of Deep Neural Networks](Notebooks/Lec_18_%28Recap_of_Deep_Neural_Networks%29.ipynb) | Deep learning architectures, gradient descent, MLPs, how LLMs are pre-trained | – |
| 19 | [A Deep Dive into Transformers I](Notebooks/Lec_19_%28A_Deep_Dive_into_Transformer_Architecture-I%29.ipynb) | Encoder and decoder stacks, GPT vs. BERT, decoder-only models, positional encoding | – |
| 20 | [A Deep Dive into Transformers II](Notebooks/Lec_20_%28A_Deep_Dive_into_Transformer_Architecture-II%29.ipynb) | Layer normalization, the LM head, KV cache, Mixture of Experts | – |
| 21 | [Load and Run OS LLMs with AutoModel](Notebooks/Lec_21_%28Load_and_Run_OS_LLMs_using_AutoModel_and_AutoTokenizer%29.ipynb) | Inside a downloaded model; inference with `pipeline()`, `generate()` and a manual forward pass | – |

### Part 5: Fine-Tuning

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 22 | [Fine-Tuning LLMs I](Notebooks/Lec_22_%28Fine_Tuning_LLMs_I%29.ipynb) | Pre-training vs. fine-tuning, fine-tuning strategies, a deep dive into LoRA | – |
| 23 | [Fine-Tuning LLMs II](Notebooks/Lec_23_%28Fine_Tuning_LLMs_II%29.ipynb) | Quantization (INT8, INT4, NF4), QLoRA, paged optimizers, memory comparisons | – |
| 24 | [Fine-Tuning with PEFT](Notebooks/Lec_24_%28FineTuning_PEFT%29.ipynb) | Fine-tuning TinyLlama with LoRA adapters using PEFT | HF |
| 25 | [Fine-Tuning with TRL](Notebooks/Lec_25_%28FineTuning_TRL%29.ipynb) | Dataset curation, training with TRL, pushing adapters and merged models to the Hub, GGUF for Ollama and llama.cpp | HF |
| 26 | [Fine-Tuning with Unsloth](Notebooks/Lec_26_%28FineTuning_Unsloth%29.ipynb) | The same pipeline, faster and leaner with Unsloth | HF |

> Lec_24 to Lec_26 train a model and need an NVIDIA GPU: use your own machine or a free T4 GPU on Google Colab.

### Part 6: Databases

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 27 | [Modern DB Landscape](Notebooks/Lec_27_%28Modern_DB_Landscape%29.ipynb) | SQL, NoSQL and vector databases; hands-on MySQL and SQLite | – |
| 28 | [Hands-on MongoDB](Notebooks/Lec_28_%28Hands_on_MongoDB%29.ipynb) | MongoDB via `mongosh`, Compass, `pymongo` and MongoDB Atlas | – |
| 29 | [Hands-on ChromaDB](Notebooks/Lec_29_%28Hands_on_ChromaDB%29.ipynb) | Vector databases, ChromaDB with custom embeddings, CRUD operations, storage structure, GUI tools | OpenAI |

### Part 7: LangChain and Retrieval-Augmented Generation

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 30 | [LangChain and its Models Component](Notebooks/Lec_30_%28Overview_of_LangChain_and_its_Models_Component%29.ipynb) | Why LangChain, closed- and open-source chat models, images in and out, embedding models | Groq, OpenRouter (OpenAI, Anthropic, Google optional) |
| 31 | [LangChain Prompts](Notebooks/Lec_31_%28LangChain_Prompts_Components%29.ipynb) | `PromptTemplate` and `ChatPromptTemplate` | Groq |
| 32 | [LangChain Memory](Notebooks/Lec_32_%28LangChain_Memory_Components%29.ipynb) | Short-term memory, trimming history, many users, persistence, long-term memory | Groq |
| 33 | [LangChain Chains](Notebooks/Lec_33_%28LangChain_Chains_Component%29.ipynb) | LCEL chains, output parsers, sequential/parallel/branching chains, robust chains | Groq, OpenRouter |
| 34 | [LangChain Document Loaders](Notebooks/Lec_34_%28LangChain_Document_Loaders%29.ipynb) | The `Document` object; loading files, web pages, big files and databases; custom loaders | – |
| 35 | [LangChain Text Splitters](Notebooks/Lec_35_%28LangChain_Text_Splitters%29.ipynb) | Chunking by length, text structure, document structure and meaning | Groq |
| 36 | [LangChain and Vector DBs](Notebooks/Lec_36_%28LangChain_and_Vector_DBs%29.ipynb) | Vector stores, the indexing pipeline, choosing a vector store | – |
| 37 | [LangChain Retrievers](Notebooks/Lec_37_%28LangChain_Retrievers%29.ipynb) | Vector-store and other retrievers, query rewriting, re-ranking, keyword and hybrid search | Groq |
| 38 | [Vectorized vs. Vectorless RAG](Notebooks/Lec_38_%28Vectorized_vs_Vectorless_RAG%29.ipynb) | Naive and advanced RAG, a complete RAG pipeline, two ready-to-use RAG apps, vectorless RAG | Groq |

### Part 8: AI Agents and Agent Safety

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 39 | [From GenAI Apps to AI Agents](Notebooks/Lec_39_%28From_GenAI_Apps_to_AI_Agents%29.ipynb) | LLM apps, workflow design patterns, an AI agent with the ReAct loop | Groq |
| 40 | [Agentic AI and Tool Calling I](Notebooks/Lec_40_%28Agentic_AI_and_Tool_Calling-I%29.ipynb) | What a tool is, the tool-call workflow, hosted built-in tools of OpenAI, Groq and OpenRouter, computer use and browser automation | Groq, OpenAI, OpenRouter |
| 41 | [Agentic AI and Tool Calling II](Notebooks/Lec_41_%28Agentic_AI_and_Tool_Calling-II%29.ipynb) | Custom function tools step by step, a weather tool, a ReAct agent with native tool calling (Agent = Model + Harness) | Groq, Weather |
| 42 | [Agent Permissions and Guardrails](Notebooks/Lec_42_%28Agent_Permissions_and_Guardrails%29.ipynb) | Dangerous tools with human approval, an attack lab, hardening the harness with guardrails and hooks | Groq, OpenAI |
| 43 | [Sandboxing Agents: Containers and MicroVMs](Notebooks/Lec_43_%28Sandboxing_Agents_Containers_and_MicroVMs%29.ipynb) | What a sandbox is, a vulnerable agent inside a Docker container and inside a microVM sandbox, agentic security threats | Groq |

### Part 9: Model Context Protocol (MCP)

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 44 | [Accessing MCP Servers in Claude Desktop](Notebooks/Lec_44_%28Accessing_MCP_Servers_in_Claude_Desktop%29.ipynb) | MCP clients and servers, the Claude ecosystem, remote and local MCP servers in Claude Desktop, Claude Desktop with Ollama-hosted models | – |
| 45 | [Conceptual Understanding of MCP](Notebooks/Lec_45_%28Conceptual_Understanding_of_Model_Context_Protocol%29.ipynb) | Agentic protocols, why MCP, its architecture, transports, primitives, and communication life cycle | – |
| 46 | [Creating, Deploying and Accessing your own MCP Servers](Notebooks/Lec_46_%28Creating_Deploying_and_Accessing_your_own_MCP_Servers%29.ipynb) | Building an MCP server with FastMCP, the MCP Inspector, deploying on Render, flight- and hotel-search servers | – |
| 47 | [Accessing MCP Servers from Python](Notebooks/Lec_47_%28Accessing_Local_and_Remote_MCP_Servers_from_Python%29.ipynb) | Your program as the MCP host: local and remote servers, the low-level `mcp` SDK, an MCP-powered agent, provider-side MCP | Groq (OpenAI, Anthropic, HF optional) |
| 48 | [Deploy an Agent on Render](Notebooks/Lec_48_%28Deploy_Agent_on_Render_Access_from_Python%29.ipynb) | Turning an agent into a FastAPI web service, testing it locally, deploying it on Render, calling it from Python, production readiness | Groq |

### Part 10: Skills, Multi-Agent Systems and Agent Frameworks

| Lec | Notebook | What you learn | Keys |
|:--:|:--|:--|:--|
| 49 | [Extending AI Agents with Skills](Notebooks/Lec_49_%28Extending_AI_Agents_with_Skills%29.ipynb) | Agent skills and progressive disclosure, writing skills, skills in Claude Desktop, adding skill support to your own agent, skills vs. tools vs. MCP | Groq |
| 50 | [Sub-Agents and Multi-Agent Systems](Notebooks/Lec_50_%28Sub_Agents_and_multi_agent_systems%29.ipynb) | Sub-agents from scratch, orchestrators, parallel sub-agents, handoffs; the **A2A protocol** (v1.0): Agent Cards, Tasks, Messages, Artifacts, an A2A server and client from scratch and with the official `a2a-sdk` | Groq |
| 51 | [Building AI Agents using LangChain I](Notebooks/Lec_51_%28Building_AI_Agents_using_LangChain_Part_I%29.ipynb) | `create_agent()`: models, system prompts, tools, memory, images and audio, MCP servers, runtime context | Groq, Weather (HF optional) |
| 52 | [Building AI Agents using LangChain II](Notebooks/Lec_52_%28Building_AI_Agents_using_LangChain_Part_II%29.ipynb) | Middleware: long conversations, human approval, guardrails, dynamic agents, skills, sub-agents; a coding agent in one `create_agent()` | Groq, Weather |
| 53 | [Building Deep Agents using LangChain](Notebooks/Lec_53_%28Building_Deep_Agents_using_LangChain%29.ipynb) | Deep agents: execution environments, context management, delegation and steering | – |
| 54 | [Building AI Agents using OpenAI Agents SDK](Notebooks/Lec_54_%28Building_AI_Agents_using_OpenAI_Agents_SDK%29.ipynb) | The OpenAI Agents SDK: agents, tools, memory, MCP, runtime context, human approval, guardrails, skills, agents as tools and handoffs | Groq, Weather (HF optional) |

---

## 📁 Repository Structure

```
📦 Generative-and-Agentic-AI
├── 📂 Notebooks/                 # The 56 lecture notebooks (Lec_00 … Lec_54, plus Lec_11A)
│   ├── 📂 mcp_demo_server/       # Lec_46: the course's own MCP server (FastMCP), deployed on Render
│   ├── 📂 agent_service/         # Lec_48: an AI agent served with FastAPI and deployed on Render
│   ├── 📂 a2a_agents/            # Lec_50: A2A servers, from scratch and with the official a2a-sdk
│   └── 📄 requirements.txt       # pip / Google Colab alternative to uv (exported from uv.lock)
├── 📂 data/                      # Datasets, documents and files that the notebooks read
│   ├── 📂 audio/                 # Audio samples for the multi-modality lectures
│   └── 📂 attack_lab_lec42_43/   # The (fake-secret) attack lab of Lec_42 and Lec_43
├── 📂 images/                    # Figures embedded in the notebooks
├── 📂 Books/                     # Reference books
├── 📂 Research Articles/         # Supplementary reading
├── 📂 keys/                      # ⚠️ YOU create this: your .env with API keys (git-ignored)
├── 📄 pyproject.toml             # Project manifest: every library the course needs
├── 📄 uv.lock                    # Exact versions of all dependencies, for every platform
├── 📄 .python-version            # Pins the interpreter to Python 3.12
└── 📄 README.md                  # This file
```

> **Note:** The `keys/` folder is **not** in the repository: it is listed in `.gitignore` so that nobody ever commits their secrets. You create it yourself in [Step 4](#step-4-create-your-api-keys-file). Some notebooks also create working folders and files of their own (for example skill folders, sandboxes and server logs) and clean them up at the end.

---

## ✅ Prerequisites

**Knowledge**
- Programming in Python
- Hands-on understanding of machine learning
- Deep learning concepts are a plus

**Machine**
- macOS, Linux or Windows
- **About 10 GB of free disk space** (PyTorch and the ML stack are large)
- A reasonable internet connection for the first install
- `git`: check with `git --version`, otherwise install it from <https://git-scm.com/downloads>

> **You do NOT need Python pre-installed.** `uv` downloads and manages the correct Python 3.12 interpreter for you.

---

## 🚀 Quick Start (TL;DR)

```bash
# 1. Install uv (macOS / Linux; see Step 1 for Windows)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone the repository
git clone --depth 1 https://github.com/arifpucit/Generative-and-Agentic-AI.git
cd Generative-and-Agentic-AI

# 3. Build the environment (downloads Python 3.12 and all libraries)
uv sync

# 4. Create your keys file, then paste your API keys into it (see Step 4)
mkdir -p keys && touch keys/.env

# 5. Launch Jupyter Lab
uv run jupyter lab

# 6. Open Notebooks/Lec_00_(Setting_up_Lab_Environment).ipynb and run all cells
```

Each step is explained below.

---

## 🔧 Detailed Setup

### Step 1: Install `uv`

**`uv`** is a fast Python package and project manager written in Rust. It replaces `pip`, `venv`, `pyenv` and `virtualenv` with a single tool, and downloads Python interpreters for you.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close and reopen your terminal**, then check:

```bash
uv --version
```

If the command is not found, your terminal has not picked up the new `PATH` yet: open a fresh one. To upgrade `uv` later, run `uv self update`.

---

### Step 2: Clone the Repository

The repository also contains books, research articles and many figures, so its full history is large. Cloning only the latest snapshot is much faster:

```bash
git clone --depth 1 https://github.com/arifpucit/Generative-and-Agentic-AI.git
cd Generative-and-Agentic-AI
```

Drop `--depth 1` if you want the complete history. Three files drive the next step:

| File | Purpose |
|:--|:--|
| `pyproject.toml` | The project manifest: every library this course needs |
| `uv.lock` | The lock file: the *exact* version of every direct and indirect dependency, on every platform |
| `.python-version` | Pins the interpreter to Python 3.12 |

---

### Step 3: Build the Virtual Environment

One command creates the virtual environment and installs everything:

```bash
uv sync
```

Because the repository ships `pyproject.toml` and `uv.lock`, `uv sync`:

1. downloads Python 3.12 if it is not on your machine yet,
2. creates a virtual environment in a hidden `.venv/` folder inside the project,
3. installs every dependency at its locked version.

> ⏳ **Be patient the first time.** It downloads several GB of ML libraries (PyTorch, Transformers, the CUDA runtime on Linux and Windows, ...) and can take **5 to 20 minutes**. Later runs are almost instant, because `uv` caches everything.

**Check the environment:**

```bash
uv run python -c "import torch, transformers, langchain; print('OK', torch.__version__)"
```

> **Why `uv sync` and not `pip install -r requirements.txt`?** `uv sync` installs from the lock file, so every student gets identical versions, and "it works on my machine" really transfers to yours. It is also much faster. `Notebooks/requirements.txt` is there for Google Colab and pip users (see [Running on Google Colab](#-running-the-notebooks-on-google-colab)).

---

### Step 4: Create Your API Keys File

Notebooks that call a hosted model load their secrets with:

```python
load_dotenv("../keys/.env", override=True)
```

Since the notebooks live in `Notebooks/`, that path is **`keys/.env` at the root of the repository**. The `keys/` folder is git-ignored, so it is not part of the clone: **create it yourself**.

```bash
# From the root of the repository
mkdir -p keys
touch keys/.env
```

Open `keys/.env` in a text editor and paste this template, replacing each placeholder with your own key. You only need the keys of the lectures you run (see the next section).

```ini
# ==========================================================
#  Generative and Agentic AI: API Keys
#  File location: <repo-root>/keys/.env
#  NEVER commit this file. It is already excluded by .gitignore
# ==========================================================

# --- Free tiers: enough for most of the course -------------
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WEATHER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# --- Paid (pre-paid credits) -------------------------------
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# --- Optional: only for the deployment lectures ------------
# DEMO_SERVER_URL=https://<your-mcp-server>.onrender.com/mcp   # Lec_47, 51, 52, 54 (default: the course's Demo-server)
# MCP_API_TOKEN=<token-of-your-mcp-server>                      # Lec_47, only if your MCP server has a token
# AGENT_URL=https://<your-agent-service>.onrender.com          # Lec_48 (default: the local service)
# AGENT_API_TOKEN=<token-of-your-agent-service>                # Lec_48 (default: my-class-token)
```

**Formatting rules for `.env` files**
- No spaces around `=`: `GROQ_API_KEY=gsk_...` ✅, not `GROQ_API_KEY = gsk_...` ❌
- No quotes around the value (unless it contains spaces)
- One key per line
- Variable names are case-sensitive and must match **exactly**

**Check that your keys are read:**

```bash
uv run python -c "
from dotenv import load_dotenv; import os
load_dotenv('keys/.env', override=True)
for k in ['GROQ_API_KEY','HF_TOKEN','GOOGLE_API_KEY','OPENROUTER_API_KEY','WEATHER_API_KEY','OPENAI_API_KEY','ANTHROPIC_API_KEY']:
    v = os.getenv(k)
    print(f'{k:<20}', 'OK  ' + v[:8] + '...' if v else 'MISSING')
"
```

> 🔐 **Keep your API keys out of git.** Never paste a key into a notebook cell, and never commit `keys/.env`. If a key is ever exposed, revoke it immediately in the provider's dashboard and create a new one.

---

### Step 5: Launch Jupyter Lab

Start Jupyter Lab **through `uv`**, so that it runs inside the project environment:

```bash
uv run jupyter lab
```

Jupyter Lab opens in your browser. Go into the **`Notebooks/`** folder.

**Kernel:** Jupyter Lab is installed *inside* the project environment, so the default **Python 3 (ipykernel)** kernel already uses it and sees every course library. You do not need to register a kernel. If you are asked to choose one, pick **Python 3 (ipykernel)**.

> Prefer VS Code? Open the repository folder, open a notebook, and select the interpreter in `.venv/` as the kernel.

---

### Step 6: Verify Everything with Lec_00

Open **`Notebooks/Lec_00_(Setting_up_Lab_Environment).ipynb`**: it exists so that you can check your environment before Lecture 1.

- **Hardware check:** reports your CPU cores, RAM and whether an NVIDIA GPU is available. There is no "correct" output; no GPU is fine (the training lectures can run on Google Colab).
- **Environment health check:** imports 51 key libraries in 9 categories. A healthy environment ends with:

```
========================================================================
📊 OVERALL SUMMARY
========================================================================
✅ Installed: 51/51 (100.0%)
...
🎉 ENVIRONMENT READY — ALL REQUIRED LIBRARIES FOUND!
```

If a library reports `❌ NOT INSTALLED`, first re-run `uv sync` from the repository root.

---

## 🔑 API Keys: Accounts and Setup

You do **not** need every key on day one: get each one when a lecture needs it.

| # | Variable | Provider | Where to get it | Cost | Used in |
|:--|:--|:--|:--|:--|:--|
| 1 | `GROQ_API_KEY` | Groq | [console.groq.com/keys](https://console.groq.com/keys) | **Free tier** | Lec_07, 09, 10, 13, 14, 30–33, 35, 37–43, 47–52, 54 |
| 2 | `HF_TOKEN` | Hugging Face | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | **Free** | Lec_06, 07, 10, 13, 14, 24–26 (47, 51, 54 optional) |
| 3 | `GOOGLE_API_KEY` | Google AI Studio | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | **Free tier** | Lec_03, 13, 14 (30 optional) |
| 4 | `OPENROUTER_API_KEY` | OpenRouter | [openrouter.ai/keys](https://openrouter.ai/keys) | **Free models available** | Lec_07, 30, 33, 40 |
| 5 | `WEATHER_API_KEY` | WeatherAPI | [weatherapi.com](https://www.weatherapi.com/signup.aspx) | **Free tier** | Lec_41, 51, 52, 54 |
| 6 | `OPENAI_API_KEY` | OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | Paid (pre-paid credits) | Lec_01, 04, 11, 13–15, 17, 29, 40, 42 (30, 47 optional) |
| 7 | `ANTHROPIC_API_KEY` | Anthropic | [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys) | Paid (pre-paid credits) | Lec_02, 09, 13, 14 (30, 47 optional) |

> 💡 **Start with the free ones.** `GROQ_API_KEY` alone covers most of the agentic part of the course (Lec_39 to Lec_54), and together with `HF_TOKEN`, `GOOGLE_API_KEY` and `OPENROUTER_API_KEY` it covers the majority of all notebooks. Add the paid OpenAI and Anthropic keys when you reach the lectures that need them.

### How to obtain each key

<details>
<summary><b>1. Groq: free and fast inference (the most used key of the course)</b></summary>

1. Go to <https://console.groq.com> and sign up with Google, GitHub or email.
2. In the left sidebar click **API Keys** → **Create API Key**.
3. Give it a name (e.g. `genai-course`) and click **Submit**.
4. **Copy the key immediately**: it is shown only once.
5. Paste it into `keys/.env` as `GROQ_API_KEY=gsk_...`

No credit card is needed. The free tier has per-minute and per-day token limits (see [Free Tiers and Rate Limits](#-free-tiers-rate-limits-and-shared-servers)).
</details>

<details>
<summary><b>2. Hugging Face: free, for models, datasets and Spaces</b></summary>

1. Create an account at <https://huggingface.co/join>.
2. Go to **Settings → Access Tokens** (<https://huggingface.co/settings/tokens>) and click **Create new token**.
3. Choose the **Write** token type: Lec_10 (deploying to Spaces) and the fine-tuning lectures push to the Hub.
4. Name it, click **Create token** and copy it.
5. Paste it into `keys/.env` as `HF_TOKEN=hf_...`

> Some models (e.g. Llama, Gemma) are **gated**: visit the model page while logged in and accept its licence before your token can download it.
</details>

<details>
<summary><b>3. Google AI Studio: free tier for Gemini</b></summary>

1. Go to <https://aistudio.google.com/apikey> and sign in with a Google account.
2. Click **Create API key** and choose (or let it create) a Google Cloud project.
3. Paste the key into `keys/.env` as `GOOGLE_API_KEY=AIza...`

No billing is required for the course notebooks.
</details>

<details>
<summary><b>4. OpenRouter: one key for hundreds of models, many of them free</b></summary>

1. Sign up at <https://openrouter.ai>.
2. Go to **Keys** (<https://openrouter.ai/keys>) → **Create Key**, name it and copy it.
3. Paste it into `keys/.env` as `OPENROUTER_API_KEY=sk-or-v1-...`

Models whose id ends in `:free` cost nothing, with daily request limits. Lec_07 compares OpenRouter with the Groq and Hugging Face routers.
</details>

<details>
<summary><b>5. WeatherAPI: free tier for the tool-calling demos</b></summary>

1. Sign up at <https://www.weatherapi.com/signup.aspx> (free, no credit card) and verify your email.
2. Your API key is shown on the dashboard after login.
3. Paste it into `keys/.env` as `WEATHER_API_KEY=...`

It is the example external tool that the agents call in Lec_41 and the framework lectures.
</details>

<details>
<summary><b>6. OpenAI: paid, requires billing</b></summary>

1. Create an account at <https://platform.openai.com> and verify your phone number.
2. Go to **Settings → Billing**, add a payment method and buy credits (a **$5** top-up is plenty for this course).
3. Go to **API keys** → **Create new secret key**, and copy it immediately.
4. Paste it into `keys/.env` as `OPENAI_API_KEY=sk-proj-...`

> ⚠️ A ChatGPT Plus subscription does **not** include API credits: they are billed separately.
</details>

<details>
<summary><b>7. Anthropic: paid, requires credits</b></summary>

1. Create an account at <https://console.anthropic.com> and verify your email and phone number.
2. Go to **Settings → Billing** and buy credits (**$5** is enough for the course).
3. Go to **Settings → API Keys** → **Create Key**, and copy it immediately.
4. Paste it into `keys/.env` as `ANTHROPIC_API_KEY=sk-ant-...`

> ⚠️ A Claude Pro subscription does **not** include API credits: they are billed separately.
</details>

---

## 🛠️ Optional Tools for Specific Lectures

Most notebooks need nothing beyond `uv sync` and your API keys. A few lectures use software or accounts that you set up separately. Install them only when you reach those lectures.

| Tool / account | Needed for | How to get it |
|:--|:--|:--|
| **Google Colab** (free T4 GPU) | Lec_05, the training lectures Lec_24–26 | <https://colab.research.google.com> with a Google account |
| **Ollama** | Lec_08 (local LLMs), Lec_09 and Lec_11 (local models, optional), Lec_25–26 (running your fine-tuned GGUF), Lec_44 (Claude Desktop with Ollama models) | <https://ollama.com/download>, then e.g. `ollama pull llama3.2:1b` |
| **Claude Code** | Lec_11A (coding agents) | macOS/Linux: `curl -fsSL https://claude.ai/install.sh \| bash` · Windows (PowerShell): `irm https://claude.ai/install.ps1 \| iex` (see <https://code.claude.com/docs/en/setup>); needs a Claude subscription or an Anthropic Console account |
| **Claude Desktop** | Lec_44, 45, 46, 49 (MCP servers and skills in a chat app) | <https://claude.ai/download> |
| **Node.js (LTS, 22.19 or newer)** | Lec_44–46 (`npx`-based MCP servers, the MCP Inspector) | <https://nodejs.org> |
| **Docker Desktop** (or OrbStack / Colima) and Docker's **`sbx`** | Lec_43 (agents in containers and microVM sandboxes) | <https://www.docker.com/products/docker-desktop/>; `sbx`: `brew install docker/tap/sbx` (macOS) or `winget install Docker.sbx` (Windows) |
| **GitHub** and **Render** accounts | Lec_10 (Render alternative to Spaces), Lec_46 (deploying an MCP server), Lec_48 (deploying an agent service) | <https://github.com/signup>, <https://render.com> (free plan) |
| **MySQL Server** + Workbench | Lec_27 | <https://dev.mysql.com/downloads/> |
| **MongoDB** + `mongosh` + Compass | Lec_28 | [MongoDB Community Server](https://www.mongodb.com/try/download/community) on `localhost:27017`, or a free [Atlas](https://www.mongodb.com/atlas) cluster |
| **ffmpeg** | Lec_14 (audio processing) | macOS: `brew install ffmpeg` · Ubuntu/Debian: `sudo apt install ffmpeg` · Windows: [download](https://ffmpeg.org/download.html) and add it to `PATH` |
| **Playwright browser** | Lec_40 (browser automation bonus) | `uv run playwright install chromium` |
| **NLTK data** | Lec_16 (classical tokenizers) | `uv run python -c "import nltk; nltk.download('punkt_tab')"` |

> 🎮 **No GPU?** That is fine. Everything except the training runs of Lec_24 to Lec_26 works on a CPU. For those, use Google Colab with a free T4 GPU (Lec_05 shows how); Lec_26 (Unsloth) in particular expects Linux with an NVIDIA GPU.

---

## ☁️ Running the Notebooks on Google Colab

Any notebook can be opened directly from GitHub in Colab:

```
https://colab.research.google.com/github/arifpucit/Generative-and-Agentic-AI/blob/main/Notebooks/<notebook-file-name>.ipynb
```

Colab does not have the course environment, so install what a notebook needs in its first cell (the training notebooks Lec_25 and Lec_26 already contain their install cells), or install the whole course stack from the exported requirements (this takes several minutes):

```python
!git clone --depth 1 https://github.com/arifpucit/Generative-and-Agentic-AI.git
%cd Generative-and-Agentic-AI/Notebooks
!pip install -q -r requirements.txt
```

Store your API keys in Colab's **Secrets** panel (🔑 icon) instead of a `.env` file; Lec_05 walks you through it.

---

## ⏱️ Free Tiers, Rate Limits and Shared Servers

- **Groq free tier.** Each model has its own limits, for example about **8,000 tokens per minute and 200,000 tokens per day** for `openai/gpt-oss-20b` and `openai/gpt-oss-120b`. Agent notebooks resend the whole conversation on every step, so one full run of a long agent notebook can use a large part of a day's quota. The notebooks retry automatically after a per-minute `429`; after a per-day `429`, wait until the next day or switch to the other model.
- **Shared MCP servers on Render.** Lec_46 onwards use a Demo-server and two travel servers (flights, hotels) on Render's free plan. They **sleep when idle**: the first call can take up to a minute. The flight and hotel servers call third-party APIs whose free quotas are **shared by the whole class**: run those cells once, not in a loop.
- **Servers started by notebooks.** Lec_46, Lec_48 and Lec_50 start local servers (ports 8000 and 9001–9003). Always run their **Clean up** section before closing the notebook.

---

## 🔄 Daily Workflow

You run `uv sync` once. From then on:

```bash
cd Generative-and-Agentic-AI
uv run jupyter lab
```

When new notebooks are published or a library is added, refresh your copy:

```bash
git pull      # the latest notebooks and dependency files
uv sync       # bring your environment in line with uv.lock
```

> Your `keys/.env` and `.venv/` are git-ignored, so `git pull` never overwrites your API keys or your environment.

**Useful `uv` commands**

```bash
uv run jupyter lab                  # start Jupyter Lab
uv run python my_script.py          # run a script inside the environment
uv add <package>                    # add a library (updates pyproject.toml and uv.lock)
uv remove <package>                 # remove a library
uv tree                             # show the dependency tree
uv cache clean                      # clear the download cache
```

You can still activate the environment the traditional way, with `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows), but `uv run` is safer, because it keeps the environment in sync first.

---

## 🧯 Troubleshooting

| Problem | Fix |
|:--|:--|
| `uv: command not found` | Close and reopen your terminal so it picks up the new `PATH`. |
| `uv sync` fails midway | Run it again: it resumes from the cache. If it still fails, run `uv cache clean` and then `uv sync`. |
| A notebook cannot find a library | Launch Jupyter with `uv run jupyter lab` **from inside the repository folder**, use the **Python 3 (ipykernel)** kernel, and run `git pull` + `uv sync` if the library was added recently. |
| `os.getenv()` returns `None` / "API key not set" | The file must be `keys/.env` at the repository root (not `Notebooks/keys/.env`), the names must match exactly, with no spaces around `=`. Then **restart the kernel**. |
| `AuthenticationError` / `401` from a provider | The key is wrong, revoked or out of credits. Create a new one and check your balance. |
| `RateLimitError` / `429` | You hit a free-tier limit. Wait a minute (per-minute limit) or until tomorrow (per-day limit), or switch to another model or provider. |
| `insufficient_quota` from OpenAI | No credits: add a payment method and buy credits. |
| Gated model download fails (`403`) on Hugging Face | Accept the model's licence on its page while logged in, and use a token with **Write** scope. |
| `ollama: connection refused` | Start Ollama (the app, or `ollama serve`) and pull the model first, e.g. `ollama pull llama3.2:1b`. |
| `pymongo.errors.ServerSelectionTimeoutError` | MongoDB is not running: start it, or use your Atlas connection string. |
| Audio cells fail with an `ffmpeg` error | Install the real ffmpeg program (see [Optional Tools](#-optional-tools-for-specific-lectures)); the PyPI package `ffmpeg` is not the encoder. |
| A Render MCP server or agent service is slow or times out | Free Render services sleep when idle: the first call can take up to a minute. Run the cell again. |
| `address already in use` when a notebook starts a server | A server from an earlier run is still running: run that notebook's **Clean up** section, or restart the kernel. |
| `docker: command not found` / `sbx is not installed` (Lec_43) | Install and start Docker Desktop (or OrbStack/Colima), and install `sbx` (see [Optional Tools](#-optional-tools-for-specific-lectures)). |
| Out of disk space during `uv sync` | The full stack needs about 10 GB. Free some space and run `uv sync` again. |
| Want a clean start | Delete the `.venv/` folder and run `uv sync` again. |

---

## 📖 Learning Approach

> **Important:** the notebooks are provided to save you typing, but I **strongly recommend** that you:
>
> - ✅ Type the programs yourself for better understanding
> - ✅ Change the code and experiment with it
> - ✅ Do some "scuba diving" into the underlying concepts

*"The best way to learn programming is by programming!"* Don't just copy and paste the code: engage with it, modify it, break it and fix it.

---

## 🤝 Contributing

Found a problem or have a suggestion? Feel free to:

- open an issue,
- submit a pull request, or
- contact the instructor.

---

## 👨‍🏫 Meet Your Instructor

### Dr. Muhammad Arif Butt

**Assistant Professor, Department of Data Science**
**University of the Punjab, Lahore**

#### 🎓 Education

- **Pakistan Military Academy, Kakul**: Graduate
- **MPhil Computer Science**: University of the Punjab, Lahore
- **PhD Computer Science**: University of the Punjab, Lahore

#### 💼 Experience

- 🎖️ **Pakistan Army**: field, staff and instructional posts
- 👨‍🏫 **Assistant Professor**: Department of Data Science
- 🚀 **Founder**: [Excaliat](https://excaliat.com/en)
- 🦅 **Founder**: [FalconHunt](https://falconhunt.org/)
- 🔧 **Co-Founder**: [Tbox Solutionz](https://tboxsolutionz.com/)

#### 🔬 Research Interests

- Embedded and real-time operating systems
- Vulnerability analysis, binary exploitation and exploit development
- AI-driven cybersecurity and securing AI systems

#### 📞 Connect

- 📧 **Email**: <arif@pucit.edu.pk>
- 🌐 **Website**: <https://arifbutt.me>
- 📺 **YouTube**: [Learn with Arif](https://youtube.com/learnwitharif)
- 💻 **GitHub**: [@arifpucit](https://github.com/arifpucit)
- 💼 **LinkedIn**: [Dr. Arif Butt](https://www.linkedin.com/in/dr-arif-butt/)
- 🤗 **Hugging Face**: [arif-butt](https://huggingface.co/arif-butt)

---

## 📜 License

This repository is for educational purposes. Please respect academic integrity guidelines when you use this code for assignments or projects. The books and research articles in this repository belong to their respective authors and publishers.

---

⭐ **Star this repository if you find it helpful!** Happy learning, and keep building.
