#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a node
 * @head: head
 * @number: number to insert
 * Return: node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (*head == NULL)
	{
		*head = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	current = *head;
	while (current != NULL)
	{
		if (number <= current->n)
		{
			newNode->next = current;
			*head = newNode;
			return (newNode);
		}
		if ((number >= current->n) && (current->next == NULL))
		{
			newNode->next = NULL;
			current->next = newNode;
			return (newNode);
		}
		if ((number >= current->n) && (number <= current->next->n))
		{
			newNode->next = current->next;
			current->next = newNode;
			return (newNode);
		}
		current = current->next;
	}
	return (NULL);
}
