#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char infix[255] = "";

typedef struct _STACKS
{
    char op;
    struct _STACKS *next;
} STACKS;

void show(STACKS *topo);
void read(STACKS **stack, STACKS **op_stack);
void stackup(STACKS **pilha, STACKS *aux, char op);
void transfer(STACKS **stack, STACKS **op_stack, STACKS *aux);

char convert()
{
    STACKS *stack = NULL;
    STACKS *op_stack = NULL;

    printf("\nInfixa: ");
    read(&stack, &op_stack);
    printf("\n\nPos-fixa: ");
    show(stack);
    return *infix;
}

void transfer(STACKS **stack, STACKS **op_stack, STACKS *aux)
{
    aux = (*op_stack)->next;
    (*op_stack)->next = *stack;
    *stack = *op_stack;
    *op_stack = aux;
}

void stackup(STACKS **pilha, STACKS *aux, char op)
{
    aux = (STACKS *)malloc(sizeof(STACKS));
    aux->op = op;
    aux->next = *pilha;
    *pilha = aux;
    show(aux);
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

            stackup(&(*op_stack), aux, op);

            break;

        case '*':
        case '/':

            while ((*op_stack) && ((*op_stack)->op != '+' && (*op_stack)->op != '-' && (*op_stack)->op != '('))
            {
                transfer(&(*stack), &(*op_stack), aux);
            }

            stackup(&(*op_stack), aux, op);

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
            stackup(&(*op_stack), aux, op);

            break;

        default:
            stackup(&(*stack), aux, op);

            break;
        }

        scanf("%c", &op);
    }

    while (*op_stack)
    {
        transfer(&(*stack), &(*op_stack), aux);
    }
}

void show(STACKS *topo)
{
    if (topo)
    {
        show(topo->next);
        printf("%c ", topo->op);
    }
    else
    {
        printf("\n");
    }
}
