from bardapi import Bard
from defaults import BARD_KEY


bard = Bard(token=BARD_KEY)

response = bard.get_answer(str(input('Ask your question:')))
print(response['content'])
