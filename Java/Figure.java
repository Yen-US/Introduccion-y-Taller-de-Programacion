package javaapplication4;

public class Figure {
        public void figura(int n){
            for (int i = 1; i<= n; i++){
                System.out.println(crearAsteriscos(i));
            }
	}

        public String crearAsteriscos(int n){
            String res = "";
		for (int i = 0; i < n; i++){
			res += "*";
                }
		return res;    
}
}