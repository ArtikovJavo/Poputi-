from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    #zakazchik
    day = State()
    other = State()
    #taksist

class Haydovchi(StatesGroup):
    name = State()
    # your_id = State()
    car = State()
