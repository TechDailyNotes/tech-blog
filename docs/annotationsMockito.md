#### Test Double

1. Dummy

```text
An object that is passed around but never used.
rIt is used to fill parameter lists.
```

2. Fake

```text
An object that has working implementations, but they are usually simplified.
```

3. Stubs

```text
An object that provides predefined data and has no specific behaviours.
```

4. Spies

```text
They are simplified mocks.
eg. XXXService
```

5. Mocks

```text
They are objects that mock behaviours of real objects under different circumstances.
Their behaviours are defined by programmers.
eg. XXXRepository
```

6. Captor

```text
It is used to capture arguments for mocked methods.
```

#### @Mock

1. verify

   After a method call, use verify to check if an internal method is called and how many times it is called.

```java
// Syntax:
@Mock
private EmailService mockedEmailService;
userService.register(user);
verify(mockedEmailService).sendEmail(
  eq("admin@test.com"),
  eq("Register Notification")
);
```

```java
// Note:
verify(mockedEmailService, times(1)) is the same as verify(mockedEmailService)
```

```java
// Argument Matchers:
eq()
isNull()
notNull()
same()
contains()
matches()
startsWith()
endsWith()
```

2. given ... will ...

   Define the behaviour of a given method with given parameters.

```java
// Syntax:
given(mockedEmailService.sendEmail(anyString(), anyString()))
  .willReturn(true);
```

```java
// Return Methods:
willReturn()
willThrow()
will(() -> {}) // lambda expression
```

#### Captor

```java
ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
verify(mockedEmailService).sendEmail(captor.capture(), anyString());
assertEquals("admin@test.com", captor.getEmail());
assertEquals("admin", captor.getUsername());
```

#### @InjectMocks

1. Concept

   Inject mocks into the class under test.
