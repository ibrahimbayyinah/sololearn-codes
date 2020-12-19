public class Program {
    public static void main(String[] args) {
        int value = 23,
        res = value % 6; // this shows that indendation doesn't matter in Java
        double a = 15 / 4;
        double b = 15;
        int c = 4;
        double e = b / c;
        double f = 15. / 4;

        System.out.println(b); // prints 15.0
        System.out.println(res); // prints 5
        System.out.println(a); // will print 3.00 and not 3.75 because both of the operands are ints
        System.out.println(e); // will print 3.75 because at least one operand is a double
        System.out.println(f); // prints 3.75
        
        
        String city = "Pisa";
        int postalCode = 56100;
        System.out.println(city + postalCode);
        
        
        int test = 5;
        ++test;
        System.out.println(test+1);
        System.out.println(test);
        System.out.println(++test);
        System.out.println(test++); // this prints first and then increments
        System.out.println(test);
    }
}
