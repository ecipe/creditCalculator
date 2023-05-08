# 수강과목 정보 클래스
class Course:
    def __init__(self):
        self.info = input('과목명과 학점, 평점을 입력하세요: ')
        self.name = self.info.split(',')[0]
        self.credit = self.info.split(',')[1]
        self.gpa = self.info.split(',')[2]

    def allocate_course_id(self, course_name, course_id_map):
        if course_name not in course_id_map:
            new_id = str(int(course_id_map['basic']) + 1)
            course_id_map['basic'] = new_id
            course_id_map[course_name] = new_id
            course_id_map[new_id] = course_name
            return new_id, course_id_map

        else:
            return course_id_map[course_name], course_id_map

# 점수 변환 함수
def get_gpa_score(gpa):
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0

# 무한루프
course_id_map = {'basic': 10000}
archive_grade = {}
submit_grade = {}
total_input_info = []

while True:
    print("작업을 선택하세요.")
    print("     1. 입력")
    print("     2. 출력")
    print("     3. 조회")
    print("     4. 계산")
    print("     5. 종료")
    user_input = input()

    if user_input == '1':
        course = Course() #course.name, course.credit, course.gpa
        user_course_name = course.name
        user_credit = int(course.credit)
        user_gpa = course.gpa
        user_gpa_score = get_gpa_score(user_gpa)

        user_course_id, course_id_map = course.allocate_course_id(user_course_name, course_id_map)

        total_input_info.append((user_course_id, user_credit, user_gpa))

        if user_course_id in archive_grade:
            if user_gpa_score > archive_grade[user_course_id][1]:
                archive_grade[user_course_id] = (user_credit, user_gpa_score)
        else:
            archive_grade[user_course_id] = (user_credit, user_gpa_score)

        if user_gpa_score > 0.0:
            if user_course_id in submit_grade:
                if user_gpa_score > submit_grade[user_course_id][1]:
                    submit_grade[user_course_id] = (user_credit, user_gpa_score)
            else:
                submit_grade[user_course_id] = (user_credit, user_gpa_score)

        print('입력되었습니다.\n')

    elif user_input == '2':
        for i in range(len(total_input_info)):
            print('[' + course_id_map[total_input_info[i][0]] + ']' + str(total_input_info[i][1]) + '학점: ' +
                  total_input_info[i][2])

    elif user_input == '3':
        n = 0
        user_check = input('과목명을 입력하세요: ')
        if user_check in course_id_map:
            for i in range(len(total_input_info)):
                if course_id_map[total_input_info[i][0]] == user_check:
                    print('[' + course_id_map[total_input_info[i][0]] + ']' + str(total_input_info[i][1]) + '학점: ' + total_input_info[i][2])
                    n += 1
                    if(n==2):
                        break
        else:
            print('해당하는 과목이 없습니다.')

    elif user_input == '4':
        submit_credit, archive_credit = 0, 0
        submit_gpa_sum, archive_gpa_sum = 0, 0
        for user_course_id in submit_grade:
            credit = submit_grade[user_course_id][0]
            submit_credit += credit
            submit_gpa_sum += credit * submit_grade[user_course_id][1]
        for user_course_id in archive_grade:
            credit = archive_grade[user_course_id][0]
            archive_credit += credit
            archive_gpa_sum += credit * archive_grade[user_course_id][1]

        submit_gpa = submit_gpa_sum / submit_credit
        archive_gpa = archive_gpa_sum / archive_credit

        print('제출용: ' + str(submit_credit) + '(GPA: ' + str(round(submit_gpa, 2)) + ')')
        print('열람용: ' + str(archive_credit) + '(GPA: ' + str(round(archive_gpa, 2)) + ')')

    elif user_input == '5':
        print('프로그램을 종료합니다.')
        break