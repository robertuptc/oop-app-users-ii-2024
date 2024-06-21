from User import User

robert = User("Robert", "robert@mail.com")
print(robert)
robert.new_post = "first posting"
robert.new_post = "second posting"
robert.deleting_post(1)