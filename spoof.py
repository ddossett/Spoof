import getpass
import sys
import random
import textwrap

class spoof:
"""Spoof the game"""

	_list_Players = []
	def __init__(self):
		self._titleCard()
		str_Description = 'This is a game for as many players as you want (>1). You should each think of a number of coins between 0 and 3 and enter it (covertly) when prompted. Then when asked, enter in your guess for the total number of coins. Easy!'
		print textwrap.fill(str_Description,width=60)
		self._runRound()

	def _titleCard(self):
		str_Welcome = 'Welcome to Spoof'
		print
		print ('{:/^20}'.format('')).center(60)
		print ('{:/^20}'.format(str_Welcome)).center(60)
		print ('{:/^20}'.format('')).center(60)
		print

	def _checkInt(self,i):
		try:
			int(i)
			return True
		except ValueError:
			print '\nEntered Value wasn\'t a number. Please Try again.'
			return False

	def _checkValidGuess(self,guess,numPlayers):
		maxCoins = numPlayers*3
		if guess<=maxCoins:
			return True
		else:
			return False

	def _getHumanThrow(self,i,list_Players):
		str_NumPrompt = 'enter your number of coins: '
		tmpNumCoins = getpass.getpass(prompt='\n'+list_Players[i]+' '+str_NumPrompt)
		return tmpNumCoins

	def _getComputerThrow(self,i,list_Players):
		print '\n'+list_Players[i]+' is throwing...'
		tmpNumCoins = random.randint(0,3)
		return tmpNumCoins

	def _getThrow(self,i,list_Players,human=False):
		tmpNumCoins = 0
		if human:
			tmpNumCoins = self._getHumanThrow(i,list_Players)
		else: tmpNumCoins = self._getComputerThrow(i,list_Players)
		return tmpNumCoins

	def _getHumanGuess(self,i,list_Players):
		str_GuessPrompt = 'enter your guess for the sum: '
		tmpGuess = getpass.getpass(prompt='\n'+list_Players[i]+' '+str_GuessPrompt)
		return tmpGuess
	
	def _getComputerGuess(self,i,list_Players):
		print '\n'+list_Players[i]+' is guessing...'
		maxCoins = len(list_Players)*3
		tmpGuess = random.randint(0,maxCoins)
		return tmpGuess

	def _getGuess(self,i,list_Players,human=False):
		guess = 0
		if human:
			guess = self._getHumanGuess(i,list_Players)
		else:
			guess = self._getComputerGuess(i,list_Players)
		return guess

	def _runRound(self):
		numPlayers = 0
		while numPlayers==0:
			tmpNumPlayers = getpass.getpass(prompt='\nHow many players do you want?')
			if self._checkInt(tmpNumPlayers):
				numPlayers = int(tmpNumPlayers)
			else:
				print '\nThat\'s not a valid number. Please try again.'
				continue
		
		list_Players = []
		str_PlayerNameRoot = 'Player'
		for int_Player in range(numPlayers):
			list_Players.append(str_PlayerNameRoot+str((int_Player+1)))
		
		numCoins = [0]*len(list_Players)
		
		int_i = 0
		while int_i<len(list_Players):
			tmpNumCoins = self._getThrow(int_i,list_Players)
			if self._checkInt(tmpNumCoins):
				numCoins[int_i] = int(tmpNumCoins)
				int_i+=1
			else: continue
		
		int_Sum = 0
		for n in numCoins:
			int_Sum+=n
		
		guesses = [0]*len(list_Players)
		int_i = 0
		while int_i<len(guesses):
			tmpGuess = self._getGuess(int_i,list_Players)
			if self._checkInt(tmpGuess):
				print '\n'+list_Players[int_i]+' guessed',tmpGuess,"coins"
				if self._checkValidGuess(int(tmpGuess),len(guesses)):
					guesses[int_i] = int(tmpGuess)
					int_i+=1
				else:
					print '\nThat\'s not a valid guess. Please try again'
					continue
			else: continue
		
		print '\nSum of coins was',int_Sum
		str_CongratulateRound = 'wins this round!'
		int_j = 0
		winner = False
		for guess in guesses:
			if guess==int_Sum:
				print '\n'+list_Players[int_j],str_CongratulateRound
				winner=True
			int_j+=1
		
		if not winner: print '\nNoone won this round, try again.'

spoof()
