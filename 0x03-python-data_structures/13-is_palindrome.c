#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head;
	int l = 0;
	int i;
	int j;

	while (last != NULL)
	{
		last = last->next;
		l++;
	}

	for (i = 0; i < l / 2; i++)
	{
		last = *head;
		for(j = 0; j < l - 2 * i - 1; j++)
			last = last->next;
		if (last->n != (*head)->n)
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
