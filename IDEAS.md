## Ideas

- Custom properties for functions.
- New property for functions: `Body`:

  ```akuma
  fc myFunction { ReturnType: Integer, Body: "return 10;" };
  ```

  The shorthand for `Body`:

  ```akuma
  fc myFunction { ReturnType: Integer } => { return 10; };
  ```
