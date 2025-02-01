
def minmax_search(self,board,score_board,turn):
		t1,t2,s=self.max_value(board,self.STEP-1,score_board,turn,1000000)
		return t1,t2

def max_value(self,board,step,score_board,turn,limit):
	opponent = "W" if turn == "B" else "B"
	if(step==-1 or not self.has_valid_move(board, turn)): return -1,-1,self.score(board,turn,score_board)
	score=0
	ii,jj=-1,-1
	for i in range(self.BOARD_SIZE):
		for j in range(self.BOARD_SIZE):
			if(self.is_valid_move(board,i,j,turn)):
				temp_board= copy.deepcopy(board)
				self.apply_move(temp_board,i,j,turn)

				if (step == self.STEP-1 and self.score(board,opponent,score_board)==0):
					return i,j,0

				t1,t2,s=self.min_value(temp_board,step-1,score_board,opponent,score)
				if (s > score and s>0):
					score=s
					ii=i
					jj=j
					if(s>limit):
						return -1,-1,0
				

	return ii,jj,score


def min_value(self,board,step,score_board,turn,limit):
	opponent = "W" if turn == "B" else "B"
	if(step==-1 or not self.has_valid_move(board, turn)): return -1,-1,self.score(board,opponent,score_board)
	score=1000000
	ii,jj=-1,-1
	for i in range(self.BOARD_SIZE):
		for j in range(self.BOARD_SIZE):
			if(self.is_valid_move(board,i,j,turn)):
				temp_board= copy.deepcopy(board)
				self.apply_move(temp_board,i,j,turn)
				t1,t2,s=self.max_value(temp_board,step-1,score_board,opponent,score)
				if (s < score and s >0):
					score=s
					ii=i
					jj=j 
					if(s<limit):
						return -1,-1,0

	return ii,jj,score