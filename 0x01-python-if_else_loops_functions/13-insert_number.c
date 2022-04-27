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
	if (new == NULL)
		return(NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return(new);
	}
	while(aux->next->n < number && aux->next != NULL)
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
