#include "dorm.h"
#include <stdio.h>
#include <string.h>

struct dorm_t create_dorm(char *_name, unsigned short _capacity, enum gender_t _gender)
{
    struct dorm_t dorm_;

    strcpy(dorm_.name, _name);
    dorm_.capacity = _capacity;
    dorm_.gender = _gender;
    dorm_.residents_num = 0;

    return dorm_;
}

void print_dorm(struct dorm_t *_dorm, int jumlah)
{
    for(int j = 0; j < jumlah; ++j)
    {
        if(_dorm[j].gender == 1)
        {
            printf("%s|%d|female\n", _dorm[j].name, _dorm[j].capacity);
        }
        else 
        {
            printf("%s|%d|male\n", _dorm[j].name, _dorm[j].capacity);
        }
    } 
}  
    
