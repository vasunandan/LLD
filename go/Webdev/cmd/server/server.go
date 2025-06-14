package main

import(
	"fmt"
	"Webdev/pkg/logger"
	"Webdev/internal/router"
)
func main(){
	logger.Log("Started server")
	r := router.Getrouter()
	r.Run(":8080")
}