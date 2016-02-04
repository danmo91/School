package student;

public class Main {
  public static void main(String[] args) {
    // use cool DAO stuff here
    StudentDao studentDao = new StudentDaoImpl();

    // create students
    Student student1 = new Student();
    student1.setName("Dan");
    Student student2 = new Student();
    student2.setName("Andy");

    studentDao.addStudent(student1);
    studentDao.addStudent(student2);

    // print all students
    for(Student student : studentDao.getAllStudents()) {
      System.out.println("Student: [ id: " + student.getId() + ", Name: " + student.getName() + " ]");
    }

    // update students
    student1.setName("Dan Morain");
    student2.setName("Andy Mockler");

    studentDao.updateStudent(student1);
    studentDao.updateStudent(student2);

    // print all students
    for(Student student : studentDao.getAllStudents()) {
      System.out.println("Student: [ id: " + student.getId() + ", Name: " + student.getName() + " ]");
    }

    // delete student
    Student myStudent = studentDao.getStudent(1);
    studentDao.deleteStudent(myStudent);

    // print all students
    for(Student student : studentDao.getAllStudents()) {
      System.out.println("Student: [ id: " + student.getId() + ", Name: " + student.getName() + " ]");
    }

  }
}
