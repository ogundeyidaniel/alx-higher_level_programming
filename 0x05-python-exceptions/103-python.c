#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - Print some basic info about Python lists
 * @p: Pointer
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyTypeObject *type;
	PyObject *item;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	int i, size, alloc;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	if (p && p->ob_type == &PyList_Type)
	{
		for (i = 0; i < size; i++)
		{
			item = list->ob_item[i];
			type = item->ob_type;
			printf("Element %d: %s\n", i, type->tp_name);
			if (item->ob_type == &PyBytes_Type)
				print_python_bytes(item);
			else if (item->ob_type == &PyFloat_Type)
				print_python_float(item);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes -  print some basic info about Python bytes objects
 * @p: Pointer
 *
 * Return: the address of the new node, or NULL if it failed
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	unsigned int i;
	unsigned long size;
	char *string;

	printf("[.] bytes object info\n");
	if (!p || p->ob_type != &PyBytes_Type)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = var->ob_size;
	string = byte->ob_sval;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", string);
	size =  size + 1 > 10 ? 10 : size + 1;
	printf("  first %lu bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02hhx%s", string[i], i + 1 < size ? " " : "");
	printf("\n");
}
/**
 * print_python_float -  print some basic info about Python bytes objects
 * @p: Pointer
 *
 * Return: the address of the new node, or NULL if it failed
 */
void print_python_float(PyObject *p)
{
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!p || p->ob_type != &PyFloat_Type)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f  = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
	PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
