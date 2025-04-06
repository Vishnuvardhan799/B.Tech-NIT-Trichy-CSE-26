#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent an entry in the symbol table
typedef struct {
    char name[50];
    char datatype[20];
    int offset;
    int size;
    int scope;
} SymbolEntry;

// Maximum number of entries in the symbol table
#define MAX_ENTRIES 100

// Array to store the symbol table entries
SymbolEntry symbolTable[MAX_ENTRIES];

// Current index in the symbol table
int currentIdx = 0;

// Function to add an entry to the symbol table
void addToSymbolTable(char* name, char* datatype, int size, int scope) {
    if (currentIdx < MAX_ENTRIES) {
        strcpy(symbolTable[currentIdx].name, name);
        strcpy(symbolTable[currentIdx].datatype, datatype);
        symbolTable[currentIdx].size = size;
        symbolTable[currentIdx].scope = scope;
        symbolTable[currentIdx].offset = currentIdx * size; // Assuming each entry has a fixed size
        currentIdx++;
    } else {
        fprintf(stderr, "Symbol table is full.\n");
        exit(1);
    }
}

// Function to print the symbol table
void printSymbolTable() {
    printf("Symbol Table:\n");
    printf("%-20s %-20s %-10s %-10s %-10s\n", "Name", "Data Type", "Offset", "Size", "Scope");
    for (int i = 0; i < currentIdx; i++) {
        printf("%-20s %-20s %-10d %-10d %-10d\n", symbolTable[i].name, symbolTable[i].datatype,
               symbolTable[i].offset, symbolTable[i].size, symbolTable[i].scope);
    }
}

int main() {
    // Example usage of the symbol table
    addToSymbolTable("variable1", "int", sizeof(int), 1);
    addToSymbolTable("variable2", "float", sizeof(float), 1);
    addToSymbolTable("array1", "char", sizeof(char) * 10, 1);
    addToSymbolTable("variable3", "double", sizeof(double), 1);

    // Print the symbol table
    printSymbolTable();

    return 0;
}