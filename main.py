from user import User

app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

app_user_one.change_job_title("DevOps trainer")
app_user_one.get_user_info()