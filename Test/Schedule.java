package Test;

public class Schedule
{
	protected Section[] courseLoad;
	protected boolean valid;
	protected double rating;


	public Schedule()
	{
		courseLoad = new Section[6];
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
	
		for (i = 0; i < existingLecs.size(); i++)
		{
			checkOverlapHelper(existingLecs.get(i), new ArrayList<Section>(existingLecs));
		}
	}
 

	//theres a fair amount of redundancy because of the days and other stuff but i think itll work
	public void checkOverlapHelper(Section model, ArrayList<Section> workList)
	{
		Integer startHourOne = new Integer();
		Integer startHourTwo = new Integer();
		Integer startMinueOne = new Integer();
		Integer startMinuteOne = new Integer();

		Integer endHourOne = new Integer();
		Integer endHourTwo = new Integer();
		Integer endMinueOne = new Integer();
		Integer endMinuteOne = new Integer();


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
							startHourOne = Integer.parseInt(model.getTime().charAt(0) + model.getTime().charAt(1));
							startHourTwo = Integer.parseInt(toBeCompared.getTime().charAt(0) + toBeCompared.getTime().charAt(1));

							endHourOne = Integer.parseInt(model.getTime().charAt(7) + model.getTime().charAt(8));
							endHourTwo = Integer.parseInt(toBeCompared.getTime().charAt(7) + toBeCompared.getTime().charAt(8));

							
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
								startMinuteOne = Integer.parseInt(model.getTime().charAt(3) + model.getTime().charAt(4));
								startMinuteTwo = Integer.parseInt(toBeCompared.getTime().charAt(3) + toBeCompared.getTime().charAt(4));
								
								endMinuteOne = Integer.parseInt(model.getTime().charAt(10) + model.getTime().charAt(11));
								endMinuteTwo = Integer.parseInt(toBeCompared.getTime().charAt(10) + toBeCompared.getTime().charAt(11));

								
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
		int comma = model.getDays().indexOf(",");
		if (comma != -1)
		{
			String dayOne = model.getDays().subString(0,comma);
			String dayTwo = moodel.getDays().subString(comma+1,model.getDays().length() + 1);
			days = new String[2];
			days[0] = dayOne;
			days[1] = dayTwo;
		}
		else
		{
			days = new String[1];
			days[0] = model.getDays();
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
			}
		}
	}

	public void removeSection(int index)
	{
		courseLoad[index] = null;
	}



}