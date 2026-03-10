#!/usr/bin/env python3
"""
🤖 LLM-Powered Calculator
Uses TinyLlama on Hugging Face to solve math problems naturally
"""

import requests
import json
import sys

HF_SPACE_URL = "https://sagar0123-sagar-nebula-cpu-brain.hf.space"


def calculate(prompt: str, stream: bool = True) -> str:
    """Send math problem to LLM and get answer"""
    
    payload = {
        "model": "tinyllama",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "stream": stream
    }
    
    response = requests.post(
        f"{HF_SPACE_URL}/v1/chat/completions",
        json=payload,
        stream=stream,
        timeout=60
    )
    
    if not stream:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    
    # Streaming response
    full_response = ""
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                data = line[6:]
                if data == '[DONE]':
                    break
                try:
                    chunk = json.loads(data)
                    if 'choices' in chunk and chunk['choices']:
                        delta = chunk['choices'][0].get('delta', {})
                        if 'content' in delta:
                            content = delta['content']
                            full_response += content
                            print(content, end='', flush=True)
                except:
                    pass
    
    print()  # New line after response
    return full_response


def main():
    print("🤖 LLM Calculator - Type 'exit' to quit\n")
    print(f"Powered by: {HF_SPACE_URL}\n")
    
    while True:
        try:
            prompt = input("📝 Enter math problem: ").strip()
            
            if prompt.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not prompt:
                continue
            
            print("🤔 ", end='', flush=True)
            calculate(prompt)
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    # If arguments provided, calculate directly
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        print(f"Calculating: {prompt}")
        calculate(prompt)
    else:
        main()
