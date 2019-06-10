package Test;

public class testMain
{
	public static void main(String[] args)
	{
		
		
		Tutorial[] comp1406a1 = { new Tutorial("COMP1406A1", "10:05, 11:25", "Mackenzie Room 422", "Friday")};
		
		Section comp1406a = new Section("COMP1406A", "11:35, 12:55", "Azrieli Theatre room 101", "Tuesday, Thursday", comp1406a1);
		Section comp1406b = new Section("COMP1406B", "13:05, 14:25", "Azrieli Theatre room 102", "Monday, Wednesday");
		Section comp1406c = new Section("COMP1406C", "16:05, 17:25", "Azrieli Theatre room 302", "Wednesday, Friday");
		Section[] testSections = new Section[3];
		testSections[0] = comp1406a;
		testSections[1] = comp1406b;
		testSections[2] = comp1406c;
		
		
		Course comp1406 = new Course("COMP1406", testSections);

		
		Tutorial[] comp1805b1 = { new Tutorial("COMP1805B1", "10:05, 11:25", "Mackenzie Room 423", "Friday"), new Tutorial("COMP1805B2", "11:35, 12:55", "Mackenzie Room 4", "Thursday")};
	
		Section comp1805a = new Section("COMP1805A", "10:05, 11:35", "Azrieli Theatre room 102", "Tuesday, Thursday");
		Section comp1805b = new Section("COMP1805B", "13:05, 14:25", "Azrieli Theatre room 301", "Monday, Wednesday", comp1805b1);
		Section[] testSectionsTwo = new Section[2];
		testSectionsTwo[0] = comp1805a;
		testSectionsTwo[1] = comp1805b;
		
		Course comp1805 = new Course("COMP1805", testSectionsTwo);
	
	
	
	
	}
	
	
	
}