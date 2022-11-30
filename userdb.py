class UserDb:
    db = { 'test': { 'password': 'test1', 'email': 'test@email.com' } }

    def add(self, key, value):
        self.db[key] = value

    def list(self):
        return [key for key in self.db.keys()]