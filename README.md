# 🤖 LLM-Powered Calculator

A smart calculator that uses AI (TinyLlama via Hugging Face) to solve math problems naturally.

## Features

- Natural language math problems
- Step-by-step explanations
- Real-time streaming responses
- Multiple calculation types

## API Usage

```bash
curl -X POST https://sagar0123-sagar-nebula-cpu-brain.hf.space/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tinyllama",
    "messages": [{"role": "user", "content": "What is 15 + 27?"}],
    "max_tokens": 100,
    "stream": true
  }'
```

## Local Development

```bash
# Install dependencies
pip install requests

# Run the demo
python calculator.py
```

## Try These Examples

- "What is 123 × 456?"
- "Calculate the square root of 2025"
- "What is 15% of 200?"
- "Solve: 2^10"

## Tech Stack

- Python
- Hugging Face Spaces API (TinyLlama)
- FastAPI streaming
# Updated
# Update
# LLM Calculator
- Updated
## Usage
## License
- MIT License
## API
- GET /calculate
