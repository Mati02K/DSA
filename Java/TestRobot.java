// This class is just for testing Robot.
// Note that this class has the same name as this file.
public class TestRobot {
    public static void main(String[] args) {
//        Robot robot1 = new Robot();
//        robot1.name = "Tom";
//        robot1.color = "red";
//        robot1.weight = 30;
//
//        Robot robot2 = new Robot();
//        robot2.name = "Jerry";
//        robot2.color = "blue";
//        robot2.weight = 40;

        Robot robot1 = new Robot("Tom", "red", 30);
        Robot robot2 = new Robot("Jerry", "blue", 40);

        robot1.introduceSelf();
        robot2.introduceSelf();

        float x = 2 % 1000;
        System.out.println(x);
    }
}



// This is the class we want to study.
class Robot {
    String name;
    String color;
    int weight;

    Robot(String givenName, String givenColor, int givenWeight) {
        this.name = givenName;
        this.color = givenColor;
        this.weight = givenWeight;
    }

    void introduceSelf() {
        System.out.println("My name is " + this.name);
    }
}