public class Main2 {
    public static void main(String[] args) {
        
        Mot word=new Mot(args[0]);

        if(word.verfication()){
            System.out.println("<"+args[0]+"> puissance "+args[1]+" :");
            System.out.println( word.puissance(Integer.parseInt(args[1])));
      
          }else{
           System.out.println( "error \nle mot n'ppartient pas au langage");
          }
      
    }
}
