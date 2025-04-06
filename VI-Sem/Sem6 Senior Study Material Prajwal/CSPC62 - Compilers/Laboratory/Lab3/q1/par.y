%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern int yyparse();
extern FILE* yyin;
void yyerror(const char*);

#define YYSTYPE YYSTYPE
#define YYDEBUG 1

typedef struct {
    char* str;
} YYSTYPE;

%}

%token IF LPAREN RPAREN ELSE ID

%%
program : program statement;

statement : if_statement
        | ID
        ;

if_statement : IF LPAREN ID RPAREN statement 
        | IF LPAREN ID RPAREN statement ELSE statement
        ;


%%

void yyerror(const char *s) {
    printf("Error!\n");
    exit(0);
}

int main() {
    FILE* input_file = fopen("sample.c", "r");
    yyin = input_file;
    yyparse();
    printf("success\n");
    fclose(input_file);
    return 0;
}
