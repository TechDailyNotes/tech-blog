#### @Mock/@Spy

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
/**
 * 3. Argument Matchers:
 * @place: in the method called after verify().
 * @effect: match the arguments of the method called after verify().
 */

// @examples:
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
// or
@Captor
ArgumentCaptor<String> captor;

verify(mockedEmailService).sendEmail(captor.capture(), anyString());
assertEquals("admin@test.com", captor.getEmail());
assertEquals("admin", captor.getUsername());
```

```java
/**
 * 3. Usage
 * @place: methods called inside the tested method.
 * @place: tested method call.
 */

/**
 * @avoid: use captor with stubbing.
 * @reason: reduced readability
 *          -- not obvious what the captor refers to.
 * @reason: reduced defect localization
 *          -- if the stubbing method is not called, the program reports an error.
 *          -- but we expect the test to fail.
 * @examples:
 */
Credentials credentials = new Credentials("admin", "admin");
when(platform.authenticate(credentialCaptor.capture())).thenReturn(true);
assertTrue(emailService.authenticateSuccess(credentials));
assertEquals(credentials, captor.getValue());
```

#### @InjectMocks

```markdown
<!-- 1. Definition -->

Inject mocks into the class under test.
```
