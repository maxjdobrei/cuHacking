package Test;

public class Section extends Lecture
{
	
	protected Tutorial[] affiliatedTutorials;
	
	public Section(String name, String time, String location, String[] days, Tutorial[] tutorials)
	{
		super(name, time, location, days);
		affiliatedTutorials = tutorials;
	
	}

	public Section(String name, String time, String location, String[] days)
	{
		super(name, time, location, days);
		affiliatedTutorials = null;
	
	}











}