from homework6.oop_2 import Student, Teacher


def test_check_homework_result():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")

    opp_teacher.check_homework(Teacher.homework_done, result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(Teacher.homework_done, result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 is temp_2

    opp_teacher.check_homework(Teacher.homework_done, result_2)
    opp_teacher.check_homework(Teacher.homework_done, result_3)

    assert Teacher.homework_done[oop_hw].author.last_name == "Lev"
    Teacher.reset_results(Teacher.homework_done)
