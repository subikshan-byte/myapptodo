package com.springboot.employee.managment.controller;

import org.springframework.web.bind.annotation.RestController;

import com.springboot.employee.managment.entity.Employee;
import com.springboot.employee.managment.exceptions.exception;
import com.springboot.employee.managment.repository.userreopistory;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PutMapping;





@RestController
@RequestMapping("/user")
public class Employeecontroller {
    private userreopistory p;

    Employeecontroller(userreopistory p){
        this.p=p;
    }
    @GetMapping
    public List<Employee> getEmployees(){
        return p.findAll();
    }
    @PostMapping
    public Employee creatEmployee(@RequestBody Employee e){
        System.out.println(e);
        return  p.save(e);

    }
    @GetMapping("/{id}")
    public Employee getEmployeebyid(@PathVariable Long id) {
        return p.findById(id).orElseThrow(() -> new exception("user not found"+id));
    }
    @PutMapping("/{id}")
    public Employee updatEmployee(@PathVariable Long id,@RequestBody Employee e){
        Employee i=p.findById(id).orElseThrow(() -> new exception("user not found"+id));
        i.setEmail(e.getEmail());
        i.setFirstname(e.getFirstname());
        return p.save(e);
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<?> dEmployee(@PathVariable Long id) {
        Employee i=p.findById(id).orElseThrow(() -> new exception("user not found"+id));
    p.delete(i);
    return ResponseEntity.ok().build();
    }
    
    }
    

