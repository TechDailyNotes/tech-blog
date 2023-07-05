#### 创建服务

1. 契约式设计 (Design by Contract, DbC)

```markdown
<!-- 1. Definition -->

一种计算机软件的设计方法.
要求设计者为软件组件定义正式的、精确的、可验证的接口,为组件增加了先验条件、后验条件、不变式.
```

```markdown
<!-- 2. Extension -->

契约式设计(DbC)扩展到方法设计上,要求方法的契约一般具有以下信息:

1. 方法接受/不接受的数值/类型(Parameters)
2. 方法返回的数值/类型(Return value)
3. 方法的异常(Exception)
4. 方法的副作用(Side effect)
5. 方法的前置条件(Precondition)
6. 方法的后置条件(Postcondition)
7. 方法的不变式(Invariant)
8. 方法的性能(Performance)
```

```markdown
<!-- 3. Platform -->

MOM

1. Definition: Model Object Management
2. Features:
   1. Streamline the service generation and management with contracts
   2. Support multiple contracts
      1. BJSC
      2. Protobuf
      3. XSD
      4. Json Schema
   3. Support multiple languages
```
