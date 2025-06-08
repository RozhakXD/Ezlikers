from flask import render_template, request, jsonify, current_app
from app.main import bp
from app.services.qna_service import QnAService

chat_history = []

@bp.route('/', methods=['GET', 'POST'])
def index():
    global chat_history

    if request.method == 'POST':
        user_question = request.form.get('question')
        if not user_question:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'error': 'No question provided'}), 400

        qna_service_instance = QnAService()
        bot_answer, confidence = qna_service_instance.get_answer(user_question)

        chat_history.append({'sender': 'user', 'text': user_question})
        chat_history.append({'sender': 'bot', 'text': bot_answer, 'confidence': confidence})

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'user_question': user_question,
                'bot_answer': bot_answer,
                'confidence': confidence
            })

        return render_template('index.html',
                               title='EduPintar IPAS',
                               chat_history=chat_history)

    else:
        chat_history = []
        chat_history.append({
            'sender': 'bot',
            'text': 'Halo! Aku EduPintar. Siap belajar IPAS seru hari ini? Tanya apa saja tentang pelajaran IPAS kelas 6, ya!'
        })
        return render_template('index.html',
                               title='EduPintar IPAS',
                               chat_history=chat_history)