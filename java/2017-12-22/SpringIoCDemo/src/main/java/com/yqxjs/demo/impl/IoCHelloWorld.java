package com.yqxjs.demo.impl;

import com.yqxjs.demo.api.HelloWorld;

public class IoCHelloWorld implements HelloWorld {
    @Override
    public void sayHello() {
        System.out.println("Spring Hello World!");
    }
}
