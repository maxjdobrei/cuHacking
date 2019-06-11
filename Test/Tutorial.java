package Test;

public class Tutorial extends Section
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