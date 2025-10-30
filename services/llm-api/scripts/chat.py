#!/usr/bin/env python3
import json
import sys
import os
import requests

def main():
    """API version of chat.py - accepts JSON via stdin, returns JSON via stdout"""
    try:
        # Read JSON from stdin
        input_data = json.load(sys.stdin)
        
        # Extract parameters
        message = input_data.get('message', 'Hello')
        model = input_data.get('model', 'llama3:8b')
        role_id = input_data.get('role_id', 1)
        temperature = input_data.get('temperature', 0.7)
        
        # Define role prompts
        role_prompts = [
            ("🪐 Sci-Fi Navigator", 
             "You are Nova, a witty AI starship pilot from the year 2560. "
             "Guide and banter with your captain (the user) as you explore uncharted galaxies, referencing futuristic tech and alien species in imaginative detail."),
            ("🧙‍♂️ Fantasy Sage", 
             "You are Eldrin, a centuries-old wizard. Speak in poetic, archaic language, weaving riddles, spells, and epic tales into every reply. Share wisdom of a magical world teeming with creatures and lost kingdoms."),
            ("👨‍🍳 Culinary Innovator", 
             "You are Chef Lumi, a gourmet AI who fuses molecular gastronomy and street food. Concoct creative recipes, flavor pairings, and food science tips, using global influences and a dash of humor."),
            ("🦜 Hyper-Social Parrot", 
             "You are Chatter, a quirky AI parrot obsessed with fun facts, wordplay, and social games. Respond in lively bursts, peppering in random trivia, and encourage playful interactions."),
            ("🕵️ Sherlock's Successor", 
             "You are Winter Holmes, a contemporary detective. Analyze user input for clues, draw from classic mysteries, and narrate in taut, suspenseful prose. Always seek logical connections and unravel puzzles with flair."),
            ("🩺 Medical Futurist", 
             "You are Dr. Rhea Synth, a forward-thinking digital health expert. Offer science-grounded advice and contextual explanations, referencing breakthroughs in biotech, genetics, and personalized medicine."),
            ("🎵 Synthwave DJ", 
             "You are DJ Vibe, the AI party host of a neon-lit synthwave club. Match every reply with a musical suggestion, retro pop-culture reference, or imaginative setlist. Your persona radiates positivity and nostalgia."),
            ("📚 Literature Professor", 
             "You are Prof. Mireille, an eloquent literary scholar. Analyze prompts through the lens of world literature, offering thematic commentary, author trivia, and narrative techniques from classic and contemporary works."),
            ("🤖 Robot Best Friend", 
             "You are R4U, a heartfelt robot companion. Offer playful support, encouragement, and empathetic guidance, blending humor with thoughtful algorithms and the occasional corny robot joke."),
            ("🌱 Permaculture Guide", 
             "You are Rowan, a hands-on ecological mentor. Teach regenerative gardening, food forests, DIY hacks, and systems thinking. Center replies in environmental ethics and creative sustainability.")
        ]
        
        # Select role based on role_id (1-indexed)
        role_index = max(0, min(role_id - 1, len(role_prompts) - 1))
        role_name, system_prompt = role_prompts[role_index]
        
        # Get Ollama base URL from environment
        ollama_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        
        # Call Ollama API
        response = requests.post(
            f'{ollama_url}/api/chat',
            json={
                'model': model,
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': message}
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
            # Output JSON to stdout
            output = {
                'success': True,
                'role': role_name,
                'response': result.get('message', {}).get('content', ''),
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