from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

# Predefined mental health questions in Moroccan Darija
mental_health_questions = [
    "السلام عليكم، كيداير اليوم؟",
    "شنو اللي مقلقك؟",
    "واش كتقدر تنعس مزيان؟",
    "واش كتحس براسك وحيد؟",
    "واش عندك شي نشاطات اللي كتعجبك ديرها فوقت الفراغ؟",
    "واش الناس اللي حواليك كيدعموك؟",
    "كيفاش كتتعامل مع المشاكل اللي كتصادفك؟"
]

# To keep track of the conversation state
conversation_state = {
    "current_question_index": 0,
    "answers": []
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/audiocall')
def audiocall():
    return render_template('audiocall.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['user_message']
    
    # Add user message to conversation state
    conversation_state['answers'].append(user_message)
    
    # Wait for 2 seconds before responding
    time.sleep(0.5)
    
    # Check if we need to ask the next mental health question
    if conversation_state['current_question_index'] < len(mental_health_questions):
        bot_response_in_darija = mental_health_questions[conversation_state['current_question_index']]
        conversation_state['current_question_index'] += 1
    else:
        # Generate the final report
        bot_response_in_darija = """
        من خلال الأجوبة ديالك، واضح بلي عندك ضغوطات كبيرة من الخدمة والحياة اليومية، وهذا كيتسبب ليك فقلة النوم وكترة التفكير. كتحس بالوحدة حتى فوجود الناس، وما بقاتش عندك الطاقة تمارس الهوايات اللي كتعجبك بحال القراءة. كتعاني من نقص الدعم العاطفي والاهتمام من الناس اللي حواليك، وكتواجه المشاكل بطريقة سلبية عن طريق التهرب منهم.

        بناءً على هاد الشي، غادي نوصي ببعض الخطوات اللي تقدر تعاونك:

        1. حاول نلقى طرق لتخفيف الضغوطات اليومية.
        2. دير جلسات استرخاء وتمارين التنفس لتحسين النوم.
        3. حاول نبني شبكة دعم عاطفي أقوى مع العائلة والأصدقاء.
        4. واجه المشاكل بطرق بناءة ومباشرة بدلاً من التهرب منهم.
        """
    
    return jsonify({"bot_response": bot_response_in_darija})

@app.route('/reset_conversation', methods=['POST'])
def reset_conversation():
    conversation_state['current_question_index'] = 0
    conversation_state['answers'] = []
    return jsonify({"message": "Conversation reset."})

if __name__ == '__main__':
    app.run(debug=True)
