package observer

type Subject interface {
	addObservers(observers ...Observer) int
	removeObserver(observer ...Observer) int
	notifyAll()
}
