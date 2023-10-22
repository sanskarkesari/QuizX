from tkinter import * 
from tkinter import messagebox as mb 
import json 
import random


guiWindow = Tk() 


guiWindow.geometry("850x450") 


guiWindow.title("QuizX") 
 

class myQuiz: 



    def __init__(self,  max_questions=5):      

        

        self.quesNumber = 0 

        self.max_questions = max_questions


        self.displayTitle() 

        self.loadQuestions()

        self.displayQuestion() 


        self.optSelected = IntVar() 

 

        self.options = self.radioButtons() 


        self.displayOptions() 


        self.buttons() 


        self.dataSize =5 


        self.rightAnswer = 0


    def loadQuestions(self):
        global question, opts, answer
        data = json.load(open('data.json'))
        questions_and_choices = list(zip(data['ques'], data['choices'], data['ans']))
        random.shuffle(questions_and_choices)
        question, opts, answer = zip(*questions_and_choices)
        self.question_order = list(range(len(question)))


    def displayResult(self): 


        wrongCount = self.dataSize - self.rightAnswer 

        rightAnswer = f"Correct: {self.rightAnswer}" 

        wrongAnswer = f"Wrong: {wrongCount}" 

 

        the_score = int(self.rightAnswer / self.dataSize * 100) 

        the_result = f"Score: {the_score}%" 

 

        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}") 

 
    def checkAnswer(self): 

        ques_index = self.question_order[self.quesNumber]
        return self.optSelected.get() == answer[ques_index]



    def nextButton(self): 

        if self.checkAnswer():
            self.rightAnswer += 1
        self.quesNumber += 1
        if self.quesNumber == self.max_questions:
            self.displayResult()
            guiWindow.destroy()
        else:
            self.displayQuestion()
            self.displayOptions()
 


    def buttons(self): 

 

        next_button = Button( 

            guiWindow, 

            text = "Next", 

            command = self.nextButton, 

            width = 10, 

            bg = "blue", 

            fg = "white", 

            font = ("ariel", 16, "bold") 

            ) 


        next_button.place(x = 350, y = 380) 

 

        quit_button = Button( 

            guiWindow, 

            text = "Quit", 

            command = guiWindow.destroy, 

            width = 5, 

            bg = "black", 

            fg = "white", 

            font = ("ariel", 16, " bold") 

            ) 

 
        quit_button.place(x = 700, y = 50) 

 
    def displayOptions(self): 

        val = 0 

        self.optSelected.set(0) 


        for opt in opts[self.quesNumber]: 

            self.options[val]['text'] = opt 

            val += 1 

 

    def displayQuestion(self): 
        if self.quesNumber >= self.max_questions:  # Stop displaying questions if the limit is reached
            return
 
        ques_index = self.question_order[self.quesNumber]
        # setting the Question properties 
        ques_text = question[self.quesNumber]
        ques_number = self.quesNumber + 1

        quesLabel = Label( 

            guiWindow, 

            text = f"Q{ques_number}: {ques_text}", 

            width = 60, 

            font = ('ariel', 16, 'bold'), 

            anchor = 'w' 

            ) 


        quesLabel.place(x = 70, y = 100) 

 

    def displayTitle(self):          


        myTitle = Label( 

            guiWindow, 

            text = "QuizX", 

            width = 50, 

            bg = "blue", 

            fg = "white", 

            font = ("timesnewroman", 20, "bold") 

            ) 

 

        myTitle.place(x = 0, y = 2) 

 

    def radioButtons(self): 


        qList = [] 

        y_pos = 150 


        while len(qList) < 4: 


            radio_button = Radiobutton( 

                guiWindow, 

                text = " ", 

                variable = self.optSelected, 

                value = len(qList) + 1, 

                font = ("ariel", 14) 

                ) 


            qList.append(radio_button) 


            radio_button.place(x = 100, y = y_pos) 

 

            y_pos += 40 


        return qList 

 
with open('data.json') as json_file: 

    data = json.load(json_file) 

question = (data['ques']) 

opts = (data['choices']) 

answer = (data[ 'ans']) 

 
quiz = myQuiz() 


guiWindow.mainloop()
