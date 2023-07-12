**Problem 16:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.

db.Restaurants.createIndex({ id: 1 }, { unique: true, collation: { locale: "en", strength: 2 } })

db.Restaurants.createIndex({ name: 1 })

db.Restaurants.createIndex({ cuisine_type: 1 })

db.Restaurants.createIndex({ location: 1 })

db.Restaurants.createIndex({ average_rating: 1 })

db.Restaurants.createIndex({ delivery_available: 1 })


**Problem 17:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.

db.Restaurants.insertMany([
  {
    "id": 1,
    "name": "Restaurant A",
    "cuisine_type": "Italian",
    "location": "123 Main St",
    "average_rating": 4.2,
    "delivery_available": true
  },
  {
    "id": 2,
    "name": "Restaurant B",
    "cuisine_type": "Mexican",
    "location": "456 Elm St",
    "average_rating": 4.6,
    "delivery_available": false
  },
  {
    "id": 3,
    "name": "Restaurant C",
    "cuisine_type": "Indian",
    "location": "789 Oak St",
    "average_rating": 4.8,
    "delivery_available": true
  },
  {
    "id": 4,
    "name": "Restaurant D",
    "cuisine_type": "Chinese",
    "location": "321 Pine St",
    "average_rating": 3.9,
    "delivery_available": true
  },
  {
    "id": 5,
    "name": "Restaurant E",
    "cuisine_type": "American",
    "location": "654 Cedar St",
    "average_rating": 4.5,
    "delivery_available": false
  }
]);


**Problem 18:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.

   db.Restaurants.find().sort({ average_rating: -1 })

**Problem 19:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.

  db.Restaurants.find({
  delivery_available: true,
  average_rating: { $gt: 4 }
})


**Problem 20:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.

db.Restaurants.find({
  $or: [
    { cuisine_type: { $exists: false } },
    { cuisine_type: null }
  ]
})

  

**Problem 21:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.

db.Restaurants.countDocuments({
  delivery_available: true
});

**Problem 22:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.

  db.Restaurants.find({
  location: { $regex: /New York/i }
})


db.Restaurants.find({
  location: { $regex: /Cedar/i }
})


**Problem 23:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.
- 

db.Restaurants.aggregate([
  {
    $group: {
      _id: null,
      averageRating: { $avg: "$average_rating" }
    }
  }
])


**Problem 24:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.
- 
db.Restaurants.find().sort({ average_rating: -1 }).limit(5)


**Problem 25:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the restaurant with **`id`** 3.
- 

db.Restaurants.deleteOne({ id: 3 })
