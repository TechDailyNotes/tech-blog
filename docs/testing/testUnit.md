#### `Links`

[`Annotations -> JUnit`](https://techblog.streamlit.app/Annotations)

[`Annotations -> Mockito`](https://techblog.streamlit.app/Annotations)

[`Annotations -> PowerMockito`](https://techblog.streamlit.app/Annotations)

[`Annotations -> SpringBootTest`](https://techblog.streamlit.app/Annotations)

#### Test Double

1. Dummy

```markdown
<!-- 1. Definition -->

An object that is passed around but never used.
It is used to fill parameter lists.
```

```markdown
<!-- 2. Feature -->

PARAMETER ONLY
```

2. Fake

```markdown
<!-- 1. Definition -->

An object that has working implementations, but they are usually simplified.
```

```markdown
<!-- 2. Feature -->
```

3. Stubs

```markdown
<!-- 1. Definition -->

An object that provides predefined data and has no specific behaviours.
```

```markdown
<!-- 2. Feature -->

DATA ONLY
```

4. Spies

```markdown
<!-- 1. Definition -->

They are simplified mocks.
eg. XXXService
```

```markdown
<!-- 2. Feature -->

DATA AND SIMPLE BEHAVIORS
```

5. Mocks

```markdown
<!-- 1. Definition -->

1. They are objects that mock behaviours of real objects under different circumstances.
2. Their behaviours are defined by programmers.
   eg. XXXRepository
```

```markdown
<!-- 2. Feature -->

DATA AND BEHAVIORS
```

6. Captor

```markdown
<!-- 1. Definition -->

It is used to capture arguments for mocked methods.
```

```markdown
<!-- 2. Feature -->

DATA CAPTURE
```

#### Test Procedure

```markdown
<!-- 1. Init stubs -->

1. Use annotations
2. Use builders
```

```markdown
<!-- 2. Init variables -->
```

```java
/**
 * 3. Mock behaviors
 * @explain: mock behaviors of dependencies of tested method
 * @examples:
 */

when().thenReturn()
// or
doReturn().when()
// or
given().willReturn()
```

```markdown
<!-- 4. Call tested method -->
```

```java
/**
 * 5. Verify behaviors
 * @explain: verify mocked methods are called with certain arguments
 * @explain: verify mocked methods are called for certain times
 * @examples:
 */

verify().method()
```

```java
/**
 * 6. Assert results
 * @type: assert return values
 * @examples:
 */

assertThat()
assertEquals()
assertNotNull()
assertSame()

/**
 * @type: assert exceptions
 * @examples:
 */

assertThrows();

/**
 * @type: assert captured instances (used with @Captor)
 * @examples:
 */

Object instance = captor.getValue();
assertSame(instance, expectedInstance);

/**
 * @type: assert captured lambda arguments (used with @Captor)
 * @examples:
 */

Object lambda = captor.getValue();
lambda.execute();
verify(instanceOfLambda).method();
```

#### Test Types

```markdown
<!-- 1. Test return types and return values -->
```

```markdown
<!-- 2. Test passing parameters -->
```
