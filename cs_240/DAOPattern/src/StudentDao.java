package student;

import java.util.List;

public interface StudentDao {
  public List<Student> getAllStudents();
  public Student getStudent(int id);
  public void addStudent(Student student);
  public void updateStudent(Student student);
  public void deleteStudent(Student student);
}
