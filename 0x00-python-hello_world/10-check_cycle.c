#include "lists.h"
#include <stddef.h>
/**
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux2 = list;

	while(aux2)
	{
		aux = aux->next;
		aux2 = aux2->next->next;
		if (aux == aux2)
			return(1);
	}
	return(0);
}
