import java.util.*;
import java.lang.*;
class padma
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        
        int  e=sc.nextInt();
        int sum=0;
        while(e!=0)
        {
            int w=e%10;
            sum=sum+(w*w);
             e=e/10;
        }
            System.out.print(sum);
            
    }
}
