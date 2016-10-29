package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"image"
	"image/color"
	"image/png"
	"math"
	"os"
	"strings"

	"github.com/llgcode/draw2d/draw2dimg"
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
		Edge{X1: 0, Y1: 1, X2: 2, Y2: 2},
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
		E_LEFT, E_TOP, E_MIDDLE_H, E_BOTTOM,
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
		Edge{X1: 2, Y1: 1, X2: 2, Y2: 2},
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

const MAX_WIDTH = 600
const LINE_HEIGHT = 30

func getLetterEdges(ch string) []Edge {
	e, ok := LETTER_TO_EDGES[strings.ToUpper(ch)]
	if !ok {
		return nil
	}
	return e
}

func textToEdges() {
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

func normalizeEdge(e Edge) Edge {
	return Edge{
		X1: e.X1, X2: e.X2, Y1: 2 - e.Y1, Y2: 2 - e.Y2,
	}
}

func drawEdgeDots(m *image.RGBA, ee Edge, rollingX int, rollingY int, W_MULTIPLIER int) {
	//fmt.Println(e)
	e := normalizeEdge(ee)
	x1 := e.X1 * W_MULTIPLIER
	x2 := e.X2 * W_MULTIPLIER
	y1 := e.Y1 * W_MULTIPLIER
	y2 := e.Y2 * W_MULTIPLIER
	m.Set(rollingX+x1, rollingY+y1, color.RGBA{0, 0, 0, 255})
	m.Set(rollingX+x2, rollingY+y2, color.RGBA{0, 0, 0, 255})
}

func edgesToImageDots(letters []ResultElement) *image.RGBA {
	W_MULTIPLIER := 1
	L_WIDTH := W_MULTIPLIER*3 + 5
	w := len(letters) * L_WIDTH
	h := LINE_HEIGHT
	m := image.NewRGBA(image.Rect(0, 0, w, h))

	rollingY := 5
	rollingX := 0
	for _, l := range letters {
		for _, e := range l.Edges {
			drawEdgeDots(m, e, rollingX, rollingY, W_MULTIPLIER)
		}
		rollingX += L_WIDTH
	}

	var b bytes.Buffer
	png.Encode(&b, m)
	fmt.Println(b.String())

	return m
}

func drawEdgeLine(m *draw2dimg.GraphicContext, ee Edge, rollingX int, rollingY int, W_MULTIPLIER int) {
	//fmt.Println(e)
	e := normalizeEdge(ee)
	x1 := rollingX + e.X1*W_MULTIPLIER
	x2 := rollingX + e.X2*W_MULTIPLIER
	y1 := rollingY + e.Y1*W_MULTIPLIER
	y2 := rollingY + e.Y2*W_MULTIPLIER

	m.MoveTo(float64(x1), float64(y1))
	m.LineTo(float64(x2), float64(y2))
	m.Close()
	m.FillStroke()
}

func edgesToImageLines(letters []ResultElement) *image.RGBA {
	W_MULTIPLIER := 5
	L_WIDTH := W_MULTIPLIER*3 + 5

	totalw := len(letters) * L_WIDTH
	rows := int(math.Ceil(float64(totalw) / float64(MAX_WIDTH)))
	w := MAX_WIDTH

	h := LINE_HEIGHT * rows
	m := image.NewRGBA(image.Rect(0, 0, w, h))
	gc := draw2dimg.NewGraphicContext(m)

	// Set some properties
	gc.SetStrokeColor(color.RGBA{0x44, 0x44, 0x44, 0xff})
	gc.SetLineWidth(1)

	rollingY := 5
	rollingX := 5
	for _, l := range letters {
		for _, e := range l.Edges {
			drawEdgeLine(gc, e, rollingX, rollingY, W_MULTIPLIER)
		}
		rollingX += L_WIDTH
		if rollingX >= MAX_WIDTH {
			rollingY += LINE_HEIGHT
			rollingX = 5
		}
	}

	var b bytes.Buffer
	png.Encode(&b, m)
	fmt.Println(b.String())

	return m
}

func readEdges() []ResultElement {
	result := make([]ResultElement, 0)

	bio := bufio.NewReader(os.Stdin)
	sc := bufio.NewScanner(bio)
	for sc.Scan() {
		line := sc.Text()
		e := make([]ResultElement, 0)
		if err := json.Unmarshal([]byte(line), &e); err != nil {
			panic(err)
		}
		result = append(result, e...)
	}

	return result
}

type Point struct {
	X int `json:"x"`
	Y int `json:"y"`
}

func readEdgesPython() []ResultElement {
	var result [][]Point

	bio := bufio.NewReader(os.Stdin)
	sc := bufio.NewScanner(bio)
	for sc.Scan() {
		line := sc.Text()
		e := make([][]Point, 0)
		if err := json.Unmarshal([]byte(line), &e); err != nil {
			panic(err)
		}
		result = append(result, e...)
	}

	result2 := make([]ResultElement, 0)
	for _, arr := range result {
		re := ResultElement{
			Edges: make([]Edge, 0),
		}

		for i := 0; i < len(arr); i += 2 {
			re.Edges = append(re.Edges, Edge{
				X1: arr[i].X, Y1: arr[i].Y,
				X2: arr[i+1].X, Y2: arr[i+1].Y,
			})
		}

		result2 = append(result2, re)
	}
	return result2
}

func main() {
	textToEdgesF := flag.Bool("t2e", false, "Use to do text to edges transformation")
	edgesToImageF := flag.Bool("e2i", false, "Use to do edges to image transformation")
	edgesPythonToImageF := flag.Bool("ep2i", false, "Use to do python edges to image transformation")
	flag.Parse()

	if *textToEdgesF {
		textToEdges()
	} else if *edgesToImageF {
		edgesToImageLines(readEdges())
	} else if *edgesPythonToImageF {
		edgesToImageLines(readEdgesPython())
	}
}
