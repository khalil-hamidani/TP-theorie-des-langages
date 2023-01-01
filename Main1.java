public class Main1{

public static void main(String[] args) {

   Mot word1=new Mot(args[0]);
   
   if(word1.verfication()){
      System.out.println( "le miroire de \""+args[0]+"\" :\n"+word1.miroir());

    }else{
     System.out.println( "error \nle mot n'appartient pas au langage");
    }

}

}



