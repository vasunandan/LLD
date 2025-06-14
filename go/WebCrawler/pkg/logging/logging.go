package logging

import (
	"fmt"
	"os"
	"log"
	"sync"
)

type Logger struct{
	mu sync.Mutex
	log *log.Logger
}

var logger *Logger

func init(){
	file,err := os.OpenFile("/Users/arruru.vasunandan/Documents/LLD/go/WebCrawler/pkg/logging/log.txt",os.O_CREATE|os.O_APPEND|os.O_WRONLY,0666)
	if err != nil{
		fmt.Println("Couldn't open log file ",err)
	}
	logger = &Logger{log:log.New(file,"",log.Ldate|log.Ltime),mu:sync.Mutex{}}
}

func Log(msg string){
	logger.mu.Lock()
	defer logger.mu.Unlock()
	if logger.log != nil{
		logger.log.Println(msg)
	}
}

