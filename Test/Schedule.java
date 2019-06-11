package Test;


import java.util.ArrayList;


public class Schedule
{
	protected Section[] courseLoad;
	protected boolean valid;
	protected double rating;


	public Schedule()
	{
		courseLoad = new Section[12]; //6 courses with the potential for each to have a tutorial
		valid = true;
		rating = 1.0;

	}

	public Schedule(Section[] lectures)
	{
		courseLoad = lectures;
		valid = true;
		rating = 1.0;

	}

	public double getRating()
	{
		return rating;
	}

	public boolean isValid()
	{
		return valid;
	}


	public void checkOverlap()
	{
		ArrayList<Section> existingLecs = new ArrayList<Section>();


		for (int i = 0; i < 6; i++)
		{
			if (courseLoad[i] != null)
			{
				existingLecs.add(courseLoad[i]);
			}
		}
	
		for (int i = 0; i < existingLecs.size(); i++)
		{
			checkOverlapHelper(existingLecs.get(i), new ArrayList<Section>(existingLecs));
		}
	}
 

	//theres a fair amount of redundancy because of the days and other stuff but i think itll work
	public void checkOverlapHelper(Section model, ArrayList<Section> workList)
	{
		Integer startHourOne;
		Integer startHourTwo;
		Integer startMinuteOne = null;
		Integer startMinuteTwo = null; 

		Integer endHourOne; 
		Integer endHourTwo; 
		Integer endMinuteOne = null; 
		Integer endMinuteTwo = null; 


		String[] modelDays = getRealDays(model);
	
		for (int i = 0; i < workList.size() && valid == true; i++)
		{
			if (model != workList.get(i))
			{
				Section toBeCompared = workList.get(i);
				
				
				String[] comparisonDays = getRealDays(toBeCompared);
				for (String day : modelDays)
				{
					if (valid == false)
					{
						break;
					}
					
					
					for (String otherDay : comparisonDays)
					{
						if (day.equals(otherDay))
						{
							
							
							
							startHourOne = Integer.parseInt(model.getTime().substring(0,2));
							startHourTwo = Integer.parseInt(toBeCompared.getTime().substring(0,2));

							endHourOne = Integer.parseInt(model.getTime().substring(7,9));
							endHourTwo = Integer.parseInt(toBeCompared.getTime().substring(7,9));

							
							//start or endtime is smack dab in the middle of the model lecture
							if ( (startHourTwo > startHourOne && startHourTwo < endHourOne) || (endHourTwo > startHourOne && endHourTwo < endHourOne) )
							{
								this.valid = false;
								break;
							}
							//otherwise we should start caring about the minutes
							else 
							{
								
								// all the timeslots will be formatted the same way, for ex; '10:30, 11:45'
								startMinuteOne = Integer.parseInt(model.getTime().substring(3,5));
								startMinuteTwo = Integer.parseInt(toBeCompared.getTime().substring(3,5));
								
								endMinuteOne = Integer.parseInt(model.getTime().substring(10));
								endMinuteTwo = Integer.parseInt(toBeCompared.getTime().substring(10));

								
								//the other invalid possibilities are if the start/end hours are the same and minutes needed to be compared to determine validity
								if (startHourOne == startHourTwo)
								{
									if (startMinuteOne < startMinuteTwo)
									{
										this.valid = false;
										break;
									}
								}
								else if (endHourOne == endHourTwo)
								{
									if (endMinuteOne > endMinuteTwo)
									{
										this.valid = false;
										break;
									}
								}
								else if (startHourOne == endHourTwo)
								{
									if (startMinuteOne < endMinuteTwo)
									{
										this.valid = false;
										break;
									}
								}
								else if (endHourOne == startHourTwo)
								{
									if (endMinuteOne > startMinuteTwo)
									{
										this.valid = false;
										break;
									}
								}
							}
						}
					}
				}
			}
		}
	}


	public String[] getRealDays(Section lecture)
	{
		String[] days;
		int comma = lecture.getDays().indexOf(",");
		if (comma != -1)
		{
			String dayOne = lecture.getDays().substring(0,comma);
			String dayTwo = lecture.getDays().substring(comma+1);
			days = new String[2];
			days[0] = dayOne;
			days[1] = dayTwo;
		}
		else
		{
			days = new String[1];
			days[0] = lecture.getDays();
		}

		return days;
	}

	public void setRating(double score)
	{
		rating = score;
	}

	public void addSection(Section temp)
	{
		for (int i = 0; i < 6; i++)
		{
			if (courseLoad[i] == null)
			{
				courseLoad[i] = temp;
				break;
			}
		}
	}

	public void removeSection(int index)
	{
		courseLoad[index] = null;
	}



}