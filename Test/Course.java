package Test;

public class Course
{
	
	protected String name;
	protected Section[] affiliatedSections;
	protected boolean hasTutorial;


	public Course(String courseCode, Section[] sections)
	{	
		name = courseCode;
		affiliatedSections = sections;
	}

	public Section[] getSections()
	{
		return affiliatedSections;
	}


}