class Animal{
    public String name;
    public double speedKph;
    public double activityMultiplier = 1.2;
    public double weightKg;
    public double heightM;
    public boolean isPredator;

    public Animal(String name, double weightKg, double heightM, boolean isPredator, double speedKph){
        this.name = name;
        this.weightKg = weightKg;
        this.heightM = heightM;
        this.isPredator = isPredator;
        this.speedKph = speedKph;

    }

    public double getBmi(){
        return Math.floor(this.weightKg / Math.pow(this.heightM, 2) * 100) / 100;
    }

    public double getDailyCalories(){
        return Math.floor(70 * Math.pow(this.weightKg, 0.75) * activityMultiplier * 100) / 100;
    }


    public boolean isDangerous(){
        if(isPredator ||  this.speedKph >= 35 || this.heightM >= 170){
            return true;
    }
        else{
            return false;
    }
    }
}



class MyClass{
    public static void main(String[] args){
        Animal rabbit = new Animal("rabbit", 10, 0.3, false, 20);
        System.out.println(rabbit.getBmi());
        System.out.println(rabbit.isDangerous());

        Animal snake = new Animal("snake", 30, 1, true, 30);
        System.out.println(snake.isDangerous());
        System.out.println(snake.getDailyCalories());

        Animal elephant = new Animal("elephant", 300, 3, false, 5);
        System.out.println(elephant.getBmi());
        System.out.println(elephant.getDailyCalories());

        Animal gazelle = new Animal("gazelle", 50, 1.5, false, 100);
        System.out.println(gazelle.getDailyCalories());
        System.out.println(gazelle.isDangerous());

    }
}
