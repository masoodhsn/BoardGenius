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

