#include "lists.h"
#include <stddef.h>
/**
 * check_cycle - check_cycle
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux2 = list;

	if (list && aux)
	{
		while (aux2)
		{
			aux = aux->next;
			aux2 = aux2->next->next;
			if (aux == aux2)
				return (1);
		}
	}
	return (0);
}
