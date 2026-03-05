# Hexagonal Boundary Standard

Strict boundary and hierarchy rules for `hexagonal` architecture mode.

## Goal

Make inbound/outbound concepts explicit and enforceable for backend-only Go services.

## Canonical Hierarchy (Hexagonal Mode)

```text
.
├── cmd/
│   └── <service-name>/
│       └── main.go
├── internal/
│   ├── domain/
│   ├── application/
│   │   ├── usecase/
│   │   └── ports/
│   │       ├── inbound/
│   │       └── outbound/
│   ├── adapters/
│   │   ├── inbound/
│   │   │   ├── http/
│   │   │   ├── grpc/
│   │   │   └── consumer/
│   │   └── outbound/
│   │       ├── persistence/
│   │       ├── external/
│   │       ├── queue/
│   │       └── cache/
│   ├── bootstrap/
│   │   ├── wire.go
│   │   └── wire_gen.go
│   ├── errors/
│   └── observability/
├── config/
└── docs/
```

## Inbound/Outbound Semantics

- Inbound port:
  Interface exposed by application/use-case layer for requests entering the core.
- Inbound adapter:
  Transport-facing implementation that converts external input into inbound port calls.
- Outbound port:
  Interface declared by core/application for dependencies needed from outside.
- Outbound adapter:
  Implementation of outbound ports (DB, cache, queue, external services).

## Dependency Direction Rules

Required direction:

1. `adapters/inbound` -> `application/usecase` (via inbound ports)
2. `application/usecase` -> `application/ports/outbound` (interfaces only)
3. `adapters/outbound` -> implements `application/ports/outbound`
4. `domain` has no dependency on adapters/transport/framework concerns

Forbidden direction examples:

- `domain` -> `adapters/*`
- `application/usecase` -> concrete DB/client implementations
- `adapters/outbound` -> `adapters/inbound`
- `adapters/inbound` -> `adapters/outbound` (direct coupling)

## Interface Placement Rules

- Inbound ports live under `internal/application/ports/inbound`.
- Outbound ports live under `internal/application/ports/outbound`.
- Adapter implementations must not declare business contracts owned by application/domain.

## Naming Rules

- Inbound ports: `<Action>UseCase` (example: `CreateOrderUseCase`)
- Outbound ports: `<Capability>Port` (example: `OrderRepositoryPort`, `PaymentGatewayPort`)
- Inbound adapters: `<Transport><Feature>Handler` or `<Transport><Feature>Controller`
- Outbound adapters: `<Provider><Capability>Adapter`

## DI and Bootstrap Rules

- Dependency graph assembly is done with `google/wire` under `internal/bootstrap`.
- `wire` provider sets should be grouped by boundary (`inboundSet`, `useCaseSet`, `outboundSet`).
- Configuration loaders and config models live under root `config/`.
- Manual wiring in non-bootstrap packages is forbidden unless an active waiver exists.

## Required Architecture Artifact Sections (Hexagonal)

1. Inbound ports list and owning use cases.
2. Outbound ports list and mapped adapters.
3. Dependency matrix (`allowed` and `forbidden`).
4. Inbound -> UseCase -> Outbound interaction map.
5. Data ownership and transaction boundaries.
6. DI plan (`wire` sets, bootstrap location, waiver if any).

## Block Conditions

Return `BLOCK` when any condition occurs:

- Inbound/outbound ports are missing or mixed.
- Use-case layer imports concrete adapter implementations.
- Domain layer depends on transport/framework/provider code.
- Outbound adapter bypasses port contracts.
- Circular dependency exists.

## Done Criteria

- Canonical hexagonal hierarchy is explicit.
- Inbound/outbound definitions and direction rules are explicit.
- Required artifact sections and `BLOCK` conditions are explicit.
