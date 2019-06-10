package Test;

public class Tutorial extends Lecture 
{
	protected String meetingPlace;
	
	public Tutorial(String name, String time, String location, String[] days)
	{
		super(name, time, location, days);
		this.meetingPlace = location;
	}

	@Override
	public String getLocation()
	{
		return this.meetingPlace;
	}







}