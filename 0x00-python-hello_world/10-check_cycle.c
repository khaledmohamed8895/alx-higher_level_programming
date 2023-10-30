#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: ptr to list check
 * Return: 1 if cyclical ,or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	while (fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}
	return (0);
}
