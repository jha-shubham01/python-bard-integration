from bardapi import ChatBard
from defaults import BARD_KEY


bard = ChatBard(token=BARD_KEY, language="english")

response = bard.start()
