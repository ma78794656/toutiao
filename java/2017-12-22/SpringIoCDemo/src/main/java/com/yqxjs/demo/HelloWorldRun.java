package com.yqxjs.demo;

import com.yqxjs.demo.api.HelloWorld;
import com.yqxjs.demo.service.HelloWorldService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloWorldRun {
    public static void main(String[] args) {
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean.xml");
        HelloWorldService helloWorldService =
                (HelloWorldService) context.getBean("helloWorldService");
        HelloWorld helloWorld = helloWorldService.getHelloWorld();
        helloWorld.sayHello();
    }
}
