import uuid

class SessionDb:
    db = {}

    def login(self):
        session = uuid.uuid4()
        self.db[session] = session
            
        return session

    def logout(self, session_id):
        self.db[session_id] = ''
    
    def isLogged(self, session_id):
        return (session_id in self.db) and (self.db[session_id] != '')