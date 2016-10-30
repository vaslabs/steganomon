package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os/exec"
)

type StoryMessage struct {
	Message string `json:"message"`
}

func main() {
	http.HandleFunc("/api/story", func(w http.ResponseWriter, r *http.Request) {

		b, err := ioutil.ReadAll(r.Body)
		txt := string(b)

		cmd := exec.Command("./generateStory.sh")
		stdin, err := cmd.StdinPipe()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}
		_, err = stdin.Write([]byte(txt))
		if err != nil {
			fmt.Println(err)
			panic(err)
		}
		stdin.Close()

		out, err := cmd.Output()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}
		/*
			var msgs []StoryMessage
			err = json.Unmarshal([]byte(out), &msgs)
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
		*/
		fmt.Fprintf(w, "%v", string(out))
	})

	http.HandleFunc("/api/text", func(w http.ResponseWriter, r *http.Request) {
		b, err := ioutil.ReadAll(r.Body)
		story := string(b)

		/*
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
		*/

		cmd := exec.Command("./decrypt_plain.sh")
		stdin, err := cmd.StdinPipe()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}
		_, err = stdin.Write([]byte(story))
		if err != nil {
			fmt.Println(err)
			panic(err)
		}
		stdin.Close()

		out, err := cmd.Output()
		if err != nil {
			fmt.Println(err)
			panic(err)
		}

		w.Write(out)

		/*
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
		*/
	})

	fs := http.FileServer(http.Dir("."))
	http.Handle("/", fs)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
