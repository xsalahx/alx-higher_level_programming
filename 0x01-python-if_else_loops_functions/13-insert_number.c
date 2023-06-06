#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev = *head;
	listint_t *next = NULL;

	new = (listint_t *) malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (prev == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (prev->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (prev->next != NULL)
	{
		next = prev->next;
		if (next == NULL)
		{
			prev->next = new;
			new->next = NULL;
		}
		if (next->n > number)
		{
			prev->next = new;
			new->next = next;
			return (new);
		}
		prev = next;
	}
	return (NULL);

}
