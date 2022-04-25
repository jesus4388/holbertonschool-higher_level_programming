#include "lists.h"
#include <stddef.h>
/**
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;
	listint_t *aux2 = list;

	while(aux2 != NULL)
	{
		aux = aux->next;
		aux2 = aux->next->next;
		if (aux == aux2)
			break;
		if (aux2 == NULL)
			break;
	}
	if (aux == aux2)
		return(1);
	else
		return(0);
}
