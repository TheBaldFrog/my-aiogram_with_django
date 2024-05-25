from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")

# DB
DBHOST = env.str("DBHOST")
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
