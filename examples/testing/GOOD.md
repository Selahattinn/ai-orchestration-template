# Testing Example: Good

## Table-Driven Unit Test

```go
func TestValidateStatus_WhenInputInvalid_ReturnsError(t *testing.T) {
	tests := []struct {
		name    string
		input   string
		wantErr bool
	}{
		{name: "empty", input: "", wantErr: true},
		{name: "active", input: "active", wantErr: false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := ValidateStatus(tt.input)
			if (err != nil) != tt.wantErr {
				t.Fatalf("ValidateStatus() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
```

## Integration Test with Context Timeout

```go
func TestUserRepository_CreateUser_PersistsRecord(t *testing.T) {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	repo := newTestUserRepository(t)
	err := repo.CreateUser(ctx, User{ID: "u-1"})
	if err != nil {
		t.Fatalf("CreateUser() returned error: %v", err)
	}
}
```

Why good:
- Behavior-focused naming.
- Deterministic assertions.
- Explicit timeout and cleanup.
