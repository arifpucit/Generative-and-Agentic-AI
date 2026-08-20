# Generative and Agentic AI with Arif Butt

[![Course](https://img.shields.io/badge/Course-GenAI%20AgenticAI-blue.svg)](http://arifbutt.me/cources)
[![Language](https://img.shields.io/badge/Language-Python-orange.svg)](https://www.python.org/)
[![Python](https://img.shields.io/badge/Python-3.12-yellow.svg)](https://www.python.org/downloads/)
[![Package Manager](https://img.shields.io/badge/env-uv-purple.svg)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](#-license)

Welcome to the **Generative and Agentic AI Course** repository! This collection contains 45 Jupyter notebooks with the Proof of Concepts (PoCs) discussed during the course lectures.

---

## 📑 Table of Contents

1. [About This Repository](#-about-this-repository)
2. [Repository Structure](#-repository-structure)
3. [Prerequisites](#-prerequisites)
4. [Quick Start (TL;DR)](#-quick-start-tldr)
5. [Detailed Setup](#-detailed-setup)
   - [Step 1: Install `uv`](#step-1-install-uv)
   - [Step 2: Clone the Repository](#step-2-clone-the-repository)
   - [Step 3: Build the Virtual Environment](#step-3-build-the-virtual-environment)
   - [Step 4: Create Your API Keys File](#step-4-create-your-api-keys-file)
   - [Step 5: Launch Jupyter Lab](#step-5-launch-jupyter-lab)
   - [Step 6: Verify with Lec_00](#step-6-verify-everything-with-lec_00)
6. [API Keys: Accounts and Setup](#-api-keys-accounts-and-setup)
7. [Optional Tools for Specific Lectures](#-optional-tools-for-specific-lectures)
8. [Daily Workflow](#-daily-workflow)
9. [Troubleshooting](#-troubleshooting)
10. [Learning Approach](#-learning-approach)
11. [Meet Your Instructor](#-meet-your-instructor)
12. [License](#-license)

---

## 📚 About This Repository

This repository serves as a comprehensive resource for students enrolled in the Generative and Agentic AI course. Each notebook demonstrates fundamental concepts through practical Python implementations, making complex theoretical concepts tangible and understandable.

**Course topics covered across the notebooks:**

| Lectures | Topic |
|:--|:--|
| Lec_00 | Setting up your lab environment |
| Lec_01 – Lec_04 | Accessing closed-source flagship models (OpenAI, Anthropic, Google) + Prompt Engineering |
| Lec_05 – Lec_12 | Open-source models: Colab, Hugging Face Hub, Groq, Ollama, Gradio, HF Spaces |
| Lec_13 – Lec_15 | Multi-modality and AI benchmarks |
| Lec_16 – Lec_21 | Tokenization, vectorization, deep neural nets, Transformer architecture |
| Lec_22 – Lec_26 | Fine-tuning LLMs (PEFT, TRL, Unsloth) |
| Lec_27 – Lec_29 | Modern database landscape, MongoDB, ChromaDB |
| Lec_30 – Lec_38 | LangChain components, vector DBs, retrievers, RAG |
| Lec_39 – Lec_44 | Agentic AI, tool calling, MCP protocol, OpenAI Agents SDK |

### 🔗 Course Resources

- **Lecture Slides**: <http://arifbutt.me/cources>
- **Course Level**: Undergraduate + Graduate
- **Programming Language**: Python 3.12

---

## 📁 Repository Structure

```
📦 Generative-and-Agentic-AI
├── 📂 Notebooks/          # All 45 lecture notebooks (Lec_00 … Lec_44)
├── 📂 data/               # Datasets, documents, and audio files used by notebooks
│   └── 📂 audios/         # Audio samples for the multi-modality lectures
├── 📂 images/             # Images embedded in the notebooks
├── 📂 Books/              # Reference books for the course
├── 📂 Research Articles/  # Supplementary reading
├── 📂 keys/               # ⚠️ YOU create this — holds your .env with API keys (git-ignored)
├── 📄 pyproject.toml      # Project manifest: every library the course needs
├── 📄 uv.lock             # Exact pinned versions of all dependencies
├── 📄 .python-version     # Pins the interpreter to Python 3.12
└── 📄 README.md           # This file
```

> **Note:** The `keys/` folder is **not** in the repository — it is listed in `.gitignore` so that nobody ever commits their secrets. You will create it yourself in [Step 4](#step-4-create-your-api-keys-file).

---

## ✅ Prerequisites

**Knowledge:**
- Basic understanding of programming in Python
- Hands-on understanding of Machine Learning
- Understanding of Deep Learning concepts will be a plus

**Machine:**
- macOS, Linux, or Windows
- **~10 GB of free disk space** (PyTorch and the ML stack are large)
- A reasonable internet connection for the first install
- `git` installed — check with `git --version`, otherwise get it from <https://git-scm.com/downloads>

> **You do NOT need Python pre-installed.** `uv` downloads and manages the correct Python 3.12 interpreter for you.

---

## 🚀 Quick Start (TL;DR)

```bash
# 1. Install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone the repo
git clone --depth 1 https://github.com/arifpucit/Generative-and-Agentic-AI.git
cd Generative-and-Agentic-AI

# 3. Build the environment (downloads Python 3.12 + all libraries)
uv sync

# 4. Create your keys file
mkdir -p keys && touch keys/.env      # then paste your API keys into it (see Step 4)

# 5. Launch Jupyter Lab
uv run jupyter lab

# 6. Open Notebooks/Lec_00_(Setting_up_Lab_Environment).ipynb and run all cells
```

Each step is explained in detail below.

---

## 🔧 Detailed Setup

### Step 1: Install `uv`

**`uv`** is a next-generation Python package manager written in Rust that replaces `pip`, `venv`, `poetry`, `pyenv`, and `virtualenv` with a single, blazingly fast tool. It also downloads and manages Python interpreters for you, so **you do not need Python pre-installed**.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (run in PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close and reopen your terminal**, then verify:

```bash
uv --version
```

If the command is not found, your terminal has not picked up the updated `PATH` yet — close it and open a fresh one. To upgrade `uv` later, run `uv self update`.

---

### Step 2: Clone the Repository

The repository also contains books and reference material, so the full history is fairly large. Cloning only the latest snapshot is much faster:

```bash
git clone --depth 1 https://github.com/arifpucit/Generative-and-Agentic-AI.git
cd Generative-and-Agentic-AI
```

If you want the complete history instead, drop the `--depth 1` flag.

Confirm you are in the right place:

```bash
ls -a
# .python-version   pyproject.toml   uv.lock   Notebooks/   data/   images/   README.md
```

These three files drive the next step:

| File | Purpose |
|:--|:--|
| `pyproject.toml` | The project manifest — the list of every library this course needs |
| `uv.lock` | The lock file — the *exact* version of all direct and transitive dependencies |
| `.python-version` | Pins the interpreter to Python 3.12 |

---

### Step 3: Build the Virtual Environment

A **single command** creates the virtual environment and installs everything:

```bash
uv sync
```

Because the repository already ships `pyproject.toml` and `uv.lock`, `uv sync`:

1. downloads Python 3.12 if it is not already on your machine,
2. creates a virtual environment in a hidden `.venv/` folder inside the project,
3. installs every dependency at the exact locked version.

> ⏳ **Be patient the first time.** This downloads several GB of ML libraries (PyTorch, Transformers, CUDA runtime on Linux, etc.) and may take **5–20 minutes** depending on your connection. Later runs are nearly instant because `uv` caches everything.

**Verify the environment was built:**

```bash
uv run python -c "import torch, transformers, langchain; print('OK', torch.__version__)"
```

> **Why `uv sync` and not `pip install -r requirements.txt`?** `uv sync` installs from the lock file, so every student gets identical versions — which means "it works on my machine" actually transfers to yours. It is also dramatically faster.

---

### Step 4: Create Your API Keys File

Almost every notebook from Lec_01 onwards loads secrets with:

```python
load_dotenv('../keys/.env', override=True)
```

Because the notebooks live in `Notebooks/`, that path resolves to **`keys/.env` at the root of the repository**. The `keys/` folder is git-ignored, so it does not ship with the clone — **you must create it**.

```bash
# From the root of the repository
mkdir -p keys
touch keys/.env
```

Now open `keys/.env` in any text editor and paste the following template, replacing each placeholder with your own key:

```ini
# ==========================================================
#  Generative and Agentic AI — API Keys
#  File location: <repo-root>/keys/.env
#  NEVER commit this file. It is already excluded via .gitignore
# ==========================================================

# --- Closed-source flagship models -----------------------
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=AIzaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# --- Open-source models / inference ----------------------
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# --- Tool calling / agent demos --------------------------
WEATHER_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SEND_GRID=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Important formatting rules for `.env` files:**
- No spaces around the `=` sign → `OPENAI_API_KEY=sk-...` ✅ not `OPENAI_API_KEY = sk-...` ❌
- No quotes around the value (unless the value itself contains spaces)
- One key per line, no trailing commas
- The variable names must match **exactly** as written above (they are case-sensitive)

**Verify your keys are being read:**

```bash
uv run python -c "
from dotenv import load_dotenv; import os
load_dotenv('keys/.env', override=True)
for k in ['OPENAI_API_KEY','ANTHROPIC_API_KEY','GOOGLE_API_KEY','GROQ_API_KEY','HF_TOKEN','WEATHER_API_KEY','SEND_GRID']:
    v = os.getenv(k)
    print(f'{k:<20} {\"OK  \" + v[:8] + \"...\" if v else \"MISSING\"}')
"
```

> 🔐 **Keep your API keys out of git.** Never paste a key directly into a notebook cell, and never commit `keys/.env`. If you ever expose a key by accident, revoke it immediately from the provider's dashboard and generate a new one.

---

### Step 5: Launch Jupyter Lab

Start Jupyter Lab **through `uv`** so it runs inside the project environment:

```bash
uv run jupyter lab
```

Your browser will open Jupyter Lab automatically. Navigate into the **`Notebooks/`** folder.

**Selecting the kernel:** Because Jupyter Lab is installed *inside* the project environment, the default **Python 3 (ipykernel)** kernel already points at your project environment and can see all the course libraries. You do **not** need to register a kernel manually. If you are ever asked to pick a kernel, choose **Python 3 (ipykernel)**.

---

### Step 6: Verify Everything with Lec_00

Open **`Notebooks/Lec_00_(Setting_up_Lab_Environment).ipynb`** — this notebook exists specifically so you can confirm your environment is correct before Lecture 1.

Run the two code cells in it:

**Section 3 — Hardware check.** Reports your CPU cores, RAM, and whether an NVIDIA GPU is available. There is no "correct" output here; it simply tells you what your machine can handle. (No GPU is fine — the fine-tuning lectures can be run on Google Colab.)

**Section 4 — Environment health check.** Imports 51 key libraries across 9 categories and reports each one. A healthy environment ends with:

```
========================================================================
📊 OVERALL SUMMARY
========================================================================
✅ Installed: 51/51 (100.0%)

📂 Category Status:
  🟢 🧮 Core Python & Data: 5/5
  🟢 🤖 ML & Deep Learning: 8/8
  🟢 🔗 LangChain Ecosystem: 6/6
  🟢 🕸️ LangGraph: 3/3
  🟢 🗃️ Vector Databases: 5/5
  🟢 🗄️ Databases: 8/8
  🟢 🌐 LLM Providers & APIs: 5/5
  🟢 🌐 Web / Parsing / Media: 6/6
  🟢 🛠️ Dev & UI Tools: 5/5

🎉 ENVIRONMENT READY — ALL REQUIRED LIBRARIES FOUND!
```

If you see **51/51**, your lab environment is complete and you are ready for Lecture 1. If any library reports `❌ NOT INSTALLED`, the notebook prints the exact `uv add ...` command to fix it — but first try re-running `uv sync` from the repository root.

---

## 🔑 API Keys: Accounts and Setup

You do **not** need all seven keys on day one. Get them as the lectures require them. The table shows which notebooks need which key:

| # | Variable | Provider | Where to get it | Cost | Used in |
|:--|:--|:--|:--|:--|:--|
| 1 | `GROQ_API_KEY` | Groq | [console.groq.com/keys](https://console.groq.com/keys) | **Free tier** | Lec_07, 09, 10, 13, 14, 30–33, 37–40, 44 |
| 2 | `OPENAI_API_KEY` | OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | Paid (pre-paid credits) | Lec_01, 04, 11, 13, 14, 17, 29, 30, 35, 36, 39, 40, 44 |
| 3 | `HF_TOKEN` | Hugging Face | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | **Free** | Lec_06, 07, 10, 13, 14, 24, 25, 26, 30 |
| 4 | `GOOGLE_API_KEY` | Google AI Studio | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | **Free tier** | Lec_03, 13, 14, 30 |
| 5 | `ANTHROPIC_API_KEY` | Anthropic | [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys) | Paid (pre-paid credits) | Lec_02, 09, 13, 14, 30 |
| 6 | `WEATHER_API_KEY` | WeatherAPI | [weatherapi.com](https://www.weatherapi.com/signup.aspx) | **Free tier** | Lec_40, 43 |
| 7 | `SEND_GRID` | SendGrid (Twilio) | [sendgrid.com](https://signup.sendgrid.com/) | **Free tier** | Lec_44 |

> 💡 **Start with the free ones.** `GROQ_API_KEY`, `HF_TOKEN`, and `GOOGLE_API_KEY` are free and together cover the majority of the course. Add the paid OpenAI and Anthropic keys when you reach the lectures that need them.

### How to obtain each key

<details>
<summary><b>1. Groq — free, fastest inference (most used key in this course)</b></summary>

1. Go to <https://console.groq.com> and sign up with Google/GitHub or email.
2. Verify your email address.
3. In the left sidebar click **API Keys** → **Create API Key**.
4. Give it a name (e.g. `genai-course`) and click **Submit**.
5. **Copy the key immediately** — it is shown only once.
6. Paste it into `keys/.env` as `GROQ_API_KEY=gsk_...`

Groq's free tier has generous rate limits and requires no credit card.
</details>

<details>
<summary><b>2. OpenAI — paid, requires billing setup</b></summary>

1. Go to <https://platform.openai.com> and create an account.
2. Verify your phone number (required for API access).
3. Go to **Settings → Billing** and add a payment method, then buy credits (a **$5 minimum** top-up is plenty for this course).
4. Go to **API keys** → **Create new secret key**.
5. Name it, choose the default project, click **Create secret key**.
6. **Copy it immediately** — it will never be shown again.
7. Paste into `keys/.env` as `OPENAI_API_KEY=sk-proj-...`

> ⚠️ Note that a ChatGPT Plus subscription does **not** include API credits — they are billed separately.
</details>

<details>
<summary><b>3. Hugging Face — free, needed for models and Spaces</b></summary>

1. Create an account at <https://huggingface.co/join>.
2. Go to **Settings → Access Tokens** (<https://huggingface.co/settings/tokens>).
3. Click **Create new token**.
4. Choose token type **Write** — the write scope is needed for Lec_10 (deploying to HF Spaces) and the fine-tuning lectures that push models to the Hub.
5. Name it (e.g. `genai-course`), click **Create token**, and copy it.
6. Paste into `keys/.env` as `HF_TOKEN=hf_...`

> Some models on the Hub (e.g. Llama, Gemma) are **gated** — you must visit the model page while logged in and accept its licence before your token can download it.
</details>

<details>
<summary><b>4. Google AI Studio — free tier for Gemini</b></summary>

1. Go to <https://aistudio.google.com/apikey> and sign in with a Google account.
2. Click **Create API key**.
3. Choose an existing Google Cloud project or let it create a new one.
4. Copy the generated key.
5. Paste into `keys/.env` as `GOOGLE_API_KEY=AIza...`

The free tier is sufficient for the course notebooks. No billing setup is required.
</details>

<details>
<summary><b>5. Anthropic — paid, requires credit purchase</b></summary>

1. Go to <https://console.anthropic.com> and create an account.
2. Verify your email and phone number.
3. Go to **Settings → Billing** and purchase credits (a **$5 minimum** is enough for the course).
4. Go to **Settings → API Keys** → **Create Key**.
5. Name it, create it, and **copy it immediately**.
6. Paste into `keys/.env` as `ANTHROPIC_API_KEY=sk-ant-...`

> ⚠️ A Claude.ai Pro subscription does **not** include API credits — they are billed separately.
</details>

<details>
<summary><b>6. WeatherAPI — free tier for the tool-calling demos</b></summary>

1. Sign up at <https://www.weatherapi.com/signup.aspx> (free, no credit card).
2. Verify your email address.
3. Your API key is displayed directly on the dashboard after login.
4. Paste into `keys/.env` as `WEATHER_API_KEY=...`

This is used as the example external tool that the agent calls in Lec_40 and Lec_43.
</details>

<details>
<summary><b>7. SendGrid — free tier for the agent email demo</b></summary>

1. Sign up at <https://signup.sendgrid.com/> (free tier: 100 emails/day).
2. Complete email verification and the account questionnaire.
3. Go to **Settings → Sender Authentication** and verify a **Single Sender** email address — SendGrid will not send mail until you do this.
4. Go to **Settings → API Keys** → **Create API Key**, choose **Full Access**, and create it.
5. **Copy it immediately.**
6. Paste into `keys/.env` as `SEND_GRID=SG....`

> Note the variable is named `SEND_GRID` (not `SENDGRID_API_KEY`) to match the notebook code in Lec_44.
</details>

---

## 🛠️ Optional Tools for Specific Lectures

Most notebooks need nothing beyond `uv sync` and your API keys. A few lectures use external software you install separately — only install these when you reach the relevant lecture.

| Tool | Needed for | Install |
|:--|:--|:--|
| **Ollama** | Lec_08 (running local LLMs), Lec_22–26 (testing fine-tuned models) | Download from <https://ollama.com/download>, then `ollama pull llama3.2:1b` |
| **MongoDB** | Lec_28 (hands-on MongoDB) | [MongoDB Community Server](https://www.mongodb.com/try/download/community) running locally on `localhost:27017`, or a free [Atlas](https://www.mongodb.com/atlas) cluster |
| **ffmpeg** | Lec_13, Lec_14 (audio processing with `pydub`) | macOS: `brew install ffmpeg` · Ubuntu/Debian: `sudo apt install ffmpeg` · Windows: [download](https://ffmpeg.org/download.html) and add to `PATH` |
| **Playwright browsers** | Notebooks that scrape rendered web pages | `uv run playwright install` |
| **NLTK data** | Text-processing notebooks | `uv run python -c "import nltk; nltk.download('punkt_tab')"` |

> 🎮 **No GPU?** That is completely fine. Everything except the fine-tuning lectures (Lec_22–26) runs comfortably on CPU. For those, use **Google Colab** with a free T4 GPU — Lec_05 walks you through Colab, and Lec_26 (Unsloth) in particular is designed for a Linux + NVIDIA GPU environment.

---

## 🔄 Daily Workflow

You only ever run `uv sync` once. From the next session onwards:

```bash
cd Generative-and-Agentic-AI
uv run jupyter lab
```

When new notebooks are pushed or a library is added during the course, refresh your copy:

```bash
git pull      # fetch the latest notebooks and updated dependency files
uv sync       # bring your environment back in line with the lock file
```

> Your `keys/.env` and `.venv/` are git-ignored, so `git pull` will never overwrite your API keys or your environment.

**Useful `uv` commands:**

```bash
uv run jupyter lab                  # start Jupyter Lab
uv run python my_script.py          # run a script inside the environment
uv add <package>                    # add a new library (updates pyproject.toml + uv.lock)
uv remove <package>                 # remove a library
uv tree                             # show the full dependency tree
uv cache clean                      # clear the download cache
```

If you prefer the traditional workflow you can still activate the environment manually with `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows), but `uv run` is safer because it guarantees the environment is in sync first.

---

## 🧯 Troubleshooting

| Problem | Fix |
|:--|:--|
| `uv: command not found` | Close and reopen your terminal so it picks up the updated `PATH`. |
| `git: command not found` | Install Git from <https://git-scm.com/downloads> |
| `uv sync` fails midway | Re-run it — it resumes from cache. If it still fails, run `uv cache clean` then `uv sync`. |
| `jupyter: 'lab' is not a Jupyter command` | Your environment is out of date. Run `git pull` then `uv sync` from the repo root. |
| `error: Failed to build psycopg2` / `pg_config executable not found` | Your clone is out of date. Run `git pull` then `uv sync`. The course uses `psycopg2-binary`, which needs no PostgreSQL installation. |
| Notebook can't find a library | Make sure you launched with `uv run jupyter lab` **from inside the repo folder**, and that the kernel is **Python 3 (ipykernel)**. |
| Wrong kernel selected | In Jupyter Lab: **Kernel → Change Kernel… → Python 3 (ipykernel)** |
| `API Key not set` / `None` returned by `os.getenv()` | Check that the file is at `keys/.env` (not `Notebooks/keys/.env`), that variable names match exactly, and that there are no spaces around `=`. Then **restart the kernel** — `.env` is read at import time. |
| `AuthenticationError` / `401` from a provider | The key is wrong, revoked, or has no credits. Regenerate it in the provider dashboard and check your billing balance. |
| `RateLimitError` / `429` | You have hit the provider's free-tier limit. Wait a minute, or switch that notebook to the Groq or Gemini free tier. |
| `insufficient_quota` from OpenAI | You have no credits. Add a payment method and purchase credits — a ChatGPT Plus subscription does not cover API usage. |
| Gated model download fails (403) on Hugging Face | Visit the model's page while logged in and accept its licence, and make sure your `HF_TOKEN` has **Write** scope. |
| `ollama: connection refused` | Start the server with `ollama serve` in a separate terminal, and confirm you pulled the model with `ollama pull llama3.2:1b`. |
| `pymongo.errors.ServerSelectionTimeoutError` | MongoDB is not running. Start it locally, or point `MongoClient()` at your Atlas connection string. |
| Audio cells fail with a `ffmpeg` error | Install the real ffmpeg binary (see the table above) — the PyPI `ffmpeg` package is not the encoder itself. |
| Out of disk space during `uv sync` | The full stack needs roughly 10 GB. Free some space, then re-run `uv sync`. |
| Want a clean restart | Delete the `.venv/` folder and run `uv sync` again. |

---

## 📖 Learning Approach

> **Important Note**: While these source codes are provided to save your typing efforts, I **strongly recommend** that you:
>
> - ✅ Type the programs yourself for better understanding
> - ✅ Make modifications and experiment with the code
> - ✅ Do "Scuba Diving" into the underlying concepts

### 🎯 Learning Philosophy

*"The best way to learn programming is by programming!"*

Don't just copy-paste the code. Engage with it, modify it, break it, and fix it. This hands-on approach will deepen your understanding of the concepts involved.

---

## 🤝 Contributing

If you find any issues or have suggestions for improvements, feel free to:

- Open an issue
- Submit a pull request
- Contact the instructor

---

## 👨‍🏫 Meet Your Instructor

### Dr. Muhammad Arif Butt

**Assistant Professor, Department of Data Science**
**University of Punjab, Lahore**

#### 🎓 Educational Background

- **Pakistan Military Academy, Kakul** — Graduate
- **MPhil Computer Science** — University of Punjab, Lahore
- **PhD Computer Science** — University of Punjab, Lahore

#### 💼 Professional Experience

- 🎖️ **Pakistan Army** — Served in field/staff/instructional posts
- 👨‍🏫 **Assistant Professor** — Department of Data Science
- 🚀 **Founder** — [Excaliat](https://excaliat.com/en)
- 🦅 **Founder** — [FalconHunt](https://falconhunt.org/)
- 🔧 **Co-Founder** — [Tbox Solutionz](https://tboxsolutionz.com/)

#### 🔬 Research Interests

- **Embedded and Real-Time Operating Systems**
- **Vulnerability Analysis, Binary Exploitation & Exploit Development**
- **AI-Driven Cybersecurity and Securing AI Systems**

#### 📞 Connect with Dr. Butt

- 📧 **Email**: <arif@pucit.edu.pk>
- 🌐 **Website**: <https://arifbutt.me>
- 📺 **YouTube**: [Learn with Arif](https://youtube.com/learnwitharif)
- 💻 **GitHub**: [@arifpucit](https://github.com/arifpucit)
- 💼 **LinkedIn**: [Dr. Arif Butt](https://www.linkedin.com/in/dr-arif-butt/)

---

## 📜 License

This repository is for educational purposes. Please respect academic integrity guidelines when using this code for assignments or projects.

---

## 🎉 Final Words

Happy Coding! Remember, every expert was once a beginner. Keep practicing, keep learning, and most importantly, keep coding!

---

⭐ **Star this repository if you find it helpful!**
