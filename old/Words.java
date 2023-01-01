class Words {


    // Méthode "leftrotate" qui fait la rotation de la chaîne de carectéres vers la gauche avec d positions
        public static String leftrotate(String word, int d) {

            String ans = word.substring(d) + word.substring(0, d);
            return ans; //retourner une chaine de carectéres
       }
    


//---------------------------------------------------------------------------------------------------------------
         
        // La méthode "printWords"  qui print toutes les chaînes possibles de longueur "length"
        // C'est principalement un wrapper sur la méthode récursive printWordsRec()
        public static void printWords(char[] set, int length) {

            int lng=length; //pour garder la valeur réelle de la longueur length avant les modifications
            printWordsRec(set, "", length,lng);
        }
         


//----------------------------------------------------------------------------------------------------------------
        // La méthode principale récursive "printWordsRec" static 
        //pour imprimer toutes les chaînes possibles de longueur lng
        public static void printWordsRec(char[] set, String word, int length, int lng) {
          
          //déclaration des charectéres fixes "abb";
          String abb = "abb";

            // Cas de base : length vaut 0, mot à imprimé
            if (length == 0) {   

               //ajout des carectéres fixes "abb"
                word = word + abb;

              //faire toute les rotations nécessaires du word en appelant la méthode leftrotate
              //puis imprimer word
                for(int j=0; j<=lng; j++)
                System.out.print(leftrotate(word, j)+"\n");
                
                return;
            }
         
            
            // Un par un, ajout de tous les caractères de l'ensemble {a,b} et appel récursive pour length égal à length-1
            for (int i = 0; i < 2; ++i) {
         
                // L'ajout de Caractère suivant de l'entrée 
                String newword = word + set[i];
                
                // Décrémenter la longueur lng; car nous avons ajouté un nouveau caractère
                printWordsRec(set, newword, length - 1, lng);
                // System.out.println("\n");
            }
            
        }

}

