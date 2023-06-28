// 12S21016 - Kevin Unedo Samosir
// 12S21023 - Bintang Margaretha Situmorang

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "./libs/dorm.h"
#include "./libs/student.h"

int main(int _argc, char **_argv)
{
    struct student_t *students = malloc(12 * sizeof(struct student_t));
    char data[100];
    char id[10];
    char name[25];
    char year[5];
    char *kata;
    int j = 0;

    do
    {
        data[0] = '\0';
        int k = 0;
        while (1==1)
        {
            char i = getchar();
            if (i == '\n')
            {
                break;
            }
            if (i == '\r')
            {
                continue;
            }
            data[k] = i;
            data[++k] = '\0';
        }
        if (strstr(data, "student-add")!=NULL)
        {
            kata = strtok(data, "#");
            kata = strtok(NULL, "#");
            strcpy(id, kata);
            kata = strtok(NULL, "#");
            strcpy(name, kata);
            kata = strtok(NULL, "#");
            strcpy(year, kata);
            kata = strtok(NULL, "#");
            if (strcmp(kata, "female")==0)
            {
                students[j] = create_student(id, name, year, GENDER_FEMALE);
            } 
            else if (strcmp(kata, "male")==0)
            {
                students[j] = create_student(id, name, year, GENDER_MALE);
            }
            ++j;
        }
        else if (strstr(data, "student-print-all")!=NULL) 
        {
            print_student(students, j);
        }
        if(strcmp(data, "---")==0)
        {
            break;
        } 
    } while (1 == 1);
    
    return 0;
}
