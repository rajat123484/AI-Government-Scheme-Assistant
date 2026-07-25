class ChatMemory:

    def __init__(self):
        self.profile = {}

    def update(self, key, value):
        self.profile[key] = value

    def get(self, key):
        return self.profile.get(key)

    def get_profile(self):
        return self.profile

    def clear(self):
        self.profile = {}