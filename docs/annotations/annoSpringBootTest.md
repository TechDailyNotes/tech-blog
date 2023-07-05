#### `Links`

[`Testing -> Unit Testing`](https://techblog.streamlit.app/Testing)

#### SpringRunner

```markdown
<!-- 1. Definition -->

Standard Spring JUnit4 test runner.
```

#### @ContextConfiguration

```markdown
<!-- 1. Definition -->

Load the configuration of the test context.
```

```java
/**
 * 2. Syntax
 * @framework: Spring
 * @property: locations
 * @examples:
 */

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {"classpath*:/*.xml"})
@SpringBootTest(classes = {SpringBootApp.class})
public class AServiceTest {}

/**
 * @framework: Spring Boot
 * @property: classes
 * @examples:
 */

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = {BaijiServletConfiguration.class})
@SpringBootTest(classes = {SpringBootApp.class})
public class BServiceTest {}
```

#### @SpringBootTest

```markdown
<!-- 1. Definition -->

Configure the default SpringBoot Test framework and customize features.
```

```markdown
<!-- 2. Elements -->

1. webEnvironment:
   1. Definition: runtime environment of the test
   2. Types: MOCK, RANDOM_PORT, DEFINED_PORT, NONE
2. classes:
   1. Definition: classes to use for loading an ApplicationContext
```
