package observer

import "fmt"

type Item struct {
	observers map[string]Observer
	name      string
	inStock   bool
}

func newItem(name string) *Item {
	return &Item{
		observers: make(map[string]Observer),
		name:      name,
	}
}

func (i *Item) updateAvailability() {
	fmt.Printf("Item %s is now in stock\n", i.name)
	i.inStock = true
	i.notifyAll()
}

func (i *Item) addObservers(observers ...Observer) int {
	for _, observer := range observers {
		i.observers[observer.getID()] = observer
	}
	return len(i.observers)
}

func (i *Item) removeObservers(observers ...Observer) int {
	for _, observer := range observers {
		delete(i.observers, observer.getID())
	}
	return len(i.observers)
}

func (i *Item) notifyAll() {
	for _, observer := range i.observers {
		observer.update(i.name)
	}
}
