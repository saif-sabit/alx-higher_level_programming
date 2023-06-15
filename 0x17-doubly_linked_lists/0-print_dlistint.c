#include "lists.h"
/**
 * print_dlistint - prints list contents
 * @h: pointer to a doubbly list
 * Return: size of printed list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}
	return(i);
}

