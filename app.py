from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
Generate sales outreach for {name} at {company}:
- Role: {title}
- Industry: {industry}
- Revenue: {revenue}
- Recent news: {news}
Template: Casual, problem-solving tone. Max 150 words.
"""

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/generate-outreach', methods=['POST'])
def generate_outreach():
    lead = request.json
    prompt = PROMPT_TEMPLATE.format(**lead)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    return jsonify({
        "email": response.choices[0].message.content,
        "call_script": f"Hi {lead['name']}, I noticed {lead['company']}...",
        "linkedin": f"Congrats on {lead['news']}! Would love to connect..."
    })

if __name__ == '__main__':
    app.run(debug=True)
