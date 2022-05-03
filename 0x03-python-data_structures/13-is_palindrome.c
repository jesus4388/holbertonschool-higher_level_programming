#include "lists.h"
#include <stddef.h>
#include <stdio.h>
/**
 * is_palindrome - is_palindrome
 * @head: pointer
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int i = 0, j = 0;
	int copy[5000];

	if(*head == NULL || (*head)->next == NULL)
		return(1);
	while(aux)
	{
		copy[i] = aux->n;
		aux = aux->next;
		i++;
	}
	i--;
	for (j = 0; j < i; j++, i--)
	{
		if (copy[i] != copy[j])
			return (0);
	}
	return (1);
}
