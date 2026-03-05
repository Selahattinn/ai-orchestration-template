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
	"context"
	"go.uber.org/zap"
	"github.com/acme/project/internal/user/models"
)
```

Issue:
- Order does not follow stdlib -> third-party -> internal grouping.

## Logging Misuse

```go
fmt.Println("user created", req.Email)
logger.Debugw("payment failed", "error", err)
```

Issue:
- `fmt.Println` is used for operational logging.
- Sensitive data is logged raw.
- Failure case is logged at `Debugw` instead of `Errorw`.
