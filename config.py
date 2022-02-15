from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
car1 = env.list("car1") 