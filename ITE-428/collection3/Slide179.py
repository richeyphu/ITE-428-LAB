# Slide179
# Find % Skill match from Applicant

def percent_matched(a):
    return len(a & wantedskill) / len(wantedskill) * 100


wantedskill = {"C#", "Python", "Java", "PHP", "SQL", "Go"}
applicant1skill = {"VB", "C", "Ruby", "Java", "HTML"}
applicant2skill = {"C#", "HTML", "R", "PHP", "SQL", "Swift", "PHP"}
applicant3skill = {"Java", "C++", "Ruby", "JavaScript", "Objective-C", "Go"}
applicant4skill = {"Java", "Python", "Go", "SQL", "Swift"}
applicant5skill = {"C++", "C", "C#", "Objective-C", "JavaScript", "SQL"}

print("Applicant 1 skill match : {:.2f}%".format(percent_matched(applicant1skill)))
print("Applicant 2 skill match : {:.2f}%".format(percent_matched(applicant2skill)))
print("Applicant 3 skill match : {:.2f}%".format(percent_matched(applicant3skill)))
print("Applicant 4 skill match : {:.2f}%".format(percent_matched(applicant4skill)))
print("Applicant 5 skill match : {:.2f}%".format(percent_matched(applicant5skill)))
