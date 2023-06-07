#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head)
		*head = new;
	else if (current->n >= number)
	{
		*head = new;
		new->next = current;
	}
	else if (current->next)
	{
		while (current->next)
		{
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			if (!current->next->next)
				break;
			current = current->next;
		}
		current->next->next = new;
	}
	else
		current->next = new;
	return (new);
}
