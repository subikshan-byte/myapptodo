package com.springboot.employee.managment.repository;


import org.springframework.data.jpa.repository.JpaRepository;

import com.springboot.employee.managment.entity.Employee;

public interface userreopistory extends JpaRepository<Employee,Long> {

}
