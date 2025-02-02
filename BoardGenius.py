import json
import copy
import random
from math import floor
import copy

class BoardGenius:
	def __init__(self,give_score,give_action,action_resualt,toggle_turn):
		self.score=give_score
		self.action=give_action
		self.action_r=action_resualt
		self.toggle=toggle_turn


	def minmax_search(self,step,board,turn,is_valid,has_valid):
		act,s=self.max_value(board,step,turn,float('inf'),is_valid,has_valid)

		return act

	def max_value(self,board,step,turn,limit,is_valid,has_valid):
		opponent = self.toggle(turn)
		if(step==-1 or not has_valid(board, turn)): return -1,self.score(board,turn)
		score=0
		act=-1
		for i in self.action():
			if(is_valid(board,i,turn)):
				temp_board= copy.deepcopy(board)
				self.action_r(temp_board,i,turn)
				#if (step == self.STEP-1 and self.score(board,opponent)==0):
				#	return i,j,0
				temp_act,s=self.min_value(temp_board,step-1,opponent,score,is_valid,has_valid)
				if (s > score and s>0):
					score=s
					act=i
					if(s>limit):
						return -1,0
				

		return act,score


	def min_value(self,board,step,turn,limit,is_valid,has_valid):
		opponent = self.toggle(turn)
		if(step==-1 or not has_valid(board, turn)): return -1,self.score(board,opponent)
		score=float('inf')
		act=-1
		for i in self.action():
			if(is_valid(board,i,turn)):
				temp_board= copy.deepcopy(board)
				self.action_r(temp_board,i,turn)
				temp_act,s=self.max_value(temp_board,step-1,opponent,score,is_valid,has_valid)
				if (s < score and s >0):
					score=s
					act=i
					
					if(s<limit):
						return -1,0

		return act,score


class MyStruct:
    def __init__(self, number, father, win, loss, state):
        self.number = number
        self.father = father
        self.win = win
        self.loss=loss
        self.state = state

    def to_dict(self):
        return {
            str(self.number):{
            'father': self.father,
            'win': self.win,
            'number': self.loss,
            'state': self.state
            }
        }

class DataStruct:
    def __init__(self,*path_):
        self.path="data.json"
        if len(path_)==1:
            self.path=path_[0]
        if not path.endswith(".json"):
            path=str(path)+".json"
		
    def save(self,data,win): 
        fe=self.fetch()
        for key, value in data.items():
             if key in fe:
                 fe[key] = value 
             else:
                 fe.update(data)

        father=list(data.values())[0]["father"]
        while(father != -1):
            
             data={str(father):fe[str(father)]}
             data[str(father)]['number']+=1
             if win == 1:
                 data[str(father)]['win']+=1

             for key, value in data.items():
                if key in fe:
                    fe[key] = value 
                else:
                    fe.update(data)

             father=list(data.values())[0]["father"]


             with open(self.path, "w", encoding="utf-8") as json_file:
                json.dump(fe, json_file, ensure_ascii=False, indent=4)




    def fetch(self):
        try:
        
            with open(self.path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        return data
        
