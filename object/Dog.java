class Dog {
    public String name;
    public int size;
    public int age;

    public Dog(String name, int size, int age) {
        this.name = name;
        this.size = size;
        this.age = age;
    }

    public String bark() {
        if (this.size >= 50) {
            return "Wooof! Woof!";
        } else if (this.size >= 20) {
            return "Ruff! Ruff!";
        } else {
            return "Yip! Yip!";
        }
    }

    public int calcHumanAge() {
        return 12 + (this.age - 1) * 7;
    }
}
