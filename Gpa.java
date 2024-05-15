import java.util.*;
public class gpa
{
	public static void main(String[] args)
	{
		double grade=0,credits=0,semsum=0,semcredits=0,totalcredits=0,totalsum=0;
		int sem=0,sub=0;
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the number of semesters:");
		sem=sc.nextInt();
		for(int i=1;i<=sem;i++)
		{
			System.out.print("Enter the number of subjects for semester "+i+":");
			sub=sc.nextInt();
			for(int j=1;j<=sub;j++)
			{
				System.out.print("Enter the grade out of 10 for subject "+j+":");
				grade=sc.nextInt();
				System.out.print("Enter the credits of subject "+j+":");
				credits=sc.nextInt();
				semsum+=(grade*credits);
				semcredits+=credits;
			}
			double sgpa=(semsum/semcredits);
			System.out.println("Your GPA for semester "+i+" is:"+sgpa);
			totalcredits+=semcredits;
			totalsum+=semsum;
			semsum=0;
			semcredits=0;
		}
		double cgpa=(totalsum/totalcredits);
		System.out.println("Your overall CGPA for "+sem+" semesters is:"+cgpa);
	}
}