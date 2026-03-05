# Naming Example: Good

```go
package service

// Handler defines user service behavior.
type Handler interface {
	CreateUser(ctx context.Context, req CreateUserRequest) error
	GetUserByID(ctx context.Context, userID string) (User, error)
}

type handler struct {
	repo UserRepository
}

// NewHandler creates a user handler.
func NewHandler(repo UserRepository) Handler {
	return &handler{repo: repo}
}
```

Why good:
- Interface/type/function names are explicit and consistent.
- Method names are verb-first and domain-specific.
- Variable names (`ctx`, `req`, `userID`) are predictable.
