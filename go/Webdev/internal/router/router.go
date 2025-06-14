package router

import(
	"Webdev/pkg/logger"
	"github.com/gin-gonic/gin"
	"Webdev/internal/handlers"
)

type User struct{
	Name string `json:"name"`
	email string `json:"email"`
}


func Getrouter()*gin.Engine{
	r := gin.Default()
	v1 = r.Group("/v1"){
		v1.GET("/users",getuserhanlder)
	}
	return r
}
