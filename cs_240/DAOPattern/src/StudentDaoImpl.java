package student;

import java.util.ArrayList;
import java.util.List;

public class StudentDaoImpl implements StudentDao {
  // put db object here
  List<Student> students;

  public StudentDaoImpl() {
    this.students = new ArrayList<Student>();
  }

  public List<Student> getAllStudents() {
    return this.students;
  }

  public Student getStudent(int id) {
    return this.students.get(id);
  }

  public void addStudent(Student student) {
    this.students.add(student.getId(), student);
  }

  public void updateStudent(Student student) {
    this.students.get(student.getId()).setName(student.getName());
    System.out.println("Student: Id " + student.getId() + " updated in database");
  }

  public void deleteStudent(Student student) {
    this.students.remove(student.getId());
    System.out.println("Student: Id " + student.getId() + " removed from database");
  }
}
