package observer

type Observer interface {
	update(string)
	getID() string
}
