from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"  # Replace with your free key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get("prompt", "")
    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # Free model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
