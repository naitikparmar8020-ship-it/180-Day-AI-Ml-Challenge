from new_data import que_data
from question_model import Question
# write a for loop to itrate over the que_data. Create a que object from each entry
# in que_data.append each que_data into que_bank
from quiz_brain import QuizBrain
# quebank=Question()
Que_bank=[]


for questions in que_data["results"]:
    question_text=questions["question"]
    question_answer=questions["correct_answer"]
    new_question=Question(q_text=question_text,q_answer=question_answer)
    Que_bank.append(new_question)

quiz=QuizBrain(Que_bank)

while quiz.still_has_que(): 
    quiz.next_question()
print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.que_no}")
