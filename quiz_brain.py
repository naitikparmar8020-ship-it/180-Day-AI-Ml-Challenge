# todo 1 :asking the question
# todo 2 : checking the answer was correct
# todo 3 : checking if we're the end of the quiz

# create a class called Quizbrain
# write an __init__() method 
# inistilise the que_num=0
# inistilise the que_list= to in input

class QuizBrain:
    def __init__(self,q_list):
        self.que_no=0
        self.score=0
        self.que_list =  q_list

    def still_has_que(self):
        return self.que_no < len(self.que_list)
            
    #    retrive the current item at the current que_num from the que_list
    #    use input function to show user the que text and ask for the user's answer 
    def next_question(self):
        current_que=self.que_list[self.que_no]
        self.que_no+=1
        user_answer=input(f"Q{self.que_no}: {current_que.text} (true or false):- ")
        self.check_answer(user_answer,current_que.answer)

    def check_answer(self,user_answer,correct_answer):
        
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
            # print(f"your current score is {self.score}")
        else:
            print("that's the wrong")
            self.score+=0
            
        print(f"the correct answer was:{correct_answer}.")
        print(f"your current score is {self.score}/{self.que_no}")
        print("\n")