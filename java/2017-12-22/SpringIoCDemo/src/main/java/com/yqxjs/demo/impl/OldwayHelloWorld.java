package com.yqxjs.demo.impl;

import com.yqxjs.demo.api.HelloWorld;

public class OldwayHelloWorld implements HelloWorld {
    @Override
    public void sayHello() {
        System.out.println("Struts Hello World!");
    }

}
