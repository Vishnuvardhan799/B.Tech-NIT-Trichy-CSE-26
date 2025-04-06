%{
	#include <stdio.h>
	#include <stdlib.h>
	int res;
%}

%token id num

%%
stmt:expr{res=$$;};
expr:expr '+' expr {$$=$1+$3;}
	|expr '-' expr {$$=$1-$3;}
	|expr '*' expr {$$=$1*$3;}
	|expr '/' expr {$$=$1/$3;}
	|expr '<' expr {$$=($1<$3);}
	|expr '>' expr {$$=($1>$3);}
	|expr '<' '=' expr {$$=($1<=$4);}
	|expr '>' '=' expr {$$=($1>=$4);}
	|expr '=' '=' expr {$$=($1==$4);}
	|'(' expr ')'{$$=$2;}
	|id
	|num
	;
%%

int main()
{
	printf("Enter an expression : ");
	yyparse();
	printf("\nThe result is : %d",res);
	return 0;
}

int yyerror()
{
	printf("Error!");
	exit(0);
}