package Test;

public class Course
{
	
	protected String name;
	protected Section[] affiliatedSections;

	public Course(String courseCode, Section[] sections)
	{	
		name = courseCode;
		affiliatedSections = sections;
	}



}