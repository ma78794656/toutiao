package com.yqxjs.demo.service;

import com.yqxjs.demo.api.HelloWorld;

public class HelloWorldService {
    private HelloWorld helloWorld;
    public void setHelloWorld(HelloWorld helloWorld) {
        this.helloWorld = helloWorld;
    }

    public HelloWorld getHelloWorld() {
        return helloWorld;
    }
}
