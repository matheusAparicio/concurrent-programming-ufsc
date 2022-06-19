#include <stdlib.h>
#include "globals.h"

// Acredito que vamos precisar de um total de mesas!
queue_t *students_queue = NULL;
table_t *table = NULL;
buffet_t *buffets_ref = NULL;

int students_number = 0;

int number_of_tables = 0;
int seats_per_table = 0;
int all_students_entered = 0;
int students_inside_number = 0;

// Implementados pelo aluno ----------


void globals_set_students_inside(int number)
{
    students_inside_number = number;
}

int globals_get_students_inside()
{
    return students_inside_number;
}


void globals_set_all_students_entered(int bool)
{
    all_students_entered = bool;
}

int globals_get_all_students_entered()
{
    return all_students_entered;
}


void globals_set_table_quantity(int number)
{
    number_of_tables = number;
}

int globals_get_table_quantity()
{
    return number_of_tables;
}

void globals_set_seats(int number)
{
    seats_per_table = number;
}

int globals_get_seats()
{
    return seats_per_table;
}

// Fim dos implementados pelo aluno ----------

void globals_set_queue(queue_t *queue)
{
    students_queue = queue;
}

queue_t *globals_get_queue()
{
    return students_queue;
}

void globals_set_table(table_t *t)
{
    table = t;
}

table_t *globals_get_table()
{
    return table;
}


void globals_set_students(int number)
{
    students_number = number;
}

int globals_get_students()
{
    return students_number;
}

void globals_set_buffets(buffet_t *buffets)
{
    buffets_ref = buffets;
}

buffet_t *globals_get_buffets()
{
    return buffets_ref;
}


/**
 * @brief Finaliza todas as variáveis globais que ainda não foram liberadas.
 *  Se criar alguma variável global que faça uso de mallocs, lembre-se sempre de usar o free dentro
 * dessa função.
 */
void globals_finalize()
{
    free(students_queue);
    free(table);
    free(buffets_ref);
}