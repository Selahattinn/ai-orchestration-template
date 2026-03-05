# Structure Example: Bad

```text
.
├── cmd/main.go
├── pkg/
│   ├── handler.go
│   ├── service.go
│   ├── repository.go
│   └── db.go
├── internal/utils.go
└── mocks.go
```

Why bad:
- `cmd` and business logic are mixed.
- `pkg` became a dump for service-specific code.
- `internal` has no package boundaries.
- Mock organization is unclear.
