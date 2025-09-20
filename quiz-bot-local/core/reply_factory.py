from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")

    if current_question_id is None:
        bot_responses.append(BOT_WELCOME_MESSAGE)
        next_question, next_question_id = get_next_question(-1) 
        bot_responses.append(next_question)
        session["current_question_id"] = next_question_id
        session["score"] = 0
        session["responses"] = []
        session.save()
        return bot_responses

    success, error = record_current_answer(message, current_question_id, session)
    if not success:
        return [error]
    
    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    if current_question_id < 0 or current_question_id >= len(PYTHON_QUESTION_LIST):
        return False, "Invalid question ID."

    question_data = PYTHON_QUESTION_LIST[current_question_id]
    correct_answer = question_data["answer"]

    is_correct = str(answer).strip().lower() == str(correct_answer).strip().lower()

    responses = session.get("responses", [])
    responses.append({
        "question": question_data["question_text"],
        "options": question_data["options"],
        "user_answer": answer,
        "correct_answer": correct_answer,
        "is_correct": is_correct
    })
    session["responses"] = responses

    if is_correct:
        session["score"] = session.get("score", 0) + 1

    return True, ""


def get_next_question(current_question_id):

    next_id = current_question_id + 1
    if next_id < len(PYTHON_QUESTION_LIST):
        q = PYTHON_QUESTION_LIST[next_id]
        question_str = f"\nQ{next_id+1}: {q['question_text']}\n"
        for i, opt in enumerate(q["options"], start=1):
            question_str += f"{i}. {opt}\n"
        return question_str, next_id
    return None, -1


def generate_final_response(session):

    total = len(PYTHON_QUESTION_LIST)
    score = session.get("score", 0)
    responses = session.get("responses", [])

    result_msg = f"\n Quiz Finished!\nYour Score: {score}/{total}\n\n"

    for idx, r in enumerate(responses, start=1):
        result_msg += f"Q{idx}: {r['question']}\n"
        result_msg += f"Your Answer: {r['user_answer']} | Correct: {r['correct_answer']}\n"
        result_msg += f"Result: {'Correct' if r['is_correct'] else 'Wrong'}\n\n"

    return result_msg
