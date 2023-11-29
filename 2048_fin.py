import numpy as np
import random 
from tkinter import *
import keyboard
from tkinter import messagebox

N=4
class game2048:
    color={'2':'#6D214F','4':'#182C61','8':'#FC427B','16':'#82589F','32':'#3B3B98',
            '64':'#EAB543','128':'#58B19F','256':'#D6A2E8','512':'#FEA47F','1024':'#eb2f06',
            '2048':'#A3CB38',2:'#81ecec','you':'#f6b93b', 'won':'#3B3B98','Game':'#2C3A47','Over':'#341f97'}
    bg_color={'2': '#eee4da','4': '#ede0c8','8': '#ffcccc','16': '#a29bfe','32': '#f67c5f',
            '64': '#f65e3b','128': '#edcf72','256': '#b71540','512': '#f2b179','1024': '#f59563',
            '2048': '#edc22e',2:'#fdcb6e',3:'#4a69bd', 'you':'#6D214F','won':'#F8EFBA','Game':'#eb2f06','Over':'#eb2f06'}
    def __init__(self):
        self.m1=np.zeros((N,N),dtype=int)
        self.score=0
        self.m=0
        self.board=[]
        self.merg=False
        self.moved=False
        self.compress=False
        self.new_m1=[]
        for i in range(N):
            self.new_m1.append([0]*4)
        self.window=Tk()
        self.window.title("2048 Game")
        self.area=Frame(self.window,bg=self.color.get(2))

        for i in range(N):
            rows=[]
            for j in range(N):
                l=Label(self.area,text='',bg=self.bg_color.get(2),
                font=('arial',20,'bold'),width=6,height=3)
                l.grid(row=i,column=j,padx=4,pady=4)
                rows.append(l)
            self.board.append(rows)
        self.area.grid() 

    def randomchoice(self):
        cell=[]
        for i in range(N):
            for j in range(N):
                if self.m1[i][j] == 0:
                    cell.append((i, j))
        curr=random.choice(cell)
        i=curr[0]
        j=curr[1]
        r=random.random()
        if r<0.2:
            self.m1[i][j]=4
        else:
           self.m1[i][j]=2

    def paint(self):
        for i in range(N):
            for j in range(N):
                if self.m1[i][j]!=0:
                    self.board[i][j].config(text=str(self.m1[i][j]),
                    bg=self.bg_color.get(str(self.m1[i][j])),
                    fg=self.color.get(str(self.m1[i][j])))
                elif self.m1[i][j]=='you':
                    self.board[i][j].config(text='you'),
                    bg=self.bg_color.get('you'),
                    fg=self.color.get('you')
                elif self.m1[i][j]=='won':
                    self.board[i][j].config(text='won'),
                    bg=self.bg_color.get('won'),
                    fg=self.color.get('won')
                elif self.m1[i][j]=='Game':
                    self.board[i][j].config(text='Game'),
                    bg=self.bg_color.get('Game'),
                    fg=self.color.get('Game')
                elif self.m1[i][j]=='Over':
                    self.board[i][j].config(text='Over'),
                    bg=self.bg_color.get('Over'),
                    fg=self.color.get('Over')
                else:
                    self.board[i][j].config(text='',
                    bg=self.bg_color.get(3))
    
    def compresscell(self):
        self.compress=False
        self.temp=[]
        for i in range(N):
            self.temp.append([0]*4)
        for i in range(4):
            poss=0
            for j in range(4):
                if self.m1[i][j]!=0:
                    self.temp[i][poss]=self.m1[i][j]
                    if poss!=j:
                        self.compress=True
                    poss+=1
        self.m1=self.temp

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.m1[ind][i],self.m1[ind][j]=self.m1[ind][j],self.m1[ind][i]
                i+=1
                j-=1

    def merge(self):
        self.merg=False
        for i in range(N):
            for j in range(N - 1):
                if self.m1[i][j] != 0 and self.m1[i][j] == self.m1[i][j + 1]:
                    self.m1[i][j] *= 2
                    self.m1[i][j + 1] = 0
                    self.score += self.m1[i][j]
                    self.merg = True

    def transpose(self):
        self.m1=[list(t)for t in zip(*self.m1)]
    
    def canMerge(self):
        for i in range(N):
            for j in range(N-1):
                if (self.m1[i][j+1]==self.m1[i][j]):
                    return True
        for i in range(N-1):
            for j in range(N):
                if (self.m1[i][j]==self.m1[i+1][j]):
                    return True
        return False

    def eXit(self):
        result=messagebox.askokcancel('Yes or No','Do you want to Exit this game?')
        if result==True:
            exit()
        elif result==False:
            pass
    
    def StartAgain(self):
        result=messagebox.askokcancel('Yes or No','Are you sure you want to restart the game?')
        if result==True:
            gamepanel=game2048()
            game208=game(gamepanel)
            game208.start()

    def Max(self):
        for i in range(N):
            for j in range(N):
                if ((isinstance(self.m1[i][j], int))and((isinstance(self.m, int)))):
                    
                    if self.m1[i][j]>self.m:
                        self.m=self.m1[i][j]
        print('Max value is:',self.m)

class game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.won=False
        self.end=False
        self.harkat=0

    def start(self):
        self.gamepanel.randomchoice()
        self.gamepanel.randomchoice()
        self.gamepanel.paint()
        self.gamepanel.window.bind('<Key>',self.keyy)
        self.gamepanel.window.mainloop()

    def keyy(self,event):
        if self.won or self.end:
            return
        self.gamepanel.compress = False
        self.gamepanel.moved = False
        self.gamepanel.merg = False
        
        event=keyboard

        if event.is_pressed('Left'):
            self.gamepanel.compresscell()
            self.gamepanel.merge()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merg
            self.gamepanel.compresscell()
            self.harkat+=1

        elif event.is_pressed('Right'):
            self.gamepanel.reverse()
            self.gamepanel.compresscell()
            self.gamepanel.merge()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merg
            self.gamepanel.compresscell()
            self.gamepanel.reverse()
            self.harkat+=1

        elif event.is_pressed('Up'):
            self.gamepanel.transpose()
            self.gamepanel.compresscell()
            self.gamepanel.merge()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merg
            self.gamepanel.compresscell()
            self.gamepanel.transpose()
            self.harkat+=1
            
            
        elif event.is_pressed('Down'):
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compresscell()
            self.gamepanel.merge()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merg
            self.gamepanel.compresscell()
            self.gamepanel.reverse()
            self.gamepanel.transpose()
            self.harkat+=1

        elif event.is_pressed('q'):
            self.gamepanel.eXit()

        elif event.is_pressed('r'):
            self.gamepanel.StartAgain()

        else:
            pass
        
        self.gamepanel.paint()
        print('your score:',self.gamepanel.score,'Harkat:',self.harkat)

        temp=0
        for i in range(N):
            for j in range(N):
                if (self.gamepanel.m1[i][j]==2048):
                    temp=1
                    break
        if temp==1:
            self.won=True
            self.gamepanel.m1[1][1]='you'
            self.gamepanel.m1[1][2]='won'

        for i in range(4):
            for j in range(4):
                if self.gamepanel.m1[i][j]==0:
                    temp=1
                    break

        if not (temp or self.gamepanel.canMerge()):
            self.end=True
            self.gamepanel.m1[1][1]='Game'
            self.gamepanel.m1[1][2]='Over'
            self.gamepanel.Max()

        if self.gamepanel.moved:
            self.gamepanel.randomchoice()
        
        self.gamepanel.paint()

gamepanel=game2048()
game208=game(gamepanel)
game208.start()