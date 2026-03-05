# Style Examples: Good

## Interface + Constructor Pattern

```go
// Handler defines user service behavior.
type Handler interface {
	CreateUser(ctx context.Context, req CreateUserRequest) error
}

type handler struct {
	repo Repository
}

// NewHandler creates a user handler.
func NewHandler(repo Repository) Handler {
	return &handler{repo: repo}
}
```

## Import Grouping

```go
import (
	"context"
	"fmt"

	"github.com/sirupsen/logrus"

	"github.com/acme/project/internal/user/models"
)
```

## Function Comment + ctx

```go
// CreateUser validates input and persists a new user.
func (h *handler) CreateUser(ctx context.Context, req CreateUserRequest) error {
	return nil
}
```
