#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char infix[255] = "";

typedef struct _STACKS
{
    char op;
    struct _STACKS *next;
} STACKS;

void transfer(STACKS **stack, STACKS **op_stack, STACKS *aux)
{
    aux = (*op_stack)->next;
    (*op_stack)->next = *stack;
    *stack = *op_stack;
    *op_stack = aux;
}

void stack_up(STACKS **pilha, STACKS *aux, char op)
{
    aux = (STACKS *)malloc(sizeof(STACKS));
    aux->op = op;
    aux->next = *pilha;
    *pilha = aux;
}

void read(STACKS **stack, STACKS **op_stack)
{
    char op;
    STACKS *aux;

    scanf("%c", &op);
    while (op != '\n')
    {

        switch (op)
        {
        case '+':
        case '-':

            while ((*op_stack) && ((*op_stack)->op != '('))
            {
                transfer(&(*stack), &(*op_stack), aux);
            }

            stack_up(&(*op_stack), aux, op);

            break;

        case '*':
        case '/':

            while ((*op_stack) && ((*op_stack)->op != '+' && (*op_stack)->op != '-' && (*op_stack)->op != '('))
            {
                transfer(&(*stack), &(*op_stack), aux);
            }

            stack_up(&(*op_stack), aux, op);

            break;

        case ')':
            while ((*op_stack) && ((*op_stack)->op != '('))
            {
                transfer(&(*stack), &(*op_stack), aux);
            }

            if ((*op_stack) && (*op_stack)->op == '(')
            {
                aux = *op_stack;
                *op_stack = (*op_stack)->next;
                free(aux);
            }

            break;

        case '(':
            stack_up(&(*op_stack), aux, op);

            break;

        default:
            stack_up(&(*stack), aux, op);

            break;
        }

        scanf("%c", &op);
    }

    while (*op_stack)
    {
        transfer(&(*stack), &(*op_stack), aux);
    }
}

void showing(STACKS *topo)
{
    if (topo)
    {
        showing(topo->next);
        printf("%c ", topo->op);
    }
}

int main()
{
    STACKS *stack = NULL;
    STACKS *op_stack = NULL;

    printf("Operacao Infixa: ");
    read(&stack, &op_stack);
    printf("Operacao Posfixa: ");
    showing(stack);
    printf("%s\n", infix);

    return 0;
}
