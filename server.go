package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
	"strings"
)

type StoryMessage struct {
	Message string `json:"message"`
}

func main() {
	http.HandleFunc("/api/story", func(w http.ResponseWriter, r *http.Request) {
		txt := r.FormValue("text")

		ioutil.WriteFile("my_plain_text.txt", []byte(txt), 0644)

		_, err := exec.Command("./generateStory.sh").Output()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}

		b, err := ioutil.ReadFile("story.json")
		if err != nil {
			panic(err)
		}

		var msgs []StoryMessage
		err = json.Unmarshal(b, &msgs)
		if err != nil {
			panic(err)
		}

		var buffer bytes.Buffer
		for _, m := range msgs {
			_, errr := buffer.WriteString(m.Message + "|")
			if errr != nil {
				panic(errr)
			}
		}

		fmt.Fprintf(w, "%v", buffer.String())
	})

	http.HandleFunc("/api/text", func(w http.ResponseWriter, r *http.Request) {
		story := r.FormValue("story")

		messages := make([]StoryMessage, 0)
		storyLines := strings.Split(story, "|")
		for _, s := range storyLines {
			messages = append(messages, StoryMessage{Message: s})
		}
		fmt.Println(len(storyLines))

		b, err := json.Marshal(messages)
		if err != nil {
			panic(err)
		}
		ioutil.WriteFile("story_dec.json", b, 0644)

		_, err = exec.Command("./decrypt_plain.sh").Output()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}

		// Read and return image
		b, err = ioutil.ReadFile("img.png")
		if err != nil {
			panic(err)
		}

		w.Write(b)
	})

	fs := http.FileServer(http.Dir("static"))
	http.Handle("/", fs)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
