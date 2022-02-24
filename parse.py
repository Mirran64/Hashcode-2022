
from collections import OrderedDict


class Contributor:
    def __init__(self, name, skills):
        self.name = name 
        self.skills = skills

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}, {self.skills}"

class Project:
    def __init__(self,  name, days, score, dead, n_roles, roles):
        self.name = name 
        self.days = days 
        self.score = score
        self.dead = dead
        self.n_roles = n_roles
        self.roles = roles

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_worth(self, today):
        return self.dead + self.score - self.days > today


def read_data(filename):
    with open(filename, "r") as f:

        lines = f.read().split('\n')
        n_cotributors, n_projects = int(lines[0].split()[0]), int(lines[0].split()[1])
        contributors, projects = set(), list()

        indx = 1
        for c in range(n_cotributors):
            name, n_skills = lines[indx].split()[0], int(lines[indx].split()[1])
            skills = {}
            indx += 1
            for s in range(n_skills):
                skills[lines[indx].split()[0]] = int(lines[indx].split()[1])
                indx += 1
            contributors.add(Contributor(name, skills))


        for c in range(n_projects):
            name, days, score, dead, n_roles = lines[indx].split()[0], int(lines[indx].split()[1]), int(lines[indx].split()[2]), int(lines[indx].split()[3]), int(lines[indx].split()[4])
            roles = OrderedDict()
            indx += 1
            for s in range(n_roles):
                roles[lines[indx].split()[0]] = int(lines[indx].split()[1])
                indx += 1
            projects.append(Project(name, days, score, dead, n_roles, roles))

        return contributors, projects
