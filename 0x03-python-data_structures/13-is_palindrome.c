#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head node of the linked list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *palin = *head;
	int counter = 0, i = 0, j = 0;

	if (!*head)
		return (1);

	while (current)
	{
		current = current->next;
		counter++;
	}

	current = *head;
	for (i = 1; i <= counter; i++)
	{
		for (j = i; j <= counter - i; j++)
			palin = palin->next;

		if (current->n != palin->n)
			return (0);

		current = current->next;
		palin = current;
	}

	return (1);
}

