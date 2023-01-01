public class Mot {

  private String mot;

  /* constructeur */

  Mot(String mot) {
    this.mot = mot;
  }

  /* verifier si le mot appartient au language T* */
  boolean verfication() {

    for (int i = 0; i < this.mot.length(); i++) {

      if ((this.mot.charAt(i)) != 'a' & (this.mot.charAt(i)) != 'b' & (this.mot.charAt(i)) != 'c') {
        return false;
      }
    }
    return true;
  }

  /* Methode qui retourne le miroir d'un mot qui appartient au language */
  String miroir() {

    String miroir = "";

    for (int i = mot.length() - 1; i >= 0; i--) {
      miroir += this.mot.charAt(i);
    }

    return miroir;

  }

  /* Methode qui retourne une puissance n d'un mot qui appartient au language */
  String puissance(int n) {
    String word = "";
    if (n == 0) {
      return word;
    } else {
      for (int i = 0; i < n; i++) {
        word += this.mot;
      }
    }
    return word;
  }
}
