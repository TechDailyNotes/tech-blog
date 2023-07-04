#### final

1. for method parameter

```markdown
<!-- 1. Effect -->

It denotes a constant value (pointer) that cannot be changed.
```

```java
// 2. Syntax

public <T, R> R invoke(final String serviceName, final T request,ReturnActionWithEx<R> invoker);
```

2. for method itself

```markdown
<!-- 1. Effect -->

It denotes a method that cannot be overridden.
```

3. for class

```markdown
<!-- 1. Effect -->

It denotes a class that cannot be extended.
```
