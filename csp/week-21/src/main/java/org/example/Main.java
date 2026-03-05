package org.example;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();

        Square square = new Square(5);
        System.out.println(square.calculateArea());
        System.out.println(square.calculatePerimeter());

    }
}