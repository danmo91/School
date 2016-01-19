

# JUNIT Testing

https://github.com/junit-team/junit/wiki/Getting-started

## Compile tests
```sh
$ javac -cp lib/junit-4.12.jar:hamcrest-core-1.3.jar -sourcepath src/ test/CalculatorTest.java
```
### Running tests

```sh
$ java -cp .:lib/junit-4.12.jar:lib/hamcrest-core-1.3.jar:test/:src/ org.junit.runner.JUnitCore CalculatorTest
```
