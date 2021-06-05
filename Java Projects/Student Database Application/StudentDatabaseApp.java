package studentdatabaseapp;
import java.util.Scanner;

public class StudentDatabaseApp {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
/*		System.out.println("**********************************************");
		Student s1 = new Student();
		s1.enroll();
		s1.payTuition();
		System.out.println(s1.toString());
		System.out.println("**********************************************");
		Student s2 = new Student();
		s2.enroll();
		s2.payTuition();
		System.out.println(s2.toString());
		System.out.println("**********************************************");
		Student s3 = new Student();
		s3.enroll();
		s3.payTuition();
		System.out.println(s3.toString());		*/
		//System.out.println(s1.showInfo());
		
		//Ask the user how many new students we want to add
		System.out.println("Enter the number of students to enroll: ");
		Scanner sc = new Scanner(System.in);
		int numOfStudents = sc.nextInt();
		Student[] students = new Student[numOfStudents];
		
		// Create n number of new student
		for(int n = 0; n < numOfStudents; n++) {
			students[n] = new Student();
			students[n].enroll();
			students[n].payTuition();
		}
		for(int n = 0; n < numOfStudents; n++) {
			System.out.println("**************************");
			System.out.println(students[n].toString());
		}
		/*System.out.println(students[0].toString());
		System.out.println(students[1].toString());
		System.out.println(students[2].toString());*/
	}
}
