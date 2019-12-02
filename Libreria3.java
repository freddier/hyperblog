/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package libreria3;
import java.sql.*;
import java.util.Scanner; 
/**
 *
 * @author RA
 */
public class Libreria3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
	/*Scanner sc = new Scanner(System.in);
        
        while(sc.hasNextInt()) {
            sc.next();
            System.out.println("No ingresaste una opción válida1");
            System.out.println("Intenta otra vez1");
        }
        
        String response = sc.next();
        System.out.println(response);*/
        System.out.println("asdf");
        new Libreria3();
        System.out.println("asdf");
    }
        
    public Libreria3() 
    {
        // Se mete todo en un try por los posibles errores de MySQL
        try
        {
            // Se registra el Driver de MySQL
            DriverManager.registerDriver(new com.mysql.jdbc.Driver());
            
            // Se obtiene una conexión con la base de datos. Hay que
            // cambiar el usuario "root" y la clave "la_clave" por las
            // adecuadas a la base de datos que estemos usando.
            Connection conexion = DriverManager.getConnection ( "jdbc:mysql://localhost/libreria","root", "");
            
            // Se crea un Statement, para realizar la consulta
            Statement s = conexion.createStatement();
            
            // Se realiza la consulta. Los resultados se guardan en el 
            // ResultSet rs
            ResultSet rs = s.executeQuery ("select * from escritor");
            
            // Se recorre el ResultSet, mostrando por pantalla los resultados.
            while (rs.next())
            {
                System.out.println (rs.getInt ("ESCRITOR") + " " + rs.getString (2));
            }
            
            // Se cierra la conexión con la base de datos.
            conexion.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    
    
}
