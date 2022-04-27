#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *aux = *head;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	while(aux->next->n < number)
		aux = aux->next;
	if(aux->n > new->n)
	{
		new->next = *head;
		*head = new;
		return(new);
	}
	new->next = aux->next;
	aux->next = new;
	return(new);
}
