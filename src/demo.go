/**
 * File: demo.go
 * Author: Ashish Mittal
 * Contact: (support@airavana.ai)
 * Copyright (c) 2020 - 2021 Airavana Inc.
 */

package main

type UserData struct {
	FirstName   string `json:"firstName"`
	LastName    string `json:"lastName"`
	PhoneNumber string `json:"phoneNumber"`
	SSN         string `json:"ssn"`
	Email       string `json:"email"`
}

func RouteHandler(data UserData) {
	//test code to get userData
}
