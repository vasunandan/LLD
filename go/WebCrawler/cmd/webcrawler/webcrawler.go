package main

import (
	// "fmt"
	"WebCrawler/pkg/logging"
	"WebCrawler/pkg/helpers"
)

func main(){
	url_list := []string{"url1","url2"}
	logging.Log("Process started")
	helpers.StartProcess(url_list)
}
