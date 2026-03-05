package org.example;

public class Square extends Shape{
    int side;

    public Square(int side){
        this.side = side;
    }

    @Override
    public float calculateArea() {
        return (float) side * side;
    }

    @Override
    public float calculatePerimeter() {
        return (float) 4 * side;
    }
}
