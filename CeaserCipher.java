import java.util.Scanner;

public class CeaserCipher {
    public static String ALPHABETS = "abcdefghijklmnopqrstuvwxyz 1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    static void encrypt(String PT,int key){
          int base = ALPHABETS.length();
          String output = "";
       for(int i=0; i<PT.length();i++)
       {
           int add = ALPHABETS.indexOf(PT.charAt(i));
           output += ALPHABETS.charAt( (add + key) % base );
       }
       
          System.out.println("The Encrypted text is : " + output);
        
      }
      static void decrypt(String CT,int key)
      {
          int base = ALPHABETS.length();
          String output = "";
       for(int i=0; i<CT.length();i++)
       {
           int sub = ALPHABETS.indexOf(CT.charAt(i));
           int value = sub - key;
          
           value = ( value < 0 )? (value + base)  : value;
           
           output += ALPHABETS.charAt(value % base);
       }
       
          System.out.println("The Decrypted text is : " + output);
      }
   
    public static void main(String[] args) {
        int choice , key;
        String PT , CT ;
        Scanner sc = new Scanner(System.in);
        
        do{
        System.out.println("Enter Your Choice:");
        System.out.println("1. Encryption");
        System.out.println("2. Decryption");
        System.out.println("3. Exit");
         
            choice = sc.nextInt();
            sc.nextLine();
          
            switch(choice){
                case 1:
                    System.out.println("Enter Your Plain Text:");
                    PT = sc.nextLine();
                    System.out.println("Enter Your Key between 0-25:");
                    key = sc.nextInt();
                    encrypt(PT, key);
                    break;
                case 2:
                     System.out.println("Enter Your Cipher Text:");
                    CT = sc.nextLine();
                    System.out.println("Enter Your Key between 0-25:");
                    key = sc.nextInt();
                    decrypt(CT, key);
                   
                    break;
                default:
                    break;
            }
        }while(choice != 3);  
    }
}