#include <stdlib.h>

#include "worker_gate.h"
#include "globals.h"
#include "config.h"

student_t* proximo;  // Variável que guarda o estudante que irá passar a catraca

void worker_gate_look_queue()
{
    globals_set_all_students_entered(globals_get_students() > 0 ? FALSE : TRUE); // Verifica se ainda existem 
                                                                                 // estudantes na fila de entrada
    printf("\nRestam %d estudantes na fila\n", globals_get_students());
}

void worker_gate_remove_student()
{
    /* Insira aqui sua lógica */
        proximo = queue_remove(globals_get_queue());    // Remove estudante da fila
        globals_set_students(globals_get_students() - 1);   // Diminui o número de estudantes na fila
        globals_set_students_inside(globals_get_students_inside() + 1); // Aumenta o número de estudantes dentro do RU
        if (globals_get_students() + 1 > 0) {printf("\nEstudante entrou no RU\n"); }
}

void worker_gate_look_buffet()
{
    /* Insira aqui sua lógica */
    // * Observa se existem buffets com espaços livres
    // * Segura a thread enquanto não houver espaço nos buffets?
    int pode_passar = 0;
    int buffet_livre_index = 0;
    int buffet_livre_lado = 0; // 0 = esquerda e 1 = direita

    // Loop que passa por todos os buffets
    for (int i = 0; i < globals_get_buffet_number(); i++) {
        printf("\nOlhou o buffet de id %d\n", (globals_get_buffets() + i)->_id);
        // passa por todos os buffets do primeiro ao último, da esquerda pra direita, verificando o primeiro que estiver livre
        // caso encontre algum livre, pode_passar fica true e buffet_livre_index e buffet_livre_lado sao atualizados
    }

    if (pode_passar) {
        //worker_gate_insert_queue_buffet
    } else {

    }


}

void *worker_gate_run(void *arg)
{
    printf("\n-------------------WORKER_GATE_RUN FUNCIONANDO-------------------\n");
    
    int all_students_entered = globals_get_all_students_entered();
    int number_students = *((int *)arg);

    printf("all_students_entered = %d\nnumber_students = %d\n", all_students_entered, number_students);

    while (all_students_entered == FALSE)
    {
        printf("worker_gate_run está em loop");
        worker_gate_look_queue(); // * Pega id estudante
        worker_gate_look_buffet(); // * Observa pra qual buffet mandar
        worker_gate_remove_student();
        msleep(5000); /* Pode retirar este sleep quando implementar a solução! */
        all_students_entered = globals_get_all_students_entered();
        number_students = globals_get_students();
        printf("\núltima etapa do loop de worker_gate_run\n");
    }

    printf("worker_gate_run saiu do loop");
    free(proximo);
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