#### `Links`

[`Testing -> Unit Testing`](https://techblog.streamlit.app/Testing)

#### @Runwith/@ExtendWith

```java
/**
 * 1. Definition
 * @annotation: @Runwith
 * @effect: run the test with a specified runner.
 * @runner: MockitoJUnitRunner -- for Mockito tests
 * @runner: PowerMockRunner -- for PowerMockito tests
 * @runner: SpringJUnit4ClassRunner/SpringRunner -- for Spring tests (compatible with Beans)
 * @syntax:
 */

@RunWith(MockitoJUnitRunner.class)
@RunWith(PowerMockRunner.class)
@RunWith(SpringJUnit4ClassRunner.class)

/**
 * @annotation: @ExtendWith
 * @effect: run the test with a specified extension.
 * @extension: MockitoExtension -- for Mockito tests
 * @extension: PowerMockExtension -- for PowerMockito tests
 * @extension: SpringExtension -- for Spring tests (compatible with Beans)
 * @syntax:
 */

@ExtendWith(MockitoExtension.class)
@ExtendWith(PowerMockExtension.class)
@ExtendWith(SpringExtension.class)
```

```java
// 2. Alternatives

@Before
public void init() {
  MockitoAnnotations.openMocks(this);
}
```

#### @PrepareForTest

```markdown
<!-- 1. Definition -->

1. PrepareForTest prepares the class for test.
2. Similar to @Mock, @Spy, @InjectMocks.
3. It's used with mock() and mockStatic() methods.
```

#### `References`

[`Testing in Spring Boot -- Baeldung`](https://www.baeldung.com/spring-boot-testing)
