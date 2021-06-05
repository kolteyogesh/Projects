package studentdatabaseapp;
import java.util.Scanner;

public class Student 
{
	private String firstName;
	private String lastName;
	private int gradeYear;
	private String courses;
	private String studentID;
	private int tuitionBalance = 0;
	private static int costOfCourse = 600;
	private static int id = 1000;
	
	//  Constructor:  prompt user to enter student name and year
	public Student() {
		Scanner sc = new Scanner(System.in);
		System.out.println("***********************************");
		System.out.print("Enter student first name: ");
		this.firstName = sc.nextLine();
		System.out.print("Enter student last name: ");
		this.lastName = sc.nextLine();
		System.out.print("1 - Freshmen\n2 - Sophmore\n3 - Junior\n4 - Senior\nEnter student class level: ");
		this.gradeYear = sc.nextInt();
		//this.studentID = studentID;	this.courses = courses;	this.tuitionBalance = tuitionBalance;		this.costOfCourse = costOfCourse;
		setStudentID();
		//System.out.println(firstName + " " + " " + lastName + " " + gradeYear+ " " + studentID);		
	}
	// Generate an ID
	private void setStudentID() {
		//Grade Level + ID
		id++;
		this.studentID = gradeYear + " " + id;
		//System.out.println("Student-id: "+ studentID);
	}
	// Enroll in courses
	public void enroll() {
		//Get inside the loop, user hits 0.
		do {
			System.out.print("Enter the course to enroll (Q to quit): ");
			Scanner sc = new Scanner(System.in);
			String course = sc.next();
			System.out.println("Course : "+ course);
			//if(course != "Q") {
			if(!course.equals("Q")) {
				courses = courses + "\n	"+ course;
					//System.out.println("Courses: "+ courses);
				tuitionBalance = tuitionBalance + costOfCourse;
					System.out.println("TuitionBalance: "+ tuitionBalance);
			} else {
				//System.out.println("BREAK!");
				break;	
			}
		} while (1 != 0);
		//System.out.println("ENROLLED IN : " + courses);
		//System.out.println("TUITION BALANCE : " + tuitionBalance);
	}
	// View balance
	public void viewBalance() {
		System.out.println("Your balance is: $" + tuitionBalance);
	}
	// Pay Tuition
	//public void payTuition(int payment){
	public void payTuition(){
		viewBalance();
		System.out.print("Enter your payment: $");
		Scanner sc = new Scanner(System.in);
		int payment = sc.nextInt();
		tuitionBalance = tuitionBalance - payment;
		System.out.println("Thank you for your payment of $" + payment);
		viewBalance();
	}
	// Show status
	public String toString() {
		return "Name: " + firstName + " " + lastName + 
			"\nGrade Level: " + gradeYear +
			"\nStudent ID: " + studentID +
			"\nCourses Enrolled: " + courses +
			"\nBalance: $" + tuitionBalance;
	}
}

/*
Enter student first name: Yogesh
Enter student last name: Kolte
1 - Freshmen
2 - Sophmore
3 - Junior
4 - Senior
Enter student class level: 3
Student-id: 3 1001
Yogesh  Kolte 3 3 1001
Enter the course to enroll (Q to quit): Arts 100
Course : Arts
TuitionBalance: 600
Enter the course to enroll (Q to quit): Physics 100
Course : Physics
TuitionBalance: 1200
Enter the course to enroll (Q to quit): Maths 100
Course : Maths
TuitionBalance: 1800

Enter the course to enroll (Q to quit): Q
Course : Q
BREAK!
ENROLLED IN : null
Arts
Physics
Maths
Your balance is: $1800
Enter your payment: $800
Thank you for your payment of $800
Your balance is: $1000

Name: Yogesh Kolte
Grade Level: 3
Student ID: 3 1001
Courses Enrolled: null
Arts
Physics
Maths
Balance: $1000
*/
