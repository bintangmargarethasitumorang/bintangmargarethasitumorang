// 12S21016 - Kevin Unedo Samosir
// 12S21023 - Bintang Margaretha Situmorang

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "./libs/dorm.h"
#include "./libs/student.h"

int main(int _argc, char **_argv)
{
    struct dorm_t *dorms = malloc(4 * sizeof(struct dorm_t));
    char data[100];
    char name[10];
    unsigned short capacity;
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
        if (strstr(data, "dorm-add")!=NULL)
        {
            kata = strtok(data, "#");
            kata = strtok(NULL, "#");
            strcpy(name, kata);
            kata = strtok(NULL, "#");
            capacity = atoi(kata);
            kata = strtok(NULL, "#");
            if (strcmp(kata, "female")==0)
            {
                dorms[j] = create_dorm(name, capacity, GENDER_FEMALE);
            } 
            else if(strcmp(kata, "male")==0) 
            {
                dorms[j] = create_dorm(name, capacity, GENDER_MALE);
            }
            ++j;
        }
        else if (strstr(data, "dorm-print-all")!=NULL) 
        {
            print_dorm(dorms, j);
        }
        if(strcmp(data, "---")==0)
        {
            break;
        } 
    } while (1==1);
  return 0;
}
