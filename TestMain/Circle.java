

public class Circle
{
	
	private double radius;
	private String color;
	
	/*
	* Constructor
	*/
	public Circle()
	{
		this.radius = 0.0;
		this.color = "clear";
	}

	/*
	* Constructor
	*/
	public Circle(double r, String c)
	{
		this.radius = r;
		this.color = c;
	}

	/*
	* getter for color pre: none post: color returned
	*/
	public String getColor()
	{
		return this.color;
	}

	/*
	* getter for rad pre: none post: radius returned
	*/
	public double getRadius()
	{
		return this.radius;
	}

	/*
	* getter for area pre: none post: area returned
	*/
	public double getArea()
	{
		return 3.14 * (this.radius*this.radius);
	}

	/*
	* getter for circumference pre: none post: circumference returned
	*/
	public getCircumference()
	{
		return 2 * 3.14 * this.radius;
	}

	/*
	* setter for color pre: none post: color set
	*/
	public void setColor(String c)
	{
		this.color = c;
	}
	
	/*
	* setter for color pre: none post: radius set
	*/
	public void setRadius(double r)
	{
		this.radius = r;
	}




	@Override
	public String toString()
	{
		return "Radius: " +this.radius + "\nArea: " +this.getArea() +"\nCircumference: " +this.getCircumference() +"\nColor: " +this.color;
	}



}

