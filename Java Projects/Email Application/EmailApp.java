package emailapp;
import java.util.Scanner;

public class EmailApp 
{
	public static void main(String[] args) 
	{	// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter firstName: ");
		String fn = sc.next();
		System.out.println("*************************");
		System.out.print("Enter lastName: ");
		String ln = sc.next();
		Email em1 = new Email(fn,ln); 
		
		//em1.setAlternateEmail("y.kolte27@gmail.com");
		//System.out.println(em1.getAlternateEmail());

		//em1.setMailboxCapacity(100);
		//System.out.println(em1.getMailboxCapacity());
		
		//em1.changePassword("123456789");
		//System.out.println(em1.getPassword());	
		
		System.out.println(em1.showInfo());
		// when we write system.out.println(), it returns value.......
	}
}
/*
EMAIL CREATED: John  Smith
Enter the department
1 for Sales
2 for Development
3 for Accounting
0 for none
*/
