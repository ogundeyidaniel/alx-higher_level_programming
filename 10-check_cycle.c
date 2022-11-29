#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - pointer to start of linked list
 * @Return: 0 if false, 1 if true
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);
	while (tort && hare && hare->next)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
			return (1);
	}
	return (0);
}
