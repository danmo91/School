


# Tasks

## create dictionary from text file (words.txt)

words.txt =>
my
name
is
dan
i
like
my
name

dictionary trie (tree) =>
my    2
name  2
is    1
dan   1
i     1
like  1

- dictionary words are case insensitive

## in-class

- constructors can call each others
- this(name, age) is a constructor that calls another constructor

When is the best time to use a static variable or method? On a person class when you want to
update the value of class level variables like a PersonID

probably should start using getters and setters.  Failing to do so, starts introducing bugs.

* every class inherits from object by default
[Object] => [Person]

@override
public string toString() {
  // return string
}

@Override
public boolean equals(Object o) {
  // compare object to itself
  if(o == this
    return true;

  // compare to null
  if(o == null)
    return false;

  // compare to getClass() or data type
  if (getClass() != o.getClass())
    return false;

  // finally compare the actual objects

  // cast object as person
  Person other = (Person)o;
  return (id == other.id &&
          name.equals(other.name) &&
          age == other.age)

}


#### Hashcode

int hashCode()

a hashtable has add, contains, remove().  They call the object's hashCode() and uses that hashCode to save, access, remove
that object later.  The table mod's the hashCode by the size of the array so it will always fit.  Each element in the hashTable
is a list of all objects who's hashCode match

the default hashCode() returns memory address
