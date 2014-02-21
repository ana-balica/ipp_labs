from model import CoursesModel
from view import render_template


def show_courses_info():
    """ Show all the information about courses
    """
    courses_model = CoursesModel("data/courses.json")
    data = transform_data(**courses_model.data)
    render_template("template.txt", **{'courses': data})


def transform_data(**data):
    """ Transform data from dict of dicts to a list of dicts

    @param data: key/value pairs of model data
    @return: list of dicts
    """
    new_data = []
    for course_id in data.keys():
        course = dict()
        for key, value in data[course_id].iteritems():
            course[key] = value
        new_data.extend([course])
    return new_data


if __name__ == '__main__':
    show_courses_info()
