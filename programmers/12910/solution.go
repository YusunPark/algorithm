package main

import (
    "sort"
)

func solution(arr []int, divisor int) []int {
    var data []int

    for _, num := range arr {
        if num%divisor == 0 {
            index := sort.Search(len(data), func(i int) bool { return data[i] > num })
            data = append(data, num)
            copy(data[index+1:], data[index:])
            data[index] = num
        }
    }

    if data == nil {
        data = append(data, -1)
    }

    return data
}
