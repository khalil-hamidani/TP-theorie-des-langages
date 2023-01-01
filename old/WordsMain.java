class WordsMain{



public static  void main(String[] args) {



  if (args.length >0){
	  

        if((Integer.parseInt(args[0])) >= 3) {
			
         int length;
		 length = (Integer.parseInt(args[0])) - 3;
         char[] set = {'a', 'b'};
        Words.printWords(set, length ); 
            
        }
		else   System.out.println("error");


  }

}
}