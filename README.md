# Chapter 3  — Initial API Contract

## Resources
- **User**: `id`, `name`, `email`
- **Task**: `id`, `title`, `description`, `status`, `userId`, `createdAt`

Allowed task statuses: `TODO`, `IN_PROGRESS`, `DONE`.

## Base URL
`/api/v1`

## Endpoint summary

### Users
| Method | Endpoint | Purpose | Success status |
|---|---|---|---|
| GET | `/users` | List users | 200 OK |
| POST | `/users` | Create a user | 201 Created |
| GET | `/users/{userId}` | Get one user | 200 OK |
| PUT | `/users/{userId}` | Replace/update a user | 200 OK |
| DELETE | `/users/{userId}` | Delete a user | 204 No Content |

### Tasks
| Method | Endpoint | Purpose | Success status |
|---|---|---|---|
| GET | `/tasks` | List tasks; optional `userId` and `status` filters | 200 OK |
| POST | `/tasks` | Create a task | 201 Created |
| GET | `/tasks/{taskId}` | Get one task | 200 OK |
| PUT | `/tasks/{taskId}` | Replace/update a task | 200 OK |
| PATCH | `/tasks/{taskId}/status` | Change task status | 200 OK |
| DELETE | `/tasks/{taskId}` | Delete a task | 204 No Content |

## Common status codes
- `200 OK`: request completed successfully.
- `201 Created`: a new resource was created.
- `204 No Content`: deletion succeeded; response has no body.
- `400 Bad Request`: invalid input or validation error.
- `404 Not Found`: requested user/task does not exist.
- `409 Conflict`: duplicate email or another resource conflict.
- `500 Internal Server Error`: unexpected server-side error.

## Error response example
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request data is invalid."
  }
}
```
