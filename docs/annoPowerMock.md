#### @Runwith

```markdown
<!-- 1. Definition -->

1. Runwith is used to run the test with a specified runner.
2. Optional runners:
   1. MockitoJUnitRunner -- for Mockito tests
   2. PowerMockRunner -- for PowerMockito tests
```

```java
// 2. Syntax:

@RunWith(MockitoJUnitRunner.class)
@RunWith(PowerMockRunner.class)
```

#### @PrepareForTest

```markdown
<!-- 1. Definition -->

1. PrepareForTest prepares the class for test.
2. Similar to @Mock, @Spy, @InjectMocks.
3. It's used with mock() and mockStatic() methods.
```

#### @Mock/@Spy

1. private method:

   when().thenReturn()/verifyPrivate()

```markdown
<!-- 1. Definition -->

Mock and verify private methods
```

```java
/**
 * 2. Syntax of when().thenReturn()
 * @explain: call private method of mock
 * @param: ArgumentMatchers is used to match arguments.
 * @example:
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
 * @example:
 */
verifyPrivate(mock).invoke("privateMethod", ArgumentMatchers.any())
```

2. mockStatic()/verifyStatic()

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
 * @example:
 */
try (MockedStatic<StaticClass> mockedStatic = Mockito.mockStatic(StaticClass.class)) {
  mockedStatic.when(StaticClass::staticMethod).thenReturn();
}

/**
 * @type: static method with arguments
 * @solution: lambda expression
 * @example:
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
 * @example:
 */
PowerMockito.verifyStatic(StaticClass.class, atLeastOnce());
```

3. whenNew()/verifyNew()

```markdown
<!-- 1. Definition -->

Mock and verify constructor's behaviors
```

```java
/**
 * 2. Syntax of whenNew()
 * @explain: mock constructor
 * @example:
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
 * @example:
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
