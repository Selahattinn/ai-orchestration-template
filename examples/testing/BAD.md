# Testing Example: Bad

```go
func TestDoEverything(t *testing.T) {
	time.Sleep(5 * time.Second)
	got := runBigFlow()
	if got == nil {
		t.Fail()
	}
}
```

Why bad:
- Test name is ambiguous and non-behavioral.
- Uses `time.Sleep` for synchronization.
- Covers multiple unknown behaviors in one test.
- Failure output is not actionable.

```go
func TestCreateUser(t *testing.T) {
	_ = createUser(context.Background(), User{})
}
```

Why bad:
- No assertions.
- No explicit expected behavior.
- Silent pass even when behavior regresses.
