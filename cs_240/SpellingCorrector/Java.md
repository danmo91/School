## Java

### Interfaces

A Java interface is like a class, except a Java interface can only contain method signatures and fields. An Java interface cannot contain an implementation of the methods, only the signature (name, parameters and exceptions) of the method. You can use interfaces in Java as a way to achieve polymorphism.

interfaces help us work together.  It defines a standard for how a class should be structured
so we can all work on something together and have a standard interface

### Constructors

- constructors with different signatures can call other constructors

for example:
```java
class Person {

  public Person(String name) {
    this.name = name;
  }

  public Person(String name, int age) {
    this.Person(name);
    this.age = age;
  }

}

```

### Static methods and fields

When is the best time to use a static variable or method?

Example:

```java
class Person {


  // the person class has an ID field to give new instances of person
  private static id = 1;

  // each time a person instance is created, the id is incremented by 1
  private static void updateId () {
    this.id++;
  }

}
```

### Getters and Setters

- installed Atom plugin for getters and setters
- creates a single entry point to modifying those object fields

### Classes and Overriding default methods

- every class inherits from Object
```java
class Person extends Object {
  // my person class
}
```

```java
@Override
public string toString() {
  // return string
}

@Override // cool things to check for when overriding '==' operator
public boolean equals(Object o) {

  // compare object to itself
  if(o == this
    return true;

  // compare to null
  if(o == null)
    return false;

  // compare to getClass(), which returns the class or data type of the object
  if (getClass() != o.getClass())
    return false;

  // finally compare the actual objects
  Person other = (Person)o; // cast object as person
  return (id == other.id &&
          name.equals(other.name) &&
          age == other.age)
}
```

#### HashCode functions

Hashtables are highly fast and efficient arrays.  Every object generates a 'unique' hashcode
that is scaled down to the size of the hashtable using (hashcode %mod HASHTABLE_SIZE )

The goal of a hashcode function is to generate an int that uniquely identifies
the objects.

int hashCode()

a hashtable has add, contains, remove().  They call the object's hashCode() and uses that hashCode to save, access, remove
that object later.  The table mod's the hashCode by the size of the array so it will always fit.  Each element in the hashTable
is a list of all objects who's hashCode match

the default hashCode() returns memory address
