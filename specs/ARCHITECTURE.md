# Architecture Document: LLM Calculator

## 1. System Overview

LLM Calculator is a Python application that uses an AI model (TinyLlama) to understand and solve natural language math problems, providing step-by-step explanations.

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      API Interface                          │
│                   (FastAPI with streaming)                 │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  LLM Processing                             │
│              (TinyLlama via Hugging Face)                  │
└─────────────────────────────────────────────────────────────┘
```

## 3. File Structure

```
llm-calculator/
├── calculator.py      # Main application
├── specs/             # Documentation
└── README.md
```

---

*Document Version: 1.0*  
*Created: 2026-03-17*
