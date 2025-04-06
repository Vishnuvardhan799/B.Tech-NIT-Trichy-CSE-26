%{
    #include <stdio.h>
    #include <stdlib.h>

    extern int yylex();
    extern int yyparse();
    extern FILE * yyin;

    void yyerror(const char *);
    #define YYSTYPE YYSTYPE
    #define YYDEBUG 1

    typedef struct {
        char * str;
    } YYSTYPE;
%}

%token WHILE LPAREN RPAREN ID

%%
    program: statement;
    statement: WHILE LPAREN ID RPAREN statement | ID;
%%

void yyerror(const char * s)
{
    printf("Error!\n");
    exit(0);
}

int main()
{
    FILE * input_file = fopen("sample.c", "r");
    yyin = input_file;
    yyparse();
    printf("Success!\n");
    fclose(input_file);
    return 0;
}