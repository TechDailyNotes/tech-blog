#### Adapter Pattern (适配器模式)

#### Bridge Pattern (桥接模式)

#### Filter/Criteria Pattern (过滤器模式)

#### Composite Pattern (组合模式)

```markdown
<!-- 1. Definition -->

Decouple simple objects and complex objects, and treat them uniformly.
```

#### Decorator Pattern (装饰器模式)

#### Facade Pattern (外观模式)

#### Flyweight Pattern (享元模式)

#### Proxy Pattern (代理模式)

1. Concepts:

```markdown
<!-- 1. Definition -->

Use an agent instance (proxy) to invoke target instance's methods.
```

```markdown
<!-- 2. Advantages -->

1. Separate target instances with client instances
2. Protect target instances, prevent direct access from clients to targets
3. Enhance target instances with feature extensions
4. Decouple services
5. Ensure scalability:
   中介类只要封装目标类,并实现同一接口,便可以代理目标类方法并拓展新功能
```

2. Scenarios:

```java
/**
 * 1. 静态代理:
 * @explain: 中介实例自动初始化封装的目标实例
 * @connections: 中介实例、目标实例实现同一个接口
 *               中介实例封装目标实例
 *               中介实例转发方法请求到内部目标对象
 * @examples:
 */

// 租房方法接口
public interface IRentHouse {
    void rentHouse();
}

// 租房目标实现类
public class RentHouse implements IRentHouse {
    @Override
    public void rentHouse() {
        System.out.println("租了一间房子。。。");
    }
}

// 租房代理类
public class IntermediaryProxy implements IRentHouse { // 实现功能接口
    private IRentHouse rentHouse; // 封装目标实现类
    public IntermediaryProxy(IRentHouse irentHouse){
        rentHouse = irentHouse;
    }
    @Override
    public void rentHouse() {
        System.out.println("交中介费");
        rentHouse.rentHouse(); // 转发方法请求到目标实现类
        System.out.println("中介负责维修管理");
    }
}

// main
public class Main {
    public static void main(String[] args){
        //定义租房
        IRentHouse rentHouse = new RentHouse();
        //定义中介
        IRentHouse intermediary = new IntermediaryProxy(rentHouse);
        //中介租房
        intermediary.rentHouse();
    }
}
```

```java
/**
 * 2. 强制代理
 * @explain: 强制要求开发者手动初始化代理类,并转发方法请求到代理类
 * @connections: 中介类目标类实现同一功能接口
 *               目标类封装中介类,通过getProxy()方法
 */
```

#### `References`

[`代理模式教程 -- 知乎`](https://zhuanlan.zhihu.com/p/72644638)
