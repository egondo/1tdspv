import java.util.Scanner;

public class TesteIndentacao {
    public static void main(String[] args){
        System.out.println("Ola mundo!");
        Scanner tec = new Scanner(System.in);
        String nome = tec.nextLine();
        System.out.println("Texto" + nome);
    }
}