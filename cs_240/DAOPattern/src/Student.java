package student;

public class Student {
   static int next_id = 0; // class level id

  String name;
  int id;

  public Student() {
    this.name = "";
    this.id = next_id;
    next_id++; // increment id counter
  }

  public String getName() {
    return this.name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getId() {
    return this.id;
  }


}
