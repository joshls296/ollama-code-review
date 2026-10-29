# Local AI Code Review & Automated Testing Dashboard

An end-to-end, privacy-focused code analysis platform that integrates a local Large Language Model (**CodeLlama** via **Ollama**) with a **FastAPI** backend and a **React + TypeScript** frontend. The application evaluates source code snippets across multiple programming languages for security vulnerabilities (e.g., SQL injections), memory leaks, performance bottlenecks, and bad practices—running 100% locally without sending code to third-party cloud APIs.

---

## Key Features

* **Privacy-First AI Analysis:** Executes `CodeLlama` locally through Ollama, guaranteeing total source code privacy and offline capability.
* **Asynchronous API Gateway:** Built with FastAPI and LangChain for rapid prompt orchestration, structured validation, and CORS security.
* **Modern Developer UI:** React + TypeScript dashboard scaffolded with Vite, featuring code formatting, clean typography, and responsive result panels.
* **Automated CI/CD Pipeline:** PowerShell orchestration script (`run_pipeline.ps1`) that sequentially executes backend unit tests (`Pytest`), boots API services, and runs headless browser end-to-end tests (`Playwright`).

---

## Tech Stack

| Component | Technology | Description |
| --- | --- | --- |
| **Backend API** | Python 3.11, FastAPI, Uvicorn | High-performance asynchronous API framework |
| **AI Orchestration** | LangChain (`langchain-ollama`), Ollama | Local LLM prompt engineering and model execution (`codellama`) |
| **Frontend UI** | React 18, TypeScript, Vite, Axios | Reactive dashboard interface and API communication |
| **Testing & Quality** | Pytest, Playwright | Backend integration testing and headless E2E browser automation |
| **Automation** | PowerShell (Windows Native) | One-command pipeline execution and process lifecycle management |

---

## Project Structure

```text
├── main.py               # FastAPI server & LangChain CodeLlama prompt pipeline
├── test_backend.py       # Pytest suite for backend endpoints
├── run_pipeline.ps1      # PowerShell CI/CD pipeline automation script
├── requirements.txt      # Python dependencies manifest
├── .gitignore            # Git version control exclusions
├── README.md             # Project documentation
└── frontend/             # React + TypeScript Vite client application
    ├── src/
    │   ├── App.tsx       # Main dashboard interface component
    │   ├── main.tsx      # Application entry point
    │   └── index.css     # Global styles
    ├── tests/
    │   └── e2e.spec.ts   # Playwright end-to-end integration test
    ├── package.json      # Frontend npm dependencies
    └── vite.config.ts    # Vite build configuration

```

---

## Prerequisites

Before running this project, ensure you have the following installed on your system:

1. **Python 3.11+** – [Download Python](https://www.python.org/downloads/)
2. **Node.js (LTS version)** – [Download Node.js](https://nodejs.org/)
3. **Ollama** – [Download Ollama](https://ollama.com/)

Once Ollama is installed, pull the `codellama` model using PowerShell:

```powershell
ollama pull codellama

```

---

## Setup & Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/YOUR_USERNAME/code-review-dashboard.git
cd code-review-dashboard

```

### 2. Backend Setup

Create and activate a Python virtual environment, then install required backend packages:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

```

### 3. Frontend Setup

Navigate to the `frontend` directory, install Node packages, and download Playwright browser binaries:

```powershell
Set-Location frontend
npm install
npx playwright install
Set-Location ..

```

---

## Running the Application

### Option 1: Automated Pipeline Execution (Recommended)

You can run the entire test suite and verify the application end-to-end with a single command. Open PowerShell in your root project directory with `venv` activated and execute:

```powershell
.\venv\Scripts\Activate.ps1
.\run_pipeline.ps1

```

**What the pipeline does automatically:**

1. Runs `pytest test_backend.py` to verify API logic and model response.
2. Boots up the FastAPI backend on `http://localhost:8000`.
3. Runs Playwright headless browser tests against the React frontend (`http://localhost:5173`).
4. Gracefully terminates backend processes upon completion.

### Option 2: Interactive Development Mode

To run the full stack interactively in your browser:

1. **Start the FastAPI Backend (Terminal 1):**
```powershell
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8000

```


2. **Start the React Frontend (Terminal 2):**
```powershell
Set-Location frontend
npm run dev

```


3. Open your browser and navigate to **`http://localhost:5173`**.

---

## Testing Strategy

* **Unit & API Testing (`test_backend.py`):** Uses Pytest and FastAPI `TestClient` to validate JSON request schemas and LLM inference response structures.
* **End-to-End Browser Testing (`frontend/tests/e2e.spec.ts`):** Uses Playwright to simulate user interactions—filling code snippets into the UI, triggering analysis, and asserting DOM visibility of AI analysis cards.
