package strategy

type SortStrategy interface {
	Sort() string
}

type BubbleSortConcreteStrategy struct{}

func (b *BubbleSortConcreteStrategy) Sort() string {
	return "Ordenando con bubble sort!"
}

type MergeSortConcreteStrategy struct{}

func (m *MergeSortConcreteStrategy) Sort() string {
	return "Ordenando con merge sort!"
}

type QuickSortConcreteStrategy struct{}

func (q *QuickSortConcreteStrategy) Sort() string {
	return "Ordenando con quick sort!"
}

type SortContext struct {
	items    []uint8
	strategy SortStrategy
}

func NewSortContext(items []uint8, strategy SortStrategy) *SortContext {
	return &SortContext{
		items:    items,
		strategy: strategy,
	}
}

func (sc *SortContext) SortContext() string {
	if sc.strategy != nil {
		return sc.strategy.Sort()
	}

	if len(sc.items) <= 100 {
		return new(BubbleSortConcreteStrategy).Sort()
	}

	if len(sc.items) <= 10000 {
		return new(MergeSortConcreteStrategy).Sort()
	}

	return new(QuickSortConcreteStrategy).Sort()
}

func (sc *SortContext) SetStrategy(strategy SortStrategy) {
	sc.strategy = strategy
}
