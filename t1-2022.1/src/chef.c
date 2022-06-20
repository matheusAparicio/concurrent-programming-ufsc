#include <stdlib.h>

#include "chef.h"
#include "config.h"
#include "globals.h"

void *chef_run()
{
    /* Insira sua lógica aqui */
    // A cada aluno que se serve no buffet verifica se têm alguma bacia vazia

    printf("\n-------------------CHEF_RUN FUNCIONANDO-------------------\n");

    while (TRUE)
    {   
        chef_check_food();
        msleep(1000); /* Pode retirar este sleep quando implementar a solução! */
    }
    
    pthread_exit(NULL);
}


void chef_put_food()
{
    /* Insira sua lógica aqui */
}
void chef_check_food()
{
    /* Insira sua lógica aqui */
    // Verifica as bacias dos i Buffets
    //buffets[i]._meal[j]

    // Loop que passa por todos os buffets
    for (int i = 0; i < globals_get_buffet_number(); i++) {

        printf("\nO chef está olhando para o buffet de id %d\n", (globals_get_buffets() + i)->_id);

        // Olhar todas as comidas do buffet atual
        for (int j = 0; j < 5; j++) {
            if ( (globals_get_buffets() + i)->_meal[j] <= 0 ) {
                (globals_get_buffets() + i)->_meal[j] = 40;
            }
        }

    }
}

/* --------------------------------------------------------- */
/* ATENÇÃO: Não será necessário modificar as funções abaixo! */
/* --------------------------------------------------------- */

void chef_init(chef_t *self)
{
    printf("\n-------------------CHEF_INIT FUNCIONANDO-------------------\n");
    pthread_create(&self->thread, NULL, chef_run, NULL);
}

void chef_finalize(chef_t *self)
{
    pthread_join(self->thread, NULL);
    free(self);
}