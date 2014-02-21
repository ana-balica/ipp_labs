import json


class CoursesModel(object):
    """ Model class for Courses of type Domain Model
    """
    def __init__(self, storage):
        """ Initialiser

        @param: storage file path
        """
        self.storage = storage

        json_data = open(storage)
        self.data = json.load(json_data)
        json_data.close()

    def save(self):
        """ Save all the changes occured to the data
        """
        with open(self.storage, "w") as f:
            json.dump(self.data, f, sort_keys=True, indent=4, separators=(',', ': '))

    def insert_course(self, course):
        """ Insert new course data

        @param course: dict describing course data - can contain title, credits, etc
        @return: updated Course storage
        """
        largest_id = max([int(i) for i in self.data.keys()])
        new_course_id = str(largest_id + 1)
        self.data[new_course_id] = course
        return self.data

    def update_title(self, course_id, title):
        """ Update the title of a course

        @param course: course id
        @param title: string new title of the course
        @return: updated Course dict or None if such course_id doensn't exist
        """
        if course_id:
            if self.data.get(course_id):
                self.data[course_id]["title"] = title
                return self.data[course_id]
        return None

    def find_course_by_title(self, title):
        """ Find a course by a title

        @param: string title
        @return: Course dict or None if nothing found
        """
        for key, value in self.data.iteritems():
            if self.data[key]["title"] == title:
                return self.data[key]
        return None


if __name__ == '__main__':
    courses_model = CoursesModel("data/courses.json")
    courses_model.update_title("2", u"No title haha")    
    courses_model.insert_course({"title": "PSI", "credits": 4, "workload": 80})
    print courses_model.data
    courses_model.save()

    print courses_model.find_course_by_title("IPP")
