# Kotlin for Interviews Cheatsheet

## Common Data Types

### MutableList

#### Initialization

```kotlin
// Create an empty MutableList
val list1 = mutableListOf<Int>()

// Create a MutableList with elements
val list2 = mutableListOf(1, 2, 3, 4)
```

#### Using MutableList as a Stack

```kotlin
val stack: MutableList<Int> = mutableListOf()
stack.add(1)
stack.add(2)

println(stack.last()) // returns 2
println(stack.removeLast()) // returns 2
println(stack.removeLast()) // returns 1
```

#### Using MutableList as a Queue

```kotlin
val queue: MutableList<Int> = mutableListOf()
queue.add(1)
queue.add(2)

println(queue.first()) // returns 1
println(queue.removeFirst()) // returns 1
println(queue.removeFirst()) // returns 2
```

### Array

#### Initialization

```kotlin
// Create an array of size 3 initialized to 0
val array1 = Array(3) { 0 }

// Create an array with specific values
val array2 = Array(5) { index -> 2 * index }
```

### HashMap

```kotlin
val map = hashMapOf("a" to 1, "b" to 2)
map["c"] = 3
println(map["a"]) // returns 1

map.getOrPut("d") { 4 }  // get current value of d or put new value 4
println(map["d"]) // returns 4
map.getOrPut("d") {4}

for ((key, value) in map.entries) {
    println("$key: $value")
}

```

### PriorityQueue

```kotlin
val pq = PriorityQueue<Int>()
pq.add(3)
pq.add(1)
pq.add(2)
println(pq.poll()) // returns 1

//custom comparator
val queue = PriorityQueue<IntArray> { p1, p2 ->  (p2[0].toDouble().pow(2)+p2[1].toDouble().pow(2)).compareTo(p1[0].toDouble().pow(2)+p1[1].toDouble().pow(2))}

```

---

## Print array

```kotlin
    print(array.contentToString())
```

## Pair in Kotlin

```kotlin
val pair1 = Pair("John", 30)
val pair2 = "John" to 30

print(pair1.first)
print(pair1.second)

fun getNameAndAge(): Pair<String, Int> {
    return "John" to 30
}

val (name, age) = getNameAndAge()
```

---

## Bitwise operators in Kotlin

```kotlin
 a and b = a.and(b)
 a or b = a.or(b)
 a xor b = a.xor(b)
 a.inv() = a.inv()
 a shl b = a.shl(b)
 a shr b = a.shr(b)
 a ushr b = a.ushr(b)
```

---

## String manipulation

```kotlin
  s.substring(0,10) // substirng
  s.length or s.count() // length
```

---

## Math

### Number Types

- `Int`: Whole numbers
- `Long`: Large whole numbers
- `Float`: Floating point numbers (32-bit)
- `Double`: Floating point numbers (64-bit)

### Useful Functions

```kotlin
println(abs(-5)) // returns 5
println(max(3, 7)) // returns 7
println(min(3, 7)) // returns 3
println(round(2.7)) // returns 3.0
```

### Useful Constants

```kotlin
println(Int.MAX_VALUE)
println(Double.MAX_VALUE)
```

---

## Iteration

### 1D Arrays/Lists

```kotlin
for (element in list) {
    println(element)
}
```

### 2D Arrays/Lists

```kotlin
for (row in matrix) {
    for (element in row) {
        println(element)
    }
}
```

### Declare 2D array

```kotlin
cMatrix = Array(matrix.size) { IntArray(matrix[0].size) }
```

---

## Sorting and Collection Functions

### Sorting

```kotlin
list.sorted()
list.sort()
```

### Search and Find

```kotlin
println(list.first { it > 5 }) // Finds first element greater than 5
println(list.indexOf(3)) // Finds index of element 3
```

---

## List Custom Sort

```kotlin
val sortedCustom = people.sortedWith(Comparator { p1, p2 ->
    p1.age.compareTo(p2.age)
})
```
