#### @Mock

1. verify()

```markdown
<!-- 1. Definition -->

After a method call, use verify to check if an internal method is called and how many times it is called.
```

```java
// 2. Syntax:

@Mock
private EmailService mockedEmailService;

userService.register(user);
verify(mockedEmailService).sendEmail(
  eq("admin@test.com"),
  eq("Register Notification")
);
```

```java
// 3. Argument Matchers:
// @place: in the method called after verify().
// @effect: match the arguments of the method called after verify().

eq()
isNull()
notNull()
same()
contains()
matches()
startsWith()
endsWith()
```

```java
// 4. Method Call Times:

verify(mockedEmailService, times(1)) is the same as verify(mockedEmailService)
```

2. given().will()

```markdown
<!-- 1. Definition -->

Define the behaviour of a given method with given parameters.
```

```java
// 2. Syntax:

given(mockedEmailService.sendEmail(anyString(), anyString())).willReturn(true);
// or
when(mockedEmailService.sendEmail(anyString(), anyString())).thenReturn(true);
```

```java
// 3. Return Methods:

willReturn()
willThrow()
will(() -> {}) // lambda expression
```

#### @Captor

```markdown
<!-- 1. Definition -->

Capture the arguments of the method called after verify() for value checking.
```

```java
// 2. Syntax

ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
verify(mockedEmailService).sendEmail(captor.capture(), anyString());
assertEquals("admin@test.com", captor.getEmail());
assertEquals("admin", captor.getUsername());
```

#### @InjectMocks

```markdown
<!-- 1. Definition -->

Inject mocks into the class under test.
```
