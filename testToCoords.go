package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"strings"
)

type Edge struct {
	X1 int `json:"x1"`
	Y1 int `json:"y1"`
	X2 int `json:"x2"`
	Y2 int `json:"y2"`
}

type ResultElement struct {
	Letter string `json:"letter"`
	Edges  []Edge `json:"edges"`
}

var E_TOP = Edge{X1: 0, Y1: 2, X2: 2, Y2: 2}
var E_BOTTOM = Edge{X1: 0, Y1: 0, X2: 2, Y2: 0}
var E_BOTTOM_LEFT = Edge{X1: 0, Y1: 0, X2: 1, Y2: 0}
var E_LEFT = Edge{X1: 0, Y1: 0, X2: 0, Y2: 2}
var E_RIGHT = Edge{X1: 2, Y1: 0, X2: 2, Y2: 2}
var E_MIDDLE_H = Edge{X1: 0, Y1: 1, X2: 2, Y2: 1}
var E_MIDDLE_V = Edge{X1: 1, Y1: 0, X2: 1, Y2: 2}

var LETTER_TO_EDGES map[string][]Edge = map[string][]Edge{
	"A": []Edge{
		E_TOP,
		E_LEFT,
		E_RIGHT,
		E_MIDDLE_H,
	},
	"B": []Edge{
		E_TOP, E_LEFT, E_BOTTOM,
		Edge{X1: 2, Y1: 2, X2: 0, Y2: 1},
		Edge{X1: 0, Y1: 1, X2: 2, Y2: 0},
	},
	"C": []Edge{
		E_TOP, E_BOTTOM, E_LEFT,
	},
	"D": []Edge{
		E_LEFT,
		Edge{X1: 0, Y1: 2, X2: 2, Y2: 1},
		Edge{X1: 2, Y1: 1, X2: 0, Y2: 0},
	},
	"E": []Edge{
		E_LEFT, E_TOP, E_MIDDLE_V, E_BOTTOM,
	},
	"F": []Edge{
		E_LEFT, E_TOP, E_MIDDLE_H,
	},
	"G": []Edge{
		E_TOP, E_LEFT, E_BOTTOM, E_MIDDLE_H,
		Edge{X1: 2, Y1: 0, X2: 2, Y2: 1},
	},
	"H": []Edge{
		E_LEFT, E_RIGHT, E_MIDDLE_H,
	},
	"I": []Edge{
		E_TOP, E_BOTTOM, E_MIDDLE_V,
	},
	"J": []Edge{
		E_BOTTOM_LEFT, E_TOP, E_MIDDLE_V,
	},
	"K": []Edge{
		E_LEFT,
		Edge{X1: 0, Y1: 1, X2: 2, Y2: 2},
		Edge{X1: 0, Y1: 1, X2: 2, Y2: 0},
	},
	"L": []Edge{
		E_LEFT, E_BOTTOM,
	},
	"M": []Edge{
		E_LEFT,
		E_RIGHT,
		Edge{X1: 0, Y1: 2, X2: 1, Y2: 0},
		Edge{X1: 2, Y1: 2, X2: 1, Y2: 0},
	},
	"N": []Edge{
		E_LEFT,
		E_RIGHT,
		Edge{X1: 0, Y1: 2, X2: 2, Y2: 0},
	},
	"O": []Edge{
		E_LEFT, E_RIGHT, E_BOTTOM, E_TOP,
	},
	"P": []Edge{
		E_LEFT, E_TOP, E_MIDDLE_H,
		Edge{X1: 2, Y1: 2, X2: 2, Y2: 1},
	},
	"R": []Edge{
		E_LEFT,
		E_TOP,
		E_MIDDLE_H,
		Edge{X1: 0, Y1: 1, X2: 2, Y2: 0},
	},
	"S": []Edge{
		E_TOP,
		E_BOTTOM,
		E_MIDDLE_H,
		Edge{X1: 0, Y1: 1, X2: 0, Y2: 2},
		Edge{X1: 2, Y1: 0, X2: 2, Y2: 1},
	},
	"T": []Edge{
		E_TOP,
		E_MIDDLE_V,
	},
	"U": []Edge{
		E_LEFT,
		E_RIGHT,
		E_BOTTOM,
	},
	"V": []Edge{
		Edge{X1: 0, Y1: 2, X2: 1, Y2: 0},
		Edge{X1: 2, Y1: 2, X2: 1, Y2: 0},
	},
	"W": []Edge{
		E_LEFT,
		E_RIGHT,
		Edge{X1: 0, Y1: 0, X2: 1, Y2: 1},
		Edge{X1: 2, Y1: 0, X2: 1, Y2: 1},
	},
	"X": []Edge{
		Edge{X1: 0, Y1: 2, X2: 2, Y2: 0},
		Edge{X1: 2, Y1: 2, X2: 0, Y2: 0},
	},
	"Y": []Edge{
		Edge{X1: 0, Y1: 2, X2: 1, Y2: 1},
		Edge{X1: 2, Y1: 2, X2: 1, Y2: 1},
		Edge{X1: 1, Y1: 0, X2: 1, Y2: 1},
	},
	"Z": []Edge{
		Edge{X1: 0, Y1: 0, X2: 2, Y2: 2},
		E_TOP,
		E_BOTTOM,
	},
	" ": []Edge{
		E_MIDDLE_V, E_MIDDLE_H,
	},
}

func getLetterEdges(ch string) []Edge {
	e, ok := LETTER_TO_EDGES[strings.ToUpper(ch)]
	if !ok {
		return nil
	}
	return e
}

func textToPoints() {
	bio := bufio.NewReader(os.Stdin)
	sc := bufio.NewScanner(bio)

	for sc.Scan() {
		line := sc.Text()
		result := make([]ResultElement, 0)
		for _, c := range line {
			r := ResultElement{
				Letter: string(c),
				Edges:  getLetterEdges(string(c)),
			}
			result = append(result, r)
			//fmt.Println(i, string(c), getLetterEdges(string(c)))
		}

		b, err := json.Marshal(result)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(b))
	}
}

func edgesToImage() {

}

func main() {
	textToPointsF := flag.Bool("t2p", false, "Use to do text to edges transformation")
	edgesToImageF := flag.Bool("e2i", false, "Use to do edges to image transformation")
	flag.Parse()

	if *textToPointsF {
		textToPoints()
	} else if *edgesToImageF {
		edgesToImage()
	}
}
