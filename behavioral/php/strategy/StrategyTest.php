<?php

declare(strict_types=1);

use PHPUnit\Framework\TestCase;

/**
 * Execute test class from the project directory with the following command:
 * './vendor/bin/phpunit --bootstrap behavioral/php/strategy/Strategy.php behavioral/php/strategy/StrategyTest.php'
 */
class StrategyTest extends TestCase
{
    /**
     * @dataProvider defaultsProvider
     */
    public function testDefaultStrategies(array $items, string $expected): void
    {
        $context = new SortContext($items);
        $this->assertEquals($context->sortContext(), $expected);
    }

    /**
     * @dataProvider specificsProvider
     */
    public function testConcreteStrategy(SortStrategy $concreteStrategy, string $expected): void
    {
        $context = new SortContext([1, 9, 8, 3, 55], $concreteStrategy);
        $this->assertEquals($context->sortContext(), $expected);
    }


    public function testUpdatingStrategy(): void
    {
        $strategyOne = new BubbleSortConcreteStrategy();
        $context = new SortContext([1, 9, 8, 3, 55], $strategyOne);
        $this->assertEquals($context->sortContext(), "Sorting with bubble sort!");
        
        $strategyTwo = new MergeSortConcreteStrategy();
        $context->setStrategy($strategyTwo);
        $this->assertEquals($context->sortContext(), "Sorting with merge sort!");
    }


    public function defaultsProvider(): array
    {
        return [
            [
                range(1, 100),
                "Sorting with bubble sort!"
            ],
            [
                range(1, 10000),
                "Sorting with merge sort!"
            ],
            [
                range(1, 100000),
                "Sorting with quick sort!"
            ],
        ];
    }


    public function specificsProvider(): array
    {
        return [
            [
                new BubbleSortConcreteStrategy([1, 9, 8, 3, 55]),
                "Sorting with bubble sort!"
            ],
            [
                new MergeSortConcreteStrategy([1, 9, 8, 3, 55]),
                "Sorting with merge sort!"
            ],
            [
                new QuickSortConcreteStrategy([1, 9, 8, 3, 55]),
                "Sorting with quick sort!"
            ]
        ];
    }
}