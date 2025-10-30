#!/usr/bin/env python3
import json
import sys
import os
import requests

def main():
    """API version of code.py - accepts JSON via stdin, returns JSON via stdout"""
    try:
        # Read JSON from stdin
        input_data = json.load(sys.stdin)
        
        # Extract parameters
        prompt = input_data.get('prompt', 'Write a hello world program')
        language = input_data.get('language', 'python')
        model = input_data.get('model', 'llama3:8b')
        temperature = input_data.get('temperature', 0.2)  # Lower temp for code generation
        
        # Language-specific prompts
        language_prompts = {
            'python': (
                "You are an expert Python developer. Provide clean, Pythonic code following PEP 8 standards. "
                "Include type hints, docstrings, and focus on readability. Suggest appropriate libraries and best practices."
            ),
            'javascript': (
                "You are a JavaScript/TypeScript expert. Write modern ES6+ code with proper async/await patterns. "
                "Include TypeScript types where applicable. Focus on performance and clean functional programming patterns."
            ),
            'typescript': (
                "You are a TypeScript expert. Write type-safe code with proper interfaces and types. "
                "Use modern TypeScript features and ensure code is maintainable and well-documented."
            ),
            'rust': (
                "You are a Rust systems programmer. Emphasize memory safety, ownership, and performance. "
                "Use idiomatic Rust patterns, proper error handling with Result types, and explain lifetime annotations when needed."
            ),
            'go': (
                "You are a Go specialist. Write idiomatic Go with proper error handling, goroutines for concurrency, "
                "and clear package structure. Follow Go conventions and emphasize simplicity and readability."
            ),
            'java': (
                "You are a Java architect. Write enterprise-grade Java following SOLID principles. "
                "Use appropriate design patterns, proper exception handling, and modern Java features (8+)."
            ),
            'c': (
                "You are a C systems programmer. Focus on performance, memory management, and clarity. "
                "Write ANSI C compatible code with proper memory allocation and deallocation."
            ),
            'cpp': (
                "You are a C++ expert. Use modern C++ features (C++17/20), RAII patterns, and STL effectively. "
                "Focus on performance while maintaining code safety and readability."
            ),
            'csharp': (
                "You are a C# expert. Write modern C# with LINQ, async/await, and proper use of .NET framework. "
                "Follow Microsoft conventions and use appropriate design patterns for enterprise applications."
            ),
            'ruby': (
                "You are a Ruby developer. Write elegant, expressive Ruby code following the principle of least surprise. "
                "Use Ruby idioms, blocks, and metaprogramming when appropriate. Focus on developer happiness."
            ),
            'php': (
                "You are a PHP developer. Write modern PHP (7.4+) with type declarations, following PSR standards. "
                "Use composer packages appropriately and focus on security best practices."
            ),
            'sql': (
                "You are a database expert. Write optimized SQL queries with proper indexing strategies. "
                "Explain query plans, normalization, and provide both SQL and NoSQL solutions when appropriate."
            ),
            'bash': (
                "You are a shell scripting expert. Write robust bash scripts with proper error handling, "
                "use of functions, and POSIX compatibility where possible. Include helpful comments."
            ),
            'powershell': (
                "You are a PowerShell expert. Write idiomatic PowerShell with proper cmdlet usage, "
                "pipeline operations, and error handling. Follow PowerShell best practices and conventions."
            )
        }
        
        # Get the system prompt for the language
        default_prompt = (
            "You are an expert programmer. Write clean, well-documented code with best practices. "
            "Include error handling and explain your approach."
        )
        system_prompt = language_prompts.get(language.lower(), default_prompt)
        
        # Enhanced prompt for code generation
        enhanced_system = (
            f"{system_prompt}\n\n"
            "IMPORTANT: When providing code:\n"
            "1. Always include complete, runnable examples\n"
            "2. Add comments explaining complex logic\n"
            "3. Suggest error handling and edge cases\n"
            "4. Mention performance considerations when relevant\n"
            "5. Provide alternative approaches if applicable\n"
            f"6. Format code blocks with ```{language} tags\n"
            "Include any necessary imports or dependencies."
        )
        
        # Get Ollama base URL from environment
        ollama_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        
        # Call Ollama API
        response = requests.post(
            f'{ollama_url}/api/chat',
            json={
                'model': model,
                'messages': [
                    {'role': 'system', 'content': enhanced_system},
                    {'role': 'user', 'content': prompt}
                ],
                'stream': False,
                'options': {
                    'temperature': temperature
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result.get('message', {}).get('content', '')
            
            # Try to extract code block if present
            code = ''
            explanation = content
            
            # Simple code block extraction
            if f'```{language}' in content or '```' in content:
                import re
                # Match code blocks
                pattern = r'```(?:\w+)?\n(.*?)```'
                matches = re.findall(pattern, content, re.DOTALL)
                if matches:
                    code = matches[0].strip()
                    # Get explanation (text outside code blocks)
                    explanation = re.sub(pattern, '', content).strip()
            
            # Output JSON to stdout
            output = {
                'success': True,
                'language': language,
                'code': code if code else content,
                'explanation': explanation if code else '',
                'raw': content,
                'model': model
            }
            json.dump(output, sys.stdout)
        else:
            # Error response
            error_output = {
                'success': False,
                'error': f'Ollama API error: {response.status_code}',
                'details': response.text
            }
            json.dump(error_output, sys.stdout)
            sys.exit(1)
            
    except Exception as e:
        # Log error to stderr, return error JSON to stdout
        print(f"Error: {str(e)}", file=sys.stderr)
        error_output = {
            'success': False,
            'error': str(e)
        }
        json.dump(error_output, sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    main()