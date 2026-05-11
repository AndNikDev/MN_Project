# Numerical Differentiation & Richardson Extrapolation

Interactive Streamlit application that explains, visualises and applies:

1. **Three-point formula** for numerical differentiation (forward, centered, backward).
2. **Richardson extrapolation** for accuracy improvement of order-2 schemes.

Built as part of the *MA-0322 Métodos Numéricos* course at Universidad de Costa Rica.

---

## Project structure

```
MN_Project/
├── app.py                    # Streamlit entry point
├── requirements.txt          # Runtime dependencies
├── pyproject.toml            # Project metadata & tooling
├── .streamlit/config.toml    # Streamlit theme & server config
│
├── core/                     # Pure logic layer (no Streamlit imports)
│   ├── parser.py             # SymPy expression parsing & evaluation
│   ├── differentiation.py    # Three-point formula contracts
│   ├── richardson.py         # Richardson extrapolation contracts
│   ├── errors.py             # Error metrics (absolute / relative / order)
│   └── visualization.py      # Plotly figure builders
│
├── ui/                       # Presentation layer (Streamlit components)
│   ├── sidebar.py            # Input widgets & configuration panel
│   ├── tables.py             # Pandas DataFrame builders & styling
│   └── latex_renderer.py     # LaTeX formula rendering helpers
│
├── tests/                    # Unit tests (pytest)
└── assets/                   # Images, static files, exported PDFs
```

The architecture follows a **layered / clean architecture** pattern:
`UI → Core (logic) → No external IO`. The `core` package is fully decoupled
from Streamlit so it can be reused from notebooks, scripts or unit tests.

---

## Setup

### 1. Recommended Python version

**Python 3.12.x** (most stable for `numpy + pandas + streamlit`).
Supported range: `>=3.10, <3.14`.

> Python 3.14 is too new — many scientific wheels are not yet published.

### 2. Create a virtual environment

```powershell
# Windows PowerShell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```bash
# Linux / macOS
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the app

```powershell
streamlit run app.py
```

Open the URL printed in the terminal (usually `http://localhost:8501`).

---

## Status

The project skeleton is ready. The numerical methods themselves are intentionally
left unimplemented (placeholders raise `NotImplementedError`) — they will be added
in subsequent iterations following the same modular contracts.
