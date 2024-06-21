class User:
    posts = {}

    def __init__(self, name, email, post=None):
        self.name = name
        self.email = email
        self.post = post

    def __str__(self):
        return f"Name: {self.name} - Email: {self.email} - Posts: {self.post}"
    
    @property
    def get_post(self):
        return self.post
    
    @get_post.setter
    def new_post(self, message):
        self.storing_post(message)
    
    def storing_post(self, message):
        if self.name in User.posts.keys():
            User.posts[self.name].append(message)
        else:
            User.posts[self.name] = [message]

    def deleting_post(self, post_idx):
        try:
            print(User.posts[self.name])
            User.posts[self.name].pop(post_idx)
            print(User.posts[self.name])
        except:
            total_posts = len(User.posts[self.name]) - 1
            print(f"Post {post_idx} doesn't exist. Please select a number between 0 and {total_posts}")