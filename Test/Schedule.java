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






	}

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
	
		for (int i = 0; i < workList.size(); i++)
		{
			if (model != workList.get(i))
			{
				Section toBeCompared = workList.get(i);
				
				
				
				String[] comparisonDays = getRealDays(toBeCompared);
				for (String day : modelDays)
				{
					
					
					
					for (String otherDay : comparisonDays)
					{
						if (day.equals(otherDay))
						{
							startHourOne = Integer.parseInt(model.getTime().charAt(0) + model.getTime().charAt(1));
							startHourTwo = Integer.parseInt(toBeCompared.getTime().charAt(0) + toBeCompared.getTime().charAt(1));

							endHourOne = Integer.parseInt(model.getTime().charAt(7) + model.getTime().charAt(8));
							endHourTwo = Integer.parseInt(toBeCompared.getTime().charAt(7) + toBeCompared.getTime().charAt(8));

							if ( (startHourTwo > startHourOne && startHourTwo < endHourOne) || (endHourTwo > startHourOne && endHourTwo < endHourOne) )
							{
								this.valid = false;
								break;
							}

							///////////////////////////////














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