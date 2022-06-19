#include <stdlib.h>

#include "worker_gate.h"
#include "globals.h"
#include "config.h"

student_t* proximo;  // Variável que guarda o estudante que irá passar a catraca

//vai agir como um bool
int catraca = 1;

void worker_gate_look_queue()
{
    /* Insira aqui sua lógica */
    
    // * Segura a thread enquanto não houver espaço nos buffets?

    //buffets_ref

    while (catraca == TRUE) {

    }
    
    printf("\nRestam %d estudantes na fila\n", globals_get_students());
    
    

}

void worker_gate_remove_student()
{
    /* Insira aqui sua lógica */
        proximo = queue_remove(globals_get_queue());     // Remove estudante da fila
        printf("AAAAAAAAAAAAAAAA");
}

void worker_gate_look_buffet()
{
    /* Insira aqui sua lógica */
    // * Observa se existem buffets com espaços livres


}

void *worker_gate_run(void *arg)
{
    printf("\n-------------------WORKER_GATE_RUN FUNCIONANDO-------------------\n");
    
    int all_students_entered;
    int number_students;


    number_students = *((int *)arg);
    all_students_entered = number_students > 0 ? FALSE : TRUE;

    while (all_students_entered == FALSE)
    {
        worker_gate_look_queue(); // * Pega id estudante
        worker_gate_look_buffet(); // * Observa pra qual buffet mandar
        worker_gate_remove_student();
        msleep(5000); /* Pode retirar este sleep quando implementar a solução! */
    }

    pthread_exit(NULL);
}

void worker_gate_init(worker_gate_t *self)
{
    printf("\n-------------------WORKER_GATE_INIT FUNCIONANDO-------------------\n");
    int number_students = globals_get_students();
    pthread_create(&self->thread, NULL, worker_gate_run, &number_students);
}

void worker_gate_finalize(worker_gate_t *self)
{
    pthread_join(self->thread, NULL);
    free(self);
}

void worker_gate_insert_queue_buffet(student_t *student)
{
    /* Insira aqui sua lógica */
    // * Verificar fila livre e mandar o primeiro da fila externa
    // buffet_queue_insert(buffet_t *self, student_t *student)
}