class School(object):
    def __init__(self, name=object, roster={}):
        self.name = name
        self.roster = roster
    
    def add_student(self, name=None, grade=None):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
    
    def grade(self, number=None):
        return self.roster[number]
    
    def sort_roster(self):
        for s in self.roster:
            self.roster[s].sort()
        return self.roster
        


