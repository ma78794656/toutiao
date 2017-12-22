package com.yqxjs.test;

public class HelloWorldRun {
    public static void main(String[] args) {
        HelloWorldService helloWorldService = new HelloWorldService();
        HelloWorld helloWorld = helloWorldService.getHelloWorld();
        helloWorld.sayHello();
    }
}
class HelloWorldService {
    private HelloWorld helloWorld;
    HelloWorldService() {
        this.helloWorld = new OldwayHelloWorld();
    }

    HelloWorld getHelloWorld() {
        return helloWorld;
    }
}

class OldwayHelloWorld implements HelloWorld{
    @Override
    public void sayHello() {
        System.out.println("Old way say hello world!");
    }
}

class IoCHelloWorld implements HelloWorld {
    @Override
    public void sayHello() {
        System.out.println("Ioc way say hello world!");
    }
}

interface HelloWorld{
    void sayHello();
}
