package observer

import (
	"io"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestAddObservers(t *testing.T) {
	var tests = []struct {
		testName  string
		observers []Observer
		want      int
	}{
		{
			testName: "add observer",
			observers: []Observer{
				newCustomer("test-customer-1"),
			},
			want: 1,
		},
		{
			testName: "add multiple observers",
			observers: []Observer{
				newCustomer("test-customer-2"),
				newCustomer("test-customer-3"),
				newCustomer("test-customer-4"),
				newCustomer("test-customer-5"),
			},
			want: 5,
		},
		{
			testName:  "add no observers",
			observers: []Observer{},
			want:      5,
		},
	}

	i := newItem("test-item")
	for _, tt := range tests {
		t.Run(tt.testName, func(t *testing.T) {
			got := i.addObservers(tt.observers...)
			if got != tt.want {
				t.Errorf("addObservers() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRemoveObserver(t *testing.T) {
	var tests = []struct {
		testName  string
		observers []Observer
		i         int
		j         int
		want      int
	}{
		{
			testName: "remove observer",
			observers: []Observer{
				newCustomer("test-customer-1"),
			},
			i:    0,
			j:    1,
			want: 0,
		},
		{
			testName: "remove multiple observers",
			observers: []Observer{
				newCustomer("test-customer-2"),
				newCustomer("test-customer-3"),
				newCustomer("test-customer-4"),
				newCustomer("test-customer-5"),
			},
			i:    0,
			j:    2,
			want: 2,
		},
		{
			testName: "remove no observers",
			observers: []Observer{
				newCustomer("test-customer-6"),
			},
			i:    -1,
			j:    -1,
			want: 3,
		},
	}

	i := newItem("test-item")
	for _, tt := range tests {
		t.Run(tt.testName, func(t *testing.T) {
			i.addObservers(tt.observers...)
			var got int
			if tt.i != -1 && tt.j != -1 {
				got = i.removeObservers(tt.observers[tt.i:tt.j]...)
			} else {
				got = i.removeObservers()
			}
			if got != tt.want {
				t.Errorf("removeObservers() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNotifyAll(t *testing.T) {
	shirtItem := newItem("Nike Shirt")

	observerFirst := &Customer{id: "abc@gmail.com"}
	observerSecond := &Customer{id: "xyz@gmail.com"}

	shirtItem.addObservers(observerFirst, observerSecond)

	shirtItem.updateAvailability()
	output := captureOutput(func() {
		shirtItem.updateAvailability()
	})

	assert.Contains(t, output, "Sending email to customer abc@gmail.com for item Nike Shirt")
	assert.Contains(t, output, "Sending email to customer xyz@gmail.com for item Nike Shirt")
}

func captureOutput(f func()) string {
	orig := os.Stdout
	r, w, _ := os.Pipe()
	os.Stdout = w
	f()
	os.Stdout = orig
	w.Close()
	out, _ := io.ReadAll(r)
	return string(out)
}
