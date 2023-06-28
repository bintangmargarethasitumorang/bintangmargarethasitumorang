#include "student.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct student_t create_student(char *_id, char *_name, char *_year, enum gender_t _gender)
{
    struct student_t stu;

    strcpy(stu.id, _id);
    strcpy(stu.name, _name);
    strcpy(stu.year, _year);
    stu.gender = _gender;

    return stu;
}

void print_student(struct student_t *_student, int jumlah)
{
    for (int j = 0; j < jumlah; j++)
    {
        if(_student[j].gender == 1)
        {
            printf("%s|%s|%s|female\n", _student[j].id, _student[j].name, _student[j].year);
        }
        else
        {
            printf("%s|%s|%s|male\n", _student[j].id, _student[j].name, _student[j].year);
        }
    }
}
