#include <stdlib.h>
#include "table.h"

#include <stdio.h>
//TODO remover include stdio.h

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

table_t *table_init(int number_of_tables, int seats_per_table)
{
    printf("\n-------------------TABLE_INIT FUNCIONANDO-------------------\n");
    table_t *new_tables = malloc(sizeof(table_t) * number_of_tables);
    for (int i = 0; i < number_of_tables; i++)
    {
        new_tables[i]._id = i;
        new_tables[i]._empty_seats = seats_per_table;
        new_tables[i]._max_seats = seats_per_table;

        // Por gentileza, alterem a função (disponível em table.c):
        // able_t *table_init(int number_of_tables, int seats_per_table)
        // inserindo ali duas variáveis globais 
        // que possuem a quantidade de mesas do restaurante
        // e a quantidade de cadeiras por mesa.
        // Vocês podem implementá-la em globals.c.
    }

    return new_tables;
}