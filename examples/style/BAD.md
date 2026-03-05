# Style Examples: Bad

## Missing Interface Boundary

```go
type Handler struct {}

func NewHandler() *Handler {
	return &Handler{}
}
```

Issue:
- Constructor returns concrete type, violating preferred interface-first style.

## Missing Context Parameter

```go
func (h *handler) CreateUser(req CreateUserRequest) error {
	return nil
}
```

Issue:
- `ctx context.Context` is missing.

## Import Grouping Violation

```go
import (
	"github.com/sirupsen/logrus"
	"context"
	"github.com/acme/project/internal/user/models"
)
```

Issue:
- Order does not follow stdlib -> third-party -> internal grouping.
