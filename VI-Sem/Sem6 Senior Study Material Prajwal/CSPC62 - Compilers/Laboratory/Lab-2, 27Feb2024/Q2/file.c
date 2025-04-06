#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    char name[50];     
    char datatype[20];  
    int offset;       
    int size;           
    char scope[20];     
} SymbolEntry;
typedef struct {
    SymbolEntry entries[100]; 
    int count;                 
} SymbolTable;
void initSymbolTable(SymbolTable *table) {
    table->count = 0;
}
void addEntry(SymbolTable *table, const char *name, const char *datatype, int offset, int size, const char *scope) {
    if (table->count < 100) {
        SymbolEntry *entry = &(table->entries[table->count]);
        strcpy(entry->name, name);
        strcpy(entry->datatype, datatype);
        entry->offset = offset;
        entry->size = size;
        strcpy(entry->scope, scope);
        table->count++;
    } else {
        printf("Symbol table full, cannot add entry.\n");
    }
}
void displaySymbolTable(const SymbolTable *table) {
    printf("Name\tDataType\tOffset\tSize\tScope\n");
    printf("---------------------------------------------\n");
    for (int i = 0; i < table->count; i++) {
        SymbolEntry entry = table->entries[i];
        printf("%s\t%s\t\t%d\t%d\t%s\n", entry.name, entry.datatype, entry.offset, entry.size, entry.scope);
    }
}
int main() {
    SymbolTable symbolTable;
    initSymbolTable(&symbolTable);
    addEntry(&symbolTable, "x", "long", 4, sizeof(long), "global");
    addEntry(&symbolTable, "y", "long long", 8, sizeof(long long), "local");
    displaySymbolTable(&symbolTable);
    return 0;
}