#include "lists.h"
/**
 * print_dlistint - this is the name of the function
 * @h: thi is the head of the node
 *
 * Return: all elements o the list present
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t nodes = 0;
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		nodes++;
	}
	return (nodes);
}
