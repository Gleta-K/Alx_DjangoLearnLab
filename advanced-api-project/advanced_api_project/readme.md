## Advanced Query Features

The Book API supports filtering, searching, and ordering.

### Filtering
- title
- author
- publication_year

Example:
GET /api/books/?author=George Orwell

### Searching
Search is enabled on:
- title
- author

Example:
GET /api/books/?search=animal

### Ordering
Ordering is supported on:
- title
- publication_year

Example:
GET /api/books/?ordering=-publication_year
