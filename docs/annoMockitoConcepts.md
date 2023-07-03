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

They are objects that mock behaviours of real objects under different circumstances.
Their behaviours are defined by programmers.
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
