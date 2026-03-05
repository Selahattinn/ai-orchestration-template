# File Hierarchy Standard

Canonical Go project layout policy for this template.

## Target Structure

```text
.
├── cmd/
│   └── <service-name>/
│       └── main.go
├── internal/
│   ├── app/
│   ├── domain/
│   ├── service/
│   ├── repository/
│   ├── transport/
│   │   └── http/
│   ├── platform/
│   ├── config/
│   ├── errors/
│   └── observability/
├── pkg/
│   └── <reusable-library>/
├── mocks/
│   ├── service/
│   ├── repository/
│   └── transport/
├── testdata/
└── docs/
```

## Directory Contracts

### `cmd/`
- Contains application entrypoints only.
- Keep `main.go` thin: config load, dependency wiring, startup/shutdown.
- No business logic in `cmd`.

### `internal/`
- Contains project-private code.
- Not importable from outside module.
- Preferred split:
- `app/`: use-case orchestration and dependency wiring.
- `domain/`: entities, value objects, domain rules.
- `service/`: business services.
- `repository/`: repository interfaces and contracts.
- `transport/http/`: handlers, DTO mapping, route registration.
- `platform/`: DB, cache, queue, external adapters.
- `config/`: config models and loaders.
- `errors/`: `ErrorBag` codes and mappings.
- `observability/`: logger/tracer/metrics wiring.

### `pkg/`
- Contains intentionally reusable libraries shared across projects.
- Must not depend on business-specific internals.
- Move code here only when reuse is proven.

### `mocks/`
- Contains test doubles for interfaces.
- Prefer generated mocks.
- Organize by concern (`service`, `repository`, `transport`) and keep naming predictable.

## Placement Rules

- If code is service-specific, place in `internal/`.
- If code is reusable and stable, place in `pkg/`.
- If code is startup-only, place in `cmd/`.
- If code is test double, place in `mocks/`.

## Anti-Patterns

- Business logic inside `cmd/main.go`.
- Dumping all files under `internal/` root with no bounded structure.
- Moving unstable code to `pkg/` too early.
- Handwritten mocks that drift from interfaces.
