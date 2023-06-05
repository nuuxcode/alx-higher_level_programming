#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && list)
	{
		if (!fast)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
