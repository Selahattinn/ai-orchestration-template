# Naming Standard

Canonical naming rules for Go code generated under this template.

## General Rules

- Prefer clear, domain-oriented names over abbreviations.
- Keep naming consistent across `cmd/`, `internal/`, `pkg/`, and `mocks/`.
- Follow standard Go casing rules (`ExportedName`, `unexportedName`).
- Keep acronyms consistent (`HTTP`, `URL`, `ID`, `JSON`).

## Package Naming

- Use short, lowercase package names.
- Avoid underscores and mixed casing in package names.
- Package names should describe responsibility (`service`, `repository`, `transport`).
- Avoid generic package names like `utils`, `common`, `helpers`.

## Interface and Type Naming

- Use behavior-driven interface names where possible (`Creator`, `Finder`, `Publisher`).
- For service-level orchestration patterns, this is preferred:
- `type Handler interface { ... }`
- `type handler struct { ... }`
- `func NewHandler(...) Handler`
- Use domain nouns for entities and value objects (`User`, `Invoice`, `Session`).

## Function and Method Naming

- Use verb-first names for actions (`CreateUser`, `ListInvoices`, `SyncDevices`).
- For bool-returning checks, use intentful names (`IsHealthy`, `HasAccess`).
- Keep names specific enough to avoid context guessing.
- Avoid ambiguous names such as `Do`, `Handle`, `Run` unless scope is explicit.

## Variable Naming

- Prefer `ctx` for `context.Context`.
- Prefer `err` for error variables.
- Use `req`/`resp` for transport-layer request/response variables.
- Use descriptive names for domain values (`invoiceID`, `retryBackoff`).

## File Naming

- Use lowercase snake_case for file names (`user_handler.go`, `invoice_service.go`).
- Use `_test.go` suffix for tests.
- Name files by dominant responsibility, not by technical layer only.

## Test and Mock Naming

- Test names should describe behavior: `TestCreateUser_WhenRepositoryFails_ReturnsError`.
- Mock types should reference the mocked contract (`MockUserRepository`).
- Keep generated mocks in `mocks/<concern>/`.

## API/DTO Naming

- Use explicit DTO suffixes (`CreateUserRequest`, `CreateUserResponse`).
- Avoid generic DTO names (`Input`, `Output`, `Data`).
- Keep JSON field names semantically aligned with domain language.

## Error Naming

- Use stable error code constant names (`ErrCodeUserNotFound`).
- Use clear sentinel error names where needed (`ErrInvalidState`).
- Keep `ErrorBag.Code` catalog readable and versionable.

## Anti-Patterns

- One-letter or cryptic identifiers outside tiny scopes.
- Inconsistent acronym formatting (`HttpID`, `UrlID`).
- Reusing the same name for unrelated concepts.
- Generic file/package names that hide intent.

## Done Criteria

- Naming rules cover package/type/function/variable/file/test/mock levels.
- Anti-patterns are documented with clear examples.
- Rules are aligned with coding style and hierarchy policies.
