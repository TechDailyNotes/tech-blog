#### `Links`

[`Testing -> Unit Testing`](https://techblog.streamlit.app/Testing)

#### @Mock/@Spy

1. Private method: `when().thenReturn()` `verifyPrivate()`

```markdown
<!-- 1. Definition -->

Mock and verify private methods
```

```java
/**
 * 2. Syntax of when().thenReturn()
 * @explain: call private method of mock
 * @param: ArgumentMatchers is used to match arguments.
 * @examples:
 */

when(mock, "privateMethod", ArgumentMatchers.any()).thenReturn()
// or
doReturn().when(mock, "privateMethod", ArgumentMatchers.any())
```

```java
/**
 * 3. Syntax of verifyPrivate():
 * @explain: verify private method of mock
 * @param: ArgumentMatchers is used to match arguments.
 * @examples:
 */

verifyPrivate(mock).invoke("privateMethod", ArgumentMatchers.any())
```

2. Static method: `mockStatic()` `verifyStatic()`

```markdown
<!-- 1. Definition -->

Mock and verify static methods
```

```java
/**
 * 2. Syntax of mockStatic():
 * @explain: mock static method
 * @type: static method with no arguments
 * @solution: method reference
 * @examples:
 */

try (MockedStatic<StaticClass> mockedStatic = Mockito.mockStatic(StaticClass.class)) {
  mockedStatic.when(StaticClass::staticMethod).thenReturn();
}

/**
 * @type: static method with arguments
 * @solution: lambda expression
 * @examples:
 */

try (MockedStatic<StaticClass> mockedStatic = Mockito.mockStatic(StaticClass.class)) {
  mockedStatic.when(() -> StaticClass.staticMethod(ArgumentMatchers.any(), Object obj)).thenReturn();
}
```

```java
/**
 * 3. Syntax of verifyStatic():
 * @explain: verify static method's interactions
 * @param: atLeastOnce() is used to verify the method is called at least once. (interaction)
 * @variation: verifyNoMoreInteractions()
 * @examples:
 */

PowerMockito.verifyStatic(StaticClass.class, atLeastOnce());
```

3. Constructor: `whenNew()` `verifyNew()`

```markdown
<!-- 1. Definition -->

Mock and verify constructor's behaviors
```

```java
/**
 * 2. Syntax of whenNew()
 * @explain: mock constructor
 * @examples:
 */

PowerMockito.whenNew(StaticClass.class)
  .withAnyArguments()
  .thenReturn(mock);
// or
PowerMockito.whenNew(StaticClass.class)
  .withArguments(Object obj, ArgumentMatchers.any())
  .thenReturn(mock);
// or
PowerMockito.whenNew(StaticClass.class)
  .withNoArguments()
  .thenReturn(mock);
```

```java
/**
 * 3. Syntax of verifyNew()
 * @explain: verify constructor's interactions
 * @examples:
 */

PowerMockito.verifyNew(StaticClass.class, atLeastOnce())
  .withArguments(Object obj, ArgumentMatchers.any());
// or
PowerMockito.verifyNew(StaticClass.class, atLeastOnce())
  .withNoArguments();
// or
PowerMockito.verifyNew(StaticClass.class, atLeastOnce())
  .withAnyArguments();
```

4. Response controls: `doNothing()` `doThrow()` `doReturn()` `doAnswer()`

```java
/**
 * 1. doNothing()
 * @definition: do nothing when a method is called.
 * @examples:
 */

doNothing().when(mock).method();
```

```java
/**
 * 2. doThrow()
 * @definition: throw an exception when a method is called.
 * @examples:
 */

doThrow(new RuntimeException()).when(mock).method();
```

```java
/**
 * 3. doAnswer()
 * @definition: do a customized logic when a method is called.
 * @examples:
 */

doThrow(
  invocation -> {
    Object[] args = invocation.getArguments();
    Object mock = invocation.getMock();
    return null;
  }
).when(mock).method();
```

```java
/**
 * 4. doCallRealMethod()
 * @definition: call the real method when a method is called.
 * @explain: it's used in partial mocking.
 * @examples:
 */

doCallRealMethod().when(mock).method();
```

#### `References`

[`PowerMock Source Code`](https://github.com/powermock/powermock)

[`PowerMock Framework Site`](https://powermock.github.io/)

[`Introduction to PowerMock -- Baeldung`](https://www.baeldung.com/intro-to-powermock)
