#### @PostConstruct

```markdown
<!-- 1. Definition -->

注解初始化方法,被注解的方法初始化依赖于 Bean 变量.
```

```markdown
<!-- 2. Reason -->

SpringBoot 的实例化过程中,构造器先于依赖注入(@Autowired)执行.
因此依赖其他 Bean 的变量无法在构造器中初始化.
```

```markdown
<!-- 3. Bean Initialization Process -->

1. 初始化父类静态变量/执行父类静态代码块
2. 初始化子类静态变量/执行子类静态代码块
3. 初始化父类实例变量/执行父类实例代码块
4. 执行父类构造器
5. 初始化子类实例变量/执行子类实例代码块
6. 执行子类构造器
7. 依赖注入
8. @PostConstruct
9. 执行 init()方法,给变量赋值
```

```markdown
<!-- 4. Notes -->

@PostConstruct 被系统默认自动调用
```
