import java.lang.*;
import java.util.Scanner;

class College
{
	protected String college_name;
	
	College()
	{
		college_name=" ";
	}
	College(String cname)
	{
		college_name=cname;
	}
	public String getcname()
	{
		return college_name;
	}
	public void setcname(String cname)
	{
		this.college_name=cname;
	}
}
class Student extends College
{
	private String Student_name;
	private String unique_id;
	private String program;
	
	Student()
	{
		Student_name=" ";
		unique_id=" ";
		program=" ";
	}
	Student(String Sname,String Uid,String pro)
	{
		Student_name=Sname;
		unique_id=Uid;
		program=pro;
	}
	//getter
	public String getSname()
	{
		return Student_name;
	}
	public String getUid()
	{
		return unique_id;
	}
	public String getpro()
	{
		return program;
	}
	//setter
	public void setSname(String Sname)
	{
		this.Student_name=Sname;
	}
	public void setUid(String Uid)
	{
		this.unique_id=Uid;
	}
	public void setpro(String pro)
	{
		this.program=pro;
	}
}
class Staff extends College
{
	private String Staff_name;
	private int StaffId;
	
	Staff()
	{
		Staff_name=" ";
		StaffId=0;
	}
	Staff(String Staffnme,int Sid)
	{
		Staff_name=Staffnme;
		StaffId=Sid;
	}
	//getter
		public String getStaffnme()
	{
		return Staff_name;
	}
	public int getSid()
	{
		return StaffId;
	}
	
	//setter
	
	public void setSid(int Sid)
	{
		this.StaffId=Sid;
	}
	public void setStaffnme(String Staffnme)
	{
		this.Staff_name=Staffnme;
	}
}

class InheritanceMainPrac
{
	public static void main (String args[])
	{
		Scanner sc=new Scanner(System.in);
		Student s1=new Student();
		System.out.println("____________________Fill Students information________________________");
		System.out.println("Enter college name : ");
		String cname=sc.next();
		System.out.println("Enter name of student: ");
		String Sname=sc.next();
		System.out.println("Enter Unique ID: ");
		String Uid=sc.next();
		System.out.println("Enter program of student: ");
		String pro=sc.next();
		s1.setcname(cname);
		s1.setSname(Sname);
		s1.setUid(Uid);
		s1.setpro(pro);
		
		//staff information
		
		Staff staff1=new Staff();
		System.out.println("______________________Fill Staff Information_______________________");
		System.out.println("Enter college name : ");
		cname=sc.next();
		System.out.println("Enter name of staff: ");
		String Staffnme=sc.next();
		System.out.println("Enter Unique ID: ");
		int Sid=sc.nextInt();
		staff1.setcname(cname);
		staff1.setStaffnme(Staffnme);
		staff1.setSid(Sid);
		
		System.out.println("_________________Student Information______________________");
		System.out.println("College name : "+s1.getcname());
		System.out.println("Name of student: "+s1.getSname());
		System.out.println("Unique ID: "+s1.getUid());
		System.out.println("program of student: "+s1.getpro());
		System.out.println("______________________________________________________________");
		
		
		System.out.println("_________________Display Staff Information______________________");
		System.out.println("College name : "+staff1.getcname());
		System.out.println("Name of student: "+staff1.getStaffnme());
		System.out.println("Staff ID: "+staff1.getSid());
		System.out.println("___________________________________________________________");
	}
}