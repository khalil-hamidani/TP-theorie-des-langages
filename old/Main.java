import java.util.Scanner;

public class Main{

    public static void main(String[] args) {

          /* Miroir */

        System.out.println("veuillez entre un mot qui appartient au language T* ={a, b, c}. pour avoir son miroir");
        Scanner Scn = new Scanner(System.in);
        String x =Scn.nextLine(); 
        

        Mot w =new Mot(x);
        
        if(w.verfication()){
          System.out.println(" le miroir de mot '"+x+ "' est : ' \n" +w.miroir()); 

        }else{
         System.out.println( "le mot n'appartient pas au language");
        }

       

          /* puissance */

          System.out.println("veuillez entre un mot qui appartient au language T* ={a, b, c}.");
        Scanner Scn1 = new Scanner(System.in);
        String y =Scn1.nextLine(); 
        int n;

        
        
        Mot w1 =new Mot(y);

        if(w1.verfication()){
            
          System.out.println("veuillez entre la puissance  :");
          Scanner scn2 =new Scanner(System.in); 
           n=scn2.nextInt();
           scn2.close();
          System.out.println("la puissance "+n+" de mot '"+y+ "' est : \n'" +w1.puissance(n)+"'");

        }else{
         System.out.println( "le mot n'appartient pas au language");
        }

        


    }


}