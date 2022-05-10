from Sessions import SessionHandler

class SingleSessionHandler(SessionHandler):
	def __init__(self, fpath: str, numOfWordsToGuess: int) -> None:
		super().__init__(fpath, numOfWordsToGuess)

	def guess(self, token : str, answer : str):
		if (token in self.userMap):
			userWordle = self.getWordle(token)
			output = userWordle.guess(answer)
			print(f'[User {token}] Answer status : {output}')

			# meaning, the answer is correct
			if ((0 not in output) and (1 not in output)):
				userWordle.proceed()

			return output

		print(f'[User {token}] Answer {answer} cannot be checked because the token is not registered.')
		return []