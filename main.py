from collections import defaultdict
from collections import OrderedDict
from parse import read_data
from pprint import pprint
import os

def fill_role(p, available_contributors):

    chosen_contributors = []
    potential_contributors = []
    for r, s in p.roles.items():
        for a in available_contributors:
            if r in a.skills and a.skills[r] >= s and a not in potential_contributors:
                potential_contributors.append(a)
                break
        if len(potential_contributors) == p.n_roles:
            while potential_contributors:
                chosen_contributors.append(potential_contributors.pop(0))

    return chosen_contributors

if __name__ == "__main__":
    #filepaths = os.listdir("input")
    filepaths = ["e_exceptional_skills.in.txt"]
    for filepath in filepaths: 
        available_contributors, projects = read_data("input/" + filepath)
        calendar = defaultdict(lambda: set())
        projects = sorted(projects, key = lambda x: (x.dead, x.score), reverse = False)
        result = OrderedDict()


        last_day = 0
        # Calculate while duration
        for p in projects:
            last_worth_day = p.dead + p.score - p.days
            if  last_worth_day > last_day:
                last_day = last_worth_day

        day = 0
        while day < last_day:
            # Make available contributors back
            if day != 0 and day not in calendar.keys():
                day += 1
                continue
            if calendar[day]:
                available_contributors = available_contributors.union(calendar[day])

            # Remove worthless projects
            #for p in projects[:]:
            #    if not p.is_worth(day):
            #        projects.remove(p)

            # Fill for current projects
            for p in projects[:]:
                chosen = fill_role(p, available_contributors)
                if chosen:
                    for i in range(len(p.roles.items())):
                        role, level = list(p.roles.items())[i]
                        if chosen[i].skills[role] == level or chosen[i].skills[role] == level - 1:
                            chosen[i].skills[role] += 1
                    calendar[day + p.days] = calendar[day + p.days].union(set(chosen))
                    available_contributors = available_contributors - set(chosen)
                    projects.remove(p)
                    result[p.name] = " ".join([c.name for c in chosen])
            #print(day, last_day)
            day += 1
            if day == 1900:
                break

        # result to file
        res = str(len(result)) + "\n"
        for key in result:
            res += key + "\n" + result[key] + "\n"
        with open("output/" + filepath, "w+") as out:
            out.write(res)
            

