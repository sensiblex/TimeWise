class Activities:
    def __init__(self):
        self.activities = {}

    def __str__(self):
        for k,v in self.activities.items():
            print(v)
        return ''

    def add(self, activity):
        self.activities[len(self.activities)+1] = activity

    def remove(self, n):
        del self.activities[n]
        temp = self.activities
        self.activities = {}
        ln = 1
        for k in temp.values():
            self.activities[ln] = k
            ln += 1

    def rename(self, n, new_name):
        self.activities[n].name = new_name