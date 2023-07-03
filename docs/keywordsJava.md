#### final

1. When used in method parameters, it denotes a constant value (pointer) that cannot be changed.

```java
public <T, R> R invoke(final String serviceName, final T request,ReturnActionWithEx<R> invoker);
```
