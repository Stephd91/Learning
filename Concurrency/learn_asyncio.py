# Ressources :
# https://www.youtube.com/watch?v=GpqAQxH1Afc&ab_channel=ArjanCodes
# https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio
# https://www.youtube.com/watch?v=K56nNuBEd0c&ab_channel=Socratica

# TLDR :
#  Asyncio is essentially threading where not the CPU but you, as a programmer (or actually your application),
#  decide where and when does the context switch happen.
#  In Python you use an await keyword to suspend the execution of your coroutine (defined using async keyword).

import asyncio
from typing import List

import requests

###########################################
# 1)
###########################################


async def get_verbatims() -> List:
    endpoint = "/"
    new_token = 1
    verbatims = await requests.get(endpoint, headers=new_token)
    return verbatims
