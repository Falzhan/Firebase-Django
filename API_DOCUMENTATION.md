# Django REST API Documentation

This Django project now includes a complete REST API for managing blog posts.

## API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/
```

### Available Endpoints

1. **List all posts**
   - `GET /api/posts/`
   - Returns all blog posts with pagination

2. **Create a new post**
   - `POST /api/posts/`
   - Creates a new blog post
   - Required fields: `title`, `content`
   - Example request body:
     ```json
     {
       "title": "My First Post",
       "content": "This is the content of my first post"
     }
     ```

3. **Get post details**
   - `GET /api/posts/{id}/`
   - Returns detailed information about a specific post

4. **Update a post**
   - `PUT /api/posts/{id}/` (full update)
   - `PATCH /api/posts/{id}/` (partial update)
   - Updates an existing blog post
   - Example request body:
     ```json
     {
       "title": "Updated Title",
       "content": "Updated content"
     }
     ```

5. **Delete a post**
   - `DELETE /api/posts/{id}/`
   - Deletes a specific blog post
   - Returns 204 No Content on successful deletion

### Alternative Custom Endpoints

For more granular control, you can also use these custom endpoints:

1. `GET /api/posts/` - List all posts
2. `POST /api/posts/create/` - Create a new post
3. `GET /api/posts/{id}/detail/` - Get post details
4. `PUT /api/posts/{id}/update/` or `PATCH /api/posts/{id}/update/` - Update a post
5. `DELETE /api/posts/{id}/delete/` - Delete a post

## Testing the API

### Using curl

1. **Create a post:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/posts/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Test Post", "content": "This is a test post"}'
   ```

2. **Get all posts:**
   ```bash
   curl http://127.0.0.1:8000/api/posts/
   ```

3. **Get a specific post:**
   ```bash
   curl http://127.0.0.1:8000/api/posts/1/
   ```

4. **Update a post:**
   ```bash
   curl -X PATCH http://127.0.0.1:8000/api/posts/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title"}'
   ```

5. **Delete a post:**
   ```bash
   curl -X DELETE http://127.0.0.1:8000/api/posts/1/
   ```

### Using Postman

1. Set the base URL to `http://127.0.0.1:8000/api/`
2. Use the appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE)
3. Set the `Content-Type` header to `application/json` for POST/PUT/PATCH requests
4. Include JSON data in the request body for POST/PUT/PATCH requests

### Using the Django REST Framework Browsable API

1. Start the development server: `python manage.py runserver`
2. Navigate to `http://127.0.0.1:8000/api/` in your browser
3. Use the browsable API interface to test all endpoints interactively

## API Response Format

### Success Responses

- **200 OK** - Successful GET requests
- **201 Created** - Successful POST requests (creation)
- **204 No Content** - Successful DELETE requests
- **200 OK** - Successful PUT/PATCH requests (updates)

### Error Responses

- **400 Bad Request** - Invalid data
- **404 Not Found** - Resource not found
- **405 Method Not Allowed** - Invalid HTTP method

### Example Success Response (GET /api/posts/)

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "My First Post",
      "content": "This is the content of my first post",
      "created_at": "2024-01-01T12:00:00Z",
      "updated_at": "2024-01-01T12:00:00Z"
    }
  ]
}
```

### Example Success Response (POST /api/posts/)

```json
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

## Data Model

The API works with the `Post` model which has the following fields:

- `id` - Integer (Primary key, read-only)
- `title` - String (max 50 characters, required)
- `content` - Text (required)
- `created_at` - DateTime (read-only, auto-generated)
- `updated_at` - DateTime (read-only, auto-generated)

## Authentication

Currently, the API is public and doesn't require authentication. For production use, you would want to add authentication (e.g., Token Authentication, JWT, etc.).