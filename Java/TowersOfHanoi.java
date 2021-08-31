public class TowersOfHanoi {

    public void move(int n,char from,char to,char intermediate)
    {
        if(n==1)
        {
            System.out.println("Moving Disc 1 from "+from+" to "+to);
        }
        else
        {
            move(n-1, from, intermediate, to);
            System.out.println("Moving Disc "+ n +" from "+from+" to "+to);
            move(n-1, intermediate, to, from);
        }

    }

    public static void main(String[] args) {
        TowersOfHanoi towersOfHanoi = new TowersOfHanoi();
        towersOfHanoi.move(3, 'A', 'B', 'C');
    }
    
}
