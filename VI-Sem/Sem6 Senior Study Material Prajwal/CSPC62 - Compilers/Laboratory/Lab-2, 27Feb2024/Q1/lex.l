%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "yacc.tab.h"
	extern int yylval;
%}

%%
[a-zA-Z][a-zA-Z0-9]* {return id;}
[0-9]+ {yylval=atoi(yytext);return num;}
[\t] {;}
[\n] {return 0;}
. {return yytext[0];}
%%