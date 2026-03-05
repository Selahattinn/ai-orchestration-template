# Naming Example: Bad

```go
package utils

type H interface {
	Do(c context.Context, d Req) error
}

type HandlerImpl struct{}

func New() H {
	return &HandlerImpl{}
}
```

Why bad:
- Package name is too generic.
- Interface and method names are ambiguous (`H`, `Do`).
- Constructor and concrete type naming are inconsistent with preferred pattern.
