package com.springboot.employee.managment.exceptions;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value=HttpStatus.NOT_FOUND)
public class exception extends RuntimeException{
    public exception(String message){
        super(message);
    }
}
