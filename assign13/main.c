#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;

StringBuffer *sb_init(size_t initial_capacity) {
    if (initial_capacity == 0) {
        initial_capacity = 10;
    }
    
    StringBuffer *sb = malloc(sizeof(StringBuffer));
    if (sb == NULL) {
        printf("Error: Failed to allocate StringBuffer\n");
        return NULL;
    }
    
    sb->data = malloc(initial_capacity);
    if (sb->data == NULL) {
        printf("Error: Failed to allocate data buffer\n");
        free(sb);
        return NULL;
    }
    
    sb->data[0] = '\0';
    sb->length = 0;
    sb->capacity = initial_capacity;
    
    return sb;
}

void sb_append(StringBuffer *sb, const char *str) {
    if (sb == NULL || str == NULL) {
        return;
    }
    
    size_t str_len = strlen(str);
    size_t needed = sb->length + str_len + 1;  
    
    while (sb->capacity < needed) {
        sb->capacity *= 2;
    }
    
    char *new_data = realloc(sb->data, sb->capacity);
    if (new_data == NULL) {
        printf("Error: realloc failed\n");
        return;
    }
    sb->data = new_data;
    
    strcpy(sb->data + sb->length, str);
    sb->length += str_len;
}

void sb_free(StringBuffer *sb) {
    if (sb == NULL) {
        return;
    }
    
    free(sb->data);
    free(sb);
}

int main() {
    printf("Dynamic String Buffer Demo\n\n");
    
    StringBuffer *sb = sb_init(5);
    if (sb == NULL) {
        printf("Failed to initialize StringBuffer\n");
        return 1;
    }
    
    printf("Initial state:\n");
    printf("  Capacity: %zu\n", sb->capacity);
    printf("  Length: %zu\n\n", sb->length);
    
    printf("Append 1\n");
    printf("Appending: \"Priya Singh\"\n");
    sb_append(sb, "Priya Singh");
    printf("Result: capacity=%zu, length=%zu\n", sb->capacity, sb->length);
    printf("Content: \"%s\"\n\n", sb->data);
    
    printf("Append 2\n");
    printf("Appending: \" World\"\n");
    sb_append(sb, " World");
    printf("Result: capacity=%zu, length=%zu (GROWTH 1)\n", sb->capacity, sb->length);
    printf("Content: \"%s\"\n\n", sb->data);
    
    printf("Append 3\n");
    printf("Appending: \"! This is a longer string to trigger more growth\"\n");
    sb_append(sb, "! This is a longer string to trigger more growth");
    printf("Result: capacity=%zu, length=%zu (GROWTH 2)\n", sb->capacity, sb->length);
    printf("Content: \"%s\"\n\n", sb->data);
    
    sb_free(sb);
    printf("All memory freed successfully\n");
    
    return 0;
}
