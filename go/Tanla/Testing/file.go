package main

import (
	"fmt"
	"time"
	"sync"
	"context"
	// "errors"
	// "strings"
	// "strconv"
	// "sort"
)






func main(){
	var wg sync.WaitGroup
	ch := make(chan string,1)

	wg.Add(1)
	go func(){
		defer wg.Done()
		time.Sleep(2*time.Second)
		ch <- "task"
	}()
	select{
		case val := <-ch:
			fmt.Println("channe",val)
		case <- time.After(1*time.Second):
			fmt.Println("Timer")
	}
	wg.Wait()
	var mymap map[string]bool
	mymap = make(map[string]bool)
	mymap["a"] = true
	mymap["b"] = false
	fmt.Println(mymap["b"])
	for key,value := range mymap{
		fmt.Println(key,"-",value)
	}
}


