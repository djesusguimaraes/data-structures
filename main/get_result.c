#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "get_result.h"

typedef struct NO
{
	double value;
	struct NO *next;
} NO;

typedef struct STACKS
{
	struct NO *top;
} STACKS;

void startStack(STACKS *stack)
{
	stack->top = NULL;
}

void stack_up(STACKS *stack, double value)
{
	NO *new_no = (NO *)malloc(sizeof(NO));

	if (new_no != NULL)
	{
		new_no->value = value;
		new_no->next = stack->top;
		stack->top = new_no;
	}
	else
	{
		return;
	}
}

double unstack(STACKS *stack)
{
	NO *last = stack->top;
	if (last != NULL)
	{
		stack->top = last->next;
		last->next = NULL;
		double value = last->value;
		free(last);
		return value;
	}
	else
	{
		return 0.0;
	}
}

double operation(double left, char op, double right)
{
	switch (op)
	{
	case '+':
		printf("\n\t-> %.2lf + %.2lf\n", left, right);
		return left + right;
	case '-':
		if (right > left && right > 0)
		{
			printf("\n\t-> %.2lf - %.2lf\n", right, left);
			return right - left;
		}
		printf("\n\t-> %.2lf - %.2lf\n", left, right);
		return left - right;
	case '*':
		printf("\n\t-> %.2lf * %.2lf\n", left, right);
		return left * right;
	case '/':
		printf("\n\t-> %.2lf / %.2lf\n", right, left);
		return right / left;
	default:
		return 0.0;
	}
}

void showing(NO *topo)
{
	if (topo)
	{
		char output[255];
		showing(topo->next);
		snprintf(output, 255, "%.2lf", topo->value);
		printf("%s ", output);
	}
	else
	{
		printf("\n");
	}
}

void resolve_notation(char expression[])
{
	double left, right, result;
	char *players;
	STACKS *stack = (STACKS *)malloc(sizeof(STACKS));
	if (stack != NULL)
	{
		players = strtok(expression, " ");
		startStack(stack);
		while (players)
		{
			if (players[0] == '+' || players[0] == '-' || players[0] == '*' || players[0] == '/')
			{
				left = unstack(stack);
				right = unstack(stack);
				result = operation(left, players[0], right);
				stack_up(stack, result);
			}
			else
			{
				result = strtol(players, NULL, 10);
				stack_up(stack, result);
			}
			showing(stack->top);
			players = strtok(NULL, " ");
		}
		left = unstack(stack);
	}
}
