%option noyywrap

%{
#include <stdio.h>
#include "par.tab.h"
%}

%%
[ \t]	; // ignore all whitespace
[0-9]+\.[0-9]+ 	{yylval.fval = atof(yytext); return T_FLOAT;}
[0-9]+		{yylval.ival = atoi(yytext); return T_INT;}
\n		{return T_NEWLINE;}
"+"		{return T_PLUS;}
"-"		{return T_MINUS;}
"*"		{return T_MULTIPLY;}
"/"		{return T_DIVIDE;}
"("		{return T_LEFT;}
")"		{return T_RIGHT;}
">"      {return T_GT;}
"<"      {return T_LT;}
"=="     {return T_EQ;}
"&&"     {return T_AND;}
"||"     {return T_OR;}
"exit"		{return T_QUIT;}
"quit"		{return T_QUIT;}
%%