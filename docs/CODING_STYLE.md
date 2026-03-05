# Coding Style Profile

Personal coding profile for Go code generation and review.

## 1) Handler and Interface Pattern

Prefer interface-first construction with private implementation structs.

```go
// Handler defines service behavior.
type Handler interface {
	// TODO: method signatures
}

type handler struct {
	// deps
}

// NewHandler constructs a Handler implementation.
func NewHandler() Handler {
	return &handler{}
}
```

Rules:
- Public constructor returns interface where practical.
- Concrete implementation stays unexported unless required.
- Keep constructor signatures explicit and dependency-driven.

## 2) Context-First Function Signatures

`ctx context.Context` must exist in every function that can touch I/O, remote systems, DB, queues, or long-running operations.

```go
// CreateUser creates a user with timeout/cancel support.
func (h *handler) CreateUser(ctx context.Context, req CreateUserRequest) error {
	// ...
	return nil
}
```

Rules:
- `ctx` is the first parameter after receiver.
- Do not create background contexts inside business logic.
- Propagate `ctx` through all downstream calls.

## 3) Test Strategy Preference (TDD)

Default workflow is red -> green -> refactor.

Rules:
- Start with failing tests that represent expected behavior.
- Implement minimum code to pass.
- Refactor only after green.
- Keep one behavior per test focus.

## 4) Commenting Style

Prefer function-level comments for intent. Inline comments only for complex local breakpoints.

Rules:
- Every exported function should have a top comment.
- Non-exported function comments are recommended when intent is non-obvious.
- Inline comments must explain why, not what.

## 5) Import Ordering

Use three import groups in this exact order:
1. Standard library
2. Third-party packages
3. Internal project packages

```go
import (
	"fmt"
	"os/exec"
	"time"

	gwda "github.com/livetesting-company/live-testing-ios-go-wda-lib"
	"go.uber.org/zap"

	"github.com/device-park/device-park-ios-health-service/internal/device/models"
)
```

## 6) Error Model: ErrorBag

Use the custom `ErrorBag` pattern for app-level errors.

```go
type ErrorBag struct {
	Code       int    `json:"code"`
	Cause      error  `json:"cause"`
	Message    string `json:"message"`
	HTTPStatus int    `json:"status"`
}

func (e *ErrorBag) Error() string {
	if e == nil {
		return "<nil>"
	}
	if e.Cause != nil {
		return e.Cause.Error()
	}
	return "unknown error"
}

func (e *ErrorBag) Unwrap() error {
	if e == nil {
		return nil
	}
	return e.Cause
}

func (e *ErrorBag) GetCode() int {
	if e == nil {
		return 0
	}
	return e.Code
}

func (e *ErrorBag) GetCause() error {
	if e == nil {
		return nil
	}
	return e.Cause
}

func (e *ErrorBag) GetMessage() string {
	if e == nil {
		return ""
	}
	return e.Message
}

func (e *ErrorBag) GetHTTPStatus() int {
	if e == nil || e.HTTPStatus == 0 {
		return fiber.StatusInternalServerError
	}
	return e.HTTPStatus
}

func NewErrorBag(code int, msg string, status int, cause error) *ErrorBag {
	return &ErrorBag{Code: code, Message: msg, HTTPStatus: status, Cause: cause}
}
```

Rules:
- Wrap lower-level errors into `ErrorBag` at domain boundaries.
- Preserve original cause in `Cause`.
- Keep `Code` stable and documented.
- Ensure HTTP mapping is explicit.
- Framework-specific defaults (for example Fiber status constants) are allowed.

## 7) Style Enforcement Priority

When style conflicts with generic suggestions, this profile wins unless project constraints explicitly override it.

## 8) Logging Preference (zap SugaredLogger)

Use `zap.SugaredLogger` as the default logger API for business/application layers.

```go
// NewHandler creates a user handler.
func NewHandler(repo Repository, logger *zap.SugaredLogger) Handler {
	return &handler{repo: repo, logger: logger}
}
```

Level rules:
- `Debugw`: verbose diagnostics and temporary deep troubleshooting.
- `Infow`: state transitions, successful operations, lifecycle events.
- `Warnw`: recoverable anomalies, retries, degraded paths.
- `Errorw`: failed operations and user-impacting or system-impacting errors.

Rules:
- Prefer structured logging (`Infow/Warnw/Errorw`) over formatted strings.
- Include stable keys such as `request_id`, `operation`, and `error_code` where available.
- Do not log secrets or raw sensitive data.
- Keep one event per meaningful state transition.

## 9) Package and File Hierarchy

Follow `docs/FILE_HIERARCHY.md` for project layout decisions.

Rules:
- Keep startup/bootstrap in `cmd/`.
- Keep service-specific business code in `internal/`.
- Put only proven reusable libraries in `pkg/`.
- Keep test doubles in `mocks/` with predictable naming.

## 10) Naming Conventions

Follow `docs/NAMING_STANDARD.md` for naming decisions.

Rules:
- Use explicit domain names for packages, types, and methods.
- Prefer verb-first method names for actions.
- Avoid generic package names like `utils` and `common`.
- Keep file names responsibility-driven and predictable.
