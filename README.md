## Python env

### Node
- `node_modules/`
- `package.json`

### Python
- `venv/`
- `requirements.txt`

### Create Venv
```bash
python3 -m venv venv
```

### Activate Venv

**Windows (PowerShell or CMD):**
```powershell
.\venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

**Note for Windows PowerShell Users:**
If you get an error stating that running scripts is disabled (`UnauthorizedAccess` / Execution Policy error), run this command once to allow scripts for your user account:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try the activate command again.

### Common Commands

| Task | Command |
|---|---|
| Create env | `python -m venv venv` |
| Activate env | `.\venv\Scripts\activate` |
| Install package | `pip install fastapi` |
| Save deps | `pip freeze > requirements.txt` |
| Install deps | `pip install -r requirements.txt` |
| Run FastAPI | `uvicorn app.main:app --reload` |

# Database Architecture

## Big Picture Architecture
```mermaid
flowchart TD
    A[Angular UI] -->|HTTP Request| B(FastAPI Backend)
    B -->|Database Query| C[(PostgreSQL Database)]
```

## What Happens Internally?
```mermaid
flowchart TD
    A[FastAPI starts] --> B[SQLAlchemy connects]
    B --> C[Tables created]
    C --> D((Server listens for requests))
```

## Complete Request Flow
```mermaid
flowchart TD
    A([Browser Request]) --> B[FastAPI Route]
    B --> C[Depends get_db]
    C --> D[Session Created]
    D --> E[ORM Query]
    E --> F[psycopg2 sends SQL]
    F --> G[(PostgreSQL responds)]
    G --> H([JSON returned])
```
