#include <stdio.h>
#include "Python.h"
#include "object.h"
#include "listobject.h"
/**
 *print_python_list_info - func to print lst info
 * like list size and allocated memory
 * using cpython
 * !important: requires python3.4 sandbox
 * because this was the task requirements
 *
 *@lst: python list passed to c from .py file
 *using cpython
 */
void print_python_list_info(PyObject *lst)
{int indx;/*Py_ssize_t indx;*/
	PyListObject *tmplst = (PyListObject *)lst;
	Py_ssize_t list_sizevar = tmplst->ob_base.ob_size;
	/*above line do the same as commented line below*/
	/*Py_ssize_t list_sizevar = PyList_Size(lst);*/
	Py_ssize_t allocatedvar = ((PyListObject *)lst)->allocated;
	/*PyObject *elemitem;*/

	printf("[*] Size of the Python List = %zd\n", list_sizevar);
	printf("[*] Allocated = %zd\n", allocatedvar);

	for (indx = 0; indx < list_sizevar; indx++)
	{
		printf("Element %d: ", indx);
		printf("%s\n", tmplst->ob_item[indx]->ob_type->tp_name);
		/*above do lines the same as commented lines below*/
		/*elemitem = PyList_GetItem(lst, indx);*/
		/*printf("Element %zd: %s\n", indx, Py_TYPE(elemitem)->tp_name);*/
	}
}
