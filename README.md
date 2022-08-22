### The five SOLID principles are:
- Single responsibility principle: a class should have one, and only one, reason to change.

- Open-closed principle: software entities should be open for extension, but closed for modification. It should be possible to extend the behavior of a class without  modifying it.

- Liskov Substitution principle: subclasses should be substitutable for their superclasses.

- Interface segregation principle: many small, client-specific interfaces are better than big general interfaces.

- Dependency inversion principle: software entities should depend on abstractions, not in concretions.

### Notes 
You will find a folder inside "src" for every SOLID principle. And for each of them:
- "wrong" folder contains code that violates the principle.
- "right" folder contains code that satisfies the principle after some modifications of the code inside "wrong".

There is on exception. I am applying the Interface segregation Principle in order to satisfy the Liskov Substitution Principle. That's why:
- The folder of the Liskov Substitution Principle ("LIS") just contains a subfolder named "wrong".
- The folder of the Interface Segregation Principle ("ISP") just contains a subfolder named "right".

### To execute the examples
#### You should be in the root folder "Solid_Principles_Python"
To execute SRP examples:
```sh
python3 -m src.SRP.wrong
```

```sh
python3 -m src.SRP.right
```

To execute OCP examples:
```sh
python3 -m src.OCP.wrong
```

```sh
python3 -m src.OCP.right
```

To execute LIS example:
```sh
python3 -m src.LIS.wrong
```

To execute ISP example:
```sh
python3 -m src.ISP.right
```

To execute DIP examples:
```sh
python3 -m src.DIP.wrong
```

```sh
python3 -m src.DIP.right
```