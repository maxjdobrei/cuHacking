package Test;

public abstract class Lecture
{
	protected String courseCode;
	protected String meetingTimes;
	protected String meetingPlace;
	protected String meetingDays;

	public Lecture(String name, String time, String location, String[] days)
	{
		courseCode = name;
		meetingTimes = time;
		meetingPlace = location;
		meetingDays = days;
	}

	
	public String getName()
	{
		return this.courseCode;
	}

	public String getTime()
	{
		return this.meetingTimes;
	}

	public  String getLocation()
	{
		return this.meetingPlace;
	}
	
	public  String[] getDays()
	{
		return this.meetingDays;
	}
 

}