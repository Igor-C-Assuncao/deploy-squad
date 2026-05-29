# Antigravity Council 🚀

[![Antigravity](https://img.shields.io/badge/Framework-Antigravity%202.0-blueviolet)](https://cloud.google.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org)
[![Linter](https://img.shields.io/badge/Linter-Ruff-green)](https://github.com/astral-sh/ruff)

An automated production deployment guardrail pipeline powered by **Google Antigravity 2.0 Engine** and Gemini 3.5. This repository implements a parallel, asynchronous Multi-Agent System (*Fan-Out/Fan-In* architecture) that acts as an expert advisory council, auditing software artifacts across Software Engineering, MLOps, and International Compliance standards before hitting production.

---

## 🏗️ Architecture Overview

The pipeline leverages a parallel routing pattern. When a deployment snapshot (code diffs, database configurations, or model metadata) is submitted, the **Central Router** orchestrates three specialized subagents concurrently:

1. **Code Reviewer:** Audits code quality, cyclomatic complexity, SOLID principles, and structural Design Patterns.
2. **ML Guardian:** Audits data lineage, prevents training-serving skew (Snowflake integrations), evaluates tracking metrics (MLflow), and optimizes LLM prompt graph topologies.
3. **ISO Compliance Auditor:** Scans codebases against **ISO/IEC 25010** (Software Quality) and **ISO/IEC 42001** (Artificial Intelligence Governance).

Once the analysis loop finishes, an **Orchestrator** processes all structural reports, reconciles conflicting suggestions, and compiles a single **Final Executive Report** containing deployment status and a strategic feature backlog.

---

## 📂 Repository Structure

```text
antigravity-council/
├── antigravity.yaml         # Global Antigravity CLI routing orchestration config
├── orchestrator.py          # Asynchronous multi-agent execution engine script
└── agents/
    ├── central_router.md     # System prompt for the Central Router agent
    ├── code_reviewer/
    │   ├── prompt.md        # Skill profile for the Software Engineer Agent
    │   ├── schema.py        # Pydantic data contract for code review
    │   └── tools.py         # Local Python execution tools (Ruff, Git)
    ├── ml_guardian/
    │   ├── prompt.md        # Skill profile for the MLOps Specialist Agent
    │   ├── schema.py        # Pydantic data contract for model validation
    │   └── tools.py         # Connection mock tools (MLflow, Snowflake)
    └── iso_compliance/
        ├── prompt.md        # Skill profile for the ISO Auditor Agent
        ├── schema.py        # Pydantic data contract for compliance reports
        └── tools.py         # Regulatory and security sanity check tools
```



## 🛠️ Prerequisites & Installation
1. Install System Dependencies
Ensure you have Python 3.10+ installed along with git and ruff.

Bash
pip install antigravity-cli google-antigravity pydantic ruff
2. Authenticate the Antigravity CLI
Authenticate your terminal environment with your Google Antigravity cloud instance:

```Bash 
agy login
```

## 🚀 How to Run
Option 1: Automated Script Execution (SDK)
To trigger the full parallel council audit engine against a deployment snapshot, run the main python orchestration file:

```Bash
python orchestrator.py
```

### Option 2: Interactive Chat via Antigravity CLI (agy)

You can engage directly with individual specialized agents or the router via the terminal shell interface.

To chat with the default route configured in antigravity.yaml:

```Bash
agy chat
```

To isolate a specific agent skill along with its custom local Python tools:

```Bash
agy chat --skill agents/code_reviewer/prompt.md --tools agents/code_reviewer/tools.py
```

Direct Agent Invocation within Chat:
When utilizing the router, you can explicitly force a delegate path using slash commands:

```Plaintext
> /code_reviewer analyze this method for high nesting levels...
```

## 📊 Evaluation Outputs (Data Contracts)
Every agent generates typed JSON records leveraging native Pydantic validation. The final node produces an executive verdict matching this model contract:

```JSON
{
  "status": "APPROVED_WITH_WARNINGS",
  "summary": "The runtime logic passes security and baseline MLOps thresholds, but fails structural modularity patterns.",
  "blocking_issues": [],
  "innovation_backlog": [
    {
      "title": "Introduce Temporal Convolutional Autoencoders for Sound Anomaly Validation",
      "rationale": "Replaces standard threshold checks with deep temporal sequences, reducing false positives by 15%."
    }
  ]
}
```


## 📝 Compliance Targets
- ISO/IEC 25010: System and software quality models (Maintainability, Reliability, Security).

- ISO/IEC 42001: Information technology — Artificial intelligence — Management system.
