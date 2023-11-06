#include "lists.h"

/**
 * is_palindrome - function check if a singly linked list is a palindrome.
 * @head: pointer to ptr of first node
 * Return: (0)
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - function to know if is paldeo.
 * @head: head of list
 * @end: last of list
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
