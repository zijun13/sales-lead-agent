from flask import Flask, request, jsonify
from skill.sales_agent import SalesAgent
import os

app = Flask(__name__)
agent = SalesAgent()

@app.route('/api/generate-talk', methods=['POST'])
def generate_talk():
    data = request.json
    lead_type = data.get('lead_type')
    customer_profile = data.get('customer_profile', {})
    
    talk = agent.generate_sales_talk(lead_type, customer_profile)
    return jsonify({"talk": talk})

@app.route('/api/analyze-needs', methods=['POST'])
def analyze_needs():
    data = request.json
    customer_data = data.get('customer_data', {})
    
    needs = agent.analyze_customer_needs(customer_data)
    return jsonify({"needs": needs})

@app.route('/api/suggest-action', methods=['POST'])
def suggest_action():
    data = request.json
    customer_profile = data.get('customer_profile', {})
    interaction_history = data.get('interaction_history', [])
    
    action = agent.suggest_next_action(customer_profile, interaction_history)
    return jsonify({"action": action})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)