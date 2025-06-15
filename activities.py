class Activities:
    def __init__(self):
        self.activities = []

    def __str__(self):
        for i in self.activities:
            print(i)
        return ''

    def add(self, activity):
        self.activities.append(activity)

    def remove(self, activity):
        self.activities.remove(activity)