import uuid

class UserDb:
    db = {}
    ACCOUNTID = '232'
    OMSID = '1'
    USERID = 100

    def add(self, key, value):
        properties = {
            'ID': len(self.db) + 1,
            'UserId': self.USERID,
            'Token': uuid.uuid1(),
            'AccountId': self.ACCOUNTID,
            'OMSId': self.OMSID
        }
        self.USERID += 1

        append_properties_to_value = dict(value)
        append_properties_to_value.update(properties)

        self.db[key] = append_properties_to_value

    def list(self):
        return [key for key in self.db.keys()]

    def get(self, key):
        if(key in self.db.keys()):
            return self.db[key]

        return None