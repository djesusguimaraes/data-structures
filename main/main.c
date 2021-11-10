#include "get_result.h"
#include "fix_exp.h"

void main()
{
	convert();
	char expression[255] = {"5 3 2 + * 4 / 6 -"};
	resolve_notation(expression);
}
