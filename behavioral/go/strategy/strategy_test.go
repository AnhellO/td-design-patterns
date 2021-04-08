package strategy_test

import (
	"testing"

	"github.com/AnhellO/td-design-patterns/behavioral/go/strategy"
	"github.com/brianvoe/gofakeit/v6"
)

func init() {
	gofakeit.Seed(1000)
}

func TestDefaults(t *testing.T) {
	tcases := []struct {
		items    []uint8
		expected string
	}{
		{
			make([]uint8, 100),
			"Ordenando con bubble sort!",
		},
		{
			make([]uint8, 10000),
			"Ordenando con merge sort!",
		},
		{
			make([]uint8, 100000),
			"Ordenando con quick sort!",
		},
	}

	for _, tc := range tcases {
		gofakeit.Slice(&tc.items)
		context := strategy.NewSortContext(tc.items, nil)
		got := context.SortContext()

		if got != tc.expected {
			t.Errorf("Expected %s, got %s", tc.expected, got)
		}
	}
}

func TestSpecificStrategy(t *testing.T) {
	tcases := []struct {
		st       strategy.SortStrategy
		expected string
	}{
		{
			&strategy.BubbleSortConcreteStrategy{},
			"Ordenando con bubble sort!",
		},
		{
			&strategy.MergeSortConcreteStrategy{},
			"Ordenando con merge sort!",
		},
		{
			&strategy.QuickSortConcreteStrategy{},
			"Ordenando con quick sort!",
		},
	}

	for _, tc := range tcases {
		context := strategy.NewSortContext([]uint8{1, 9, 8, 3, 55}, tc.st)
		got := context.SortContext()

		if got != tc.expected {
			t.Errorf("Expected %s, got %s", tc.expected, got)
		}
	}
}

func TestUpdatingStrategy(t *testing.T) {
	tcases := []struct {
		concreteStrategy1 strategy.SortStrategy
		concreteStrategy2 strategy.SortStrategy
		expected1         string
		expected2         string
	}{
		{
			&strategy.BubbleSortConcreteStrategy{},
			&strategy.MergeSortConcreteStrategy{},
			"Ordenando con bubble sort!",
			"Ordenando con merge sort!",
		},
	}

	for _, tc := range tcases {
		context := strategy.NewSortContext([]uint8{1, 9, 8, 3, 55}, tc.concreteStrategy1)
		got := context.SortContext()

		if got != tc.expected1 {
			t.Errorf("Expected %s, got %s", tc.expected1, got)
		}

		context.SetStrategy(tc.concreteStrategy2)
		got = context.SortContext()

		if got != tc.expected2 {
			t.Errorf("Expected %s, got %s", tc.expected2, got)
		}
	}
}
