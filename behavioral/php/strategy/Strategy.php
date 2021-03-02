<?php

interface SortStrategy
{
    public function sort(array $items): string;
}


class BubbleSortConcreteStrategy implements SortStrategy
{
    public function sort(array $items): string
    {
        return "Sorting with bubble sort!";
    }
}


class MergeSortConcreteStrategy implements SortStrategy
{
    public function sort(array $items): string
    {
        return "Sorting with merge sort!";
    }
}


class QuickSortConcreteStrategy implements SortStrategy
{
    public function sort(array $items): string
    {
        return "Sorting with quick sort!";
    }
}


class SortContext
{
    private $items;

    private $strategy;


    public function __construct(array $items, SortStrategy $strategy = null)
    {
        $this->items = $items;
        $this->strategy = $strategy;
    }


    public function sortContext()
    {
        if (isset($this->strategy)) {
            return $this->strategy->sort($this->items);
        }

        if (count($this->items) <= 100) {
            return (new BubbleSortConcreteStrategy())->sort($this->items);
        }

        if (count($this->items) <= 10000) {
            return (new MergeSortConcreteStrategy())->sort($this->items);
        }

        return (new QuickSortConcreteStrategy())->sort($this->items);
    }


    public function setStrategy(SortStrategy $strategy)
    {
        $this->strategy = $strategy;
    }
}