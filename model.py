import sqlite3
from sqlite3 import Error as SQLError
import random

class DrawModel:
    def __init__(self,subject):
        try:
            self.database = sqlite3.connect("zkouseni.db")
            command="SELECT * FROM Otazky WHERE zkratka= '" + subject +  "'"
            cur = self.database.cursor()
            cur.execute(command)
            self.questions = cur.fetchall()
            self.question=None
        except SQLError as e:
            print(e)
            
    def draw_question(self):
        if len(self.questions)>0:
            i=random.randint(0,len(self.questions)-1)
            self.question=self.questions[i]
            self.questions.pop(i)
        else:
            self.question=None
    
    def get_question(self):
        return self.question

