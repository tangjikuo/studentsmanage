class Student:
    """
    this class defined a student info
    """
    def __init__(self, stu_no, tea_no, score, name='', sex=''):
        self.name = name
        self.sex = sex
        self.stu_no = stu_no
        self.tea_no = tea_no
        self.score = score

    def query_info(self):
        sql = "select score from stedent where stu_no={0}".format(self.stu_no)
