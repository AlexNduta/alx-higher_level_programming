#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it or not.
 * @list: pointer to the beginning of our node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *to_check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	to_check = current->next;

	while (current != NULL && to_check->next != NULL
		&& to_check->next->next != NULL)
	{
		if (current == to_check)
			return (1);
		current = current->next;
		to_check = to_check->next->next;
	}
	return (0);
}
