from collections import deque


def gather_credits(required_credits, *args):
    courses = []
    gathered_credits = 0
    available_courses = deque(args)

    while available_courses:
        if gathered_credits >= required_credits:
            break

        course, points = available_courses.popleft()

        if course not in courses:
            gathered_credits += points
            courses.append(course)

    if gathered_credits < required_credits:
        credits_shortage = required_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(courses))}"