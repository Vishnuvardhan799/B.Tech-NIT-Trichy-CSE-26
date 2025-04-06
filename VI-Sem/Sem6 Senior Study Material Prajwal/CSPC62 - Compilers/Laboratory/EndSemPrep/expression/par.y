%{
    #include <stdio.h>
    #include <stdlib.h>
    int res;
%}

%token ID NUM

%%
    stmt: expr{res=$$;};
    expr:   expr '+' expr {$$=$1+$3;}
        |   expr '-' expr {$$=$1-$3;}
        |   expr '*' expr {$$=$1*$3;}
        |   expr '/' expr {$$=$1/$3;}
        |   expr '<' expr {$$=$1<$3;}
        |   expr '>' expr {$$=$1>$3;}
        |   expr '<' '=' expr {$$=($1<=$4);}
        |   expr '>' '=' expr {$$=($1>=$4);}
        |   expr '=' '=' expr {$$=($1==$4);}
        |   ID | NUM;
%%

int yyerror()
{
    printf("Error!");
    exit(0);
}

int main()
{
    printf("Enter an expression : ");
    yyparse();
    printf("\nThe result is %d.", res);
    return 0;
}