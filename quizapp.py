
# Question Class 
class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz Object

class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self): 
        return self.questions[self.questionIndex] # getting questions of questionIndex


    def displayQuestion(self): # Method that prints Questions on the Screen!
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices: # Loop that displays answers as options!
            print('-' + q)

        answer = input('answer: ')
        print(question.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion() 
        # For the next question, we call the loadQuestion method so that we do not get an error when the number of questions runs out.

    def guess(self, answer):
        question = self.getQuestion() # Wrote down our question in this method so that we can check it with if!

        if question.checkAnswer(answer): # We check the correctness of the answer with if!
            self.score += 1 # If the question is answered correctly, the Score increases by 1!
        self.questionIndex += 1 

        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex: # if question number is equal to questionIndex length
            self.showScore() # The user's score is printed on the screen!
        else:
            self.displayProgress() # Showing Progress!
            self.displayQuestion() 

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions) 
        questionNumber = self.questionIndex + 1 

        if questionNumber > totalQuestion:
            print('Quiz is Over!')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(100,'*'))

q1 = Question('What is the best programming language?', ['C#', 'python', 'javascript', 'solidity'], 'javascript')             # questionIndex = 0
q2 = Question('What is the most popular programming language?', ['python', 'javascript', 'C#', 'solidity'], 'python')         # questionIndex = 1
q3 = Question('What is the most profitable programming language?', ['C#', 'solidity', 'python', 'javascript'], 'solidity')    # questionIndex = 2
q4 = Question('What is the most useful programming language?', ['C#', 'solidity', 'python', 'javascript'], 'C#')              # questionIndex = 3
q5 = Question('What is the newest programming language?', ['C#', 'solidity', 'python', 'javascript',], 'solidity')            # questionIndex = 4
questions = [q1,q2,q3,q4,q5] # We assigned our questions as a list to the 'questions' variable!

quiz = Quiz(questions)
quiz.loadQuestion()