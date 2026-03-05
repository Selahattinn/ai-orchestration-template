# Structure Example: Good

```text
.
├── cmd/
│   └── billing-api/
│       └── main.go
├── internal/
│   ├── app/bootstrap/
│   ├── domain/invoice/
│   ├── service/invoice/
│   ├── repository/invoice/
│   ├── transport/http/invoice/
│   ├── platform/postgres/
│   ├── config/
│   ├── errors/
│   └── observability/
├── pkg/uuidx/
├── mocks/repository/
└── testdata/
```

Why good:
- Startup code stays in `cmd`.
- Business code is in bounded `internal` packages.
- Reusable utility is isolated in `pkg`.
- Mocks are explicit and test-focused.
