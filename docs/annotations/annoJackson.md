#### @JsonSerialize/@JsonDeserialize

```markdown
<!-- 1. Definition -->

指定序列化/反序列化类
```

```markdown
<!-- 2. Scenarios -->

1. @JsonSerialize 用在 setter 方法上,指定序列化类
2. @JsonDeserialize 用在 getter 方法上,指定反序列化类
```

```markdown
<!-- 3. Usage -->

1. 使用@JsonSerialize 注解的类,需要实现 JsonSerializer 接口,定制 serialize() 方法
2. 使用@JsonDeserialize 注解的类,需要实现 JsonDeserializer 接口,定制 deserialize() 方法
```

#### @JsonAutoDetect/@JsonIgnoreProperties/@JsonIgnore

```markdown
<!-- 1. Definition -->

设置序列化的包含、排除策略
```

```markdown
<!-- 2. @JsonAutoDetect -->

根据字段、Getter、Setter 的可见性设置策略

1.  Property:
    1. fieldVisibility
    2. getterVisibility
    3. isGetterVisibility
    4. setterVisibility
    5. creatorVisibility
2.  Enum:
    1. JsonAutoDetect.Visibility.ANY
    2. JsonAutoDetect.Visibility.NONE
    3. JsonAutoDetect.Visibility.NON_PRIVATE
    4. JsonAutoDetect.Visibility.PROTECTED_AND_PUBLIC
```

```markdown
<!-- 3. @JsonIgnoreProperties -->

@JsonIgnoreProperties({"字段名称"})自动忽略指定字段及其 setter、getter 方法
```
