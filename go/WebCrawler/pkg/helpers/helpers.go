package helpers

import(
	"fmt"
	"context"
	"time"
	"sync"
	"WebCrawler/pkg/logging"
)

func FetchHtmlFromUrl(url string)(string){
	return fmt.Sprintf("<HTML>%s<HTML>",url)
}

func FetchHtmlFromUrlWithTimeOut(c context.Context,url string){
	ch := make(chan string,1)
	go func(url string){
		time.Sleep(2*time.Second)
		ch <- FetchHtmlFromUrl(url)
	}(url)
	select{
	case val:=<-ch:
		fmt.Println(val)
	case <-c.Done():
		fmt.Println("Time out for",url)
	}
}

func HandleHTMLUrlJobs(jobs chan string){
	var wg sync.WaitGroup
	for url := range jobs{
		url := url
		wg.Add(1)
		go func(url string){
			defer wg.Done()
			ctx,cancel := context.WithTimeout(context.Background(),1*time.Second)
			defer cancel()
			FetchHtmlFromUrlWithTimeOut(ctx,url)
			
		}(url)
	}
	wg.Wait()
}

func StartProcess(urls []string){
	ch := make(chan string)
	var wg sync.WaitGroup
	for i:=0;i<5;i++{
		wg.Add(1)
		go func(ch chan string,wg *sync.WaitGroup){
			defer wg.Done()
			logging.Log("Sub process started")
			HandleHTMLUrlJobs(ch)	
		}(ch,&wg)
	}
	for _,url := range urls{
		ch <- url
	}
	close(ch)
	wg.Wait()
}