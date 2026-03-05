# Logging Standard

Canonical logging policy for generated Go services.

## Logger Choice

- Use `zap` as the logging backend.
- Use `*zap.SugaredLogger` in application and handler layers.

## Level Policy

- `Debugw`: deep diagnostics, feature-flag traces, temporary troubleshooting.
- `Infow`: normal lifecycle events and successful state transitions.
- `Warnw`: recoverable failures, retries, fallback paths, partial degradation.
- `Errorw`: request/job failures, dependency failures, and user-impacting errors.

## Required Context Keys

Log with structured key-value fields where available:
- `request_id`
- `trace_id`
- `service`
- `operation`
- `duration_ms`
- `error_code`

## Security and Privacy

- Never log secrets (tokens, passwords, private keys).
- Never log raw PII; mask or hash when needed.
- Keep payload logging whitelisted and size-limited.

## ErrorBag Mapping

When logging `ErrorBag`, include structured fields:
- `error_code` from `Code`
- `http_status` from `HTTPStatus`
- `error_message` from `Message`

Avoid dumping full internals of `Cause` when it may contain sensitive data.

## Anti-Patterns

- `fmt.Println` for runtime operational logs.
- Unstructured free-text logs without stable fields.
- Logging the same error repeatedly without attempt counters.
