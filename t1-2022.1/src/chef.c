#include <stdlib.h>

#include "chef.h"
#include "config.h"

void *chef_run()
{
    /* Insira sua lógica aqui */
    // A cada aluno que se serve no buffet verifica se têm alguma bacia vazia

    printf("\n-------------------CHEF_RUN FUNCIONANDO-------------------\n");

    while (TRUE)
    {
        //if chef_check_food(){
        //    chef_put_food();
        //}
        
        msleep(5000); /* Pode retirar este sleep quando implementar a solução! */
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