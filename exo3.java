
public class exo3{
    
// compter le nombre de A 
public static int CompterA (String s)  {
    int cptA=0,  i =0;
        while((i<s.length()) && (Character.compare(s.charAt(i),'a')==0)) {
            cptA++;
            i++;

    }
    return cptA;
}    



//compter le nombre de B dans le mot entrer
public static int CompterB (String s)  {
    int cptB=0,  i =0;
        while((i < s.length())) {
            if((Character.compare(s.charAt(i),'b')==0)){
                cptB++;
            }
            i++;
    }
    return cptB;
}



//la verification des terminaux {a,b}
public static boolean verification(String s) {
	//si le mot entrer est differnet de a et b, on retourne faux car il doit appartenir à l'ensemble des terminaux a et b tout en le verifiant jusqu'à la fin
    for(int i=0; i<s.length(); i++) {
        if ((Character.compare(s.charAt(i),'a')!=0) && (Character.compare(s.charAt(i),'b')!=0)) {
            return false; //different de a et b
        }
    }
    return true; //le mot contient que des a et b
    
}



//Au cas du mot vide s-->epsilon
public static boolean MotVide(String s) {
    return (s.length()==0);
}



//fonction qui verifie les differentes conditions
public static void s(String s){
    if(!MotVide(s)) {
        if(!verification(s)) {
            System.out.println("Le mot \""+s+"\"\n \nn'appartient pas au langage \n");	
        }
        else if(CompterB(s)*2 <= CompterA(s)) {
            System.out.println("Le mot \""+s+"\"\n appartient au langage \n");
        }
        else {
            System.out.println("Le mot \""+s+"\"\n n'ppartient pas au langage \n");
        }
    }
    else {
        System.out.println("Le mot \""+s+"\"\n appartient au langage \n");
    }
    


}
    

    public static void main (String []  args){
    //   if (args.length > 0) {
    //     exo3.s(args[0]);
    //   }
      for (int i = 0; i < args.length; i++) {
        if (args.length > 0) {
            exo3.s(args[i]);
          }
      }
}
}