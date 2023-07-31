title: A short introduction to Data Modeling
date: 2023-07-31
summary: and tips that could be useful along the way.
category: data modeling
tags: data modeling
readTime: 13 min
author: Konstantinos Tsoumas

# A short introduction to Data Modeling.

<span style="font-size: 30px;">Setting the stage</span>

I've been thinking for quite some time : What should be the first blog post about? On side of me was saying that the first blog post is already out and it's the introduction while the other side was arguing that this is not so true.

So? What should it be about? The morning routine of Kim Kardashian or the hyperparameter tuning trick that will maximize your model's performance. Turns out, neither. Lately, I've been reading a lot of misconceptions about Data Modeling and Dimension Modeling so I would like to write a short introduction on defining what's what.

If you're new to data engineering, here's a landing paragraph:

Imagine you have a big box of toys, and you want to organize them in a way that makes sense. Data modeling is like that, but for computers and information! It's like creating a plan or a map for all the information a computer needs to understand.

You know how sometimes you have to follow certain rules while playing with your toys? Well, data modeling helps people and computers follow rules too. It makes things easier for everyone! When we use data modeling, we can see how different pieces of information are connected, just like how your toys might be related to each other. This approach also make things crazy more effiecient. Sounds fun, right?


### Data Modeling

As you begin to explore the world of databases and their design, you'll notice that this term pops up quite often, becoming a familiar part of your learning journey. If you are experienced on the field, you probably have seen this term more than you have seen the word 'Ketchup'. Which is okay.

First things first, what is a Data Modeling?

But why does this matter, you may wonder? Ah, well, this magical process bestows countless blessings upon the realm of stakeholders and developers alike.
    
Data Modeling is the very important process of conceptually creating (and later as a visual representation) of a data (or a complete information system) and its relationships. The objective is to structure the information of a system (or a whole system) in a meaningful way which will make the life of the stakeholders a lot easier. It would also make our lives way easier, as developers, as it will enhance the ease of our communication as well. Not to forget that it would be make things way more efficient and reduce errors.

Data models are built around business needs and they mature/evole along with them.

### Data model types

As you may already have guessed, there are a lot of data models. 
However, there are also three distinguishable types of data models. Let me explain with a supply chain example, to spice things up a bit.

Imagine you are working for a company that sells electronic products such as laptops and smartphones through their online store. The supply chain involes various stages including suppliers, warehouses, products, customers, and orders.

* Conceptual data model: As the name suggests, this type of models provide a high level overview of the data entities, their relationships and characteristics but also their constraints. They are part of the initial discussions and they answer questions such as "what business rules should we enforce?" or "how will we organize our data?".

Let's touch base with our example above. 

We have: 


| Entities                             | Entities           |
|--------------------------------------|--------------------|
| A Supplier supplies many Products    | Supplier           |
| A Warehouse stores many Products.    | Warehouse          |
| A Customer can place many Orders.    | Product            |
| An Order can include many Products.  | Customer           |
|                                      | Order              |


After a long discussion with our stakeholders, our first Conceptual data model could be brought to life: 


<pre>
       +------------+        +--------------+
       |  Supplier  |        |   Warehouse  |
       +------------+        +--------------+
             |                      |
             |                      |
             |                      |
       +-----+-------+       +------+------+
       |   Product  |       |   Customer  |
       +------------+       +------+------+
             |
             |
             |
       +-----+-------+
       |   Order    |
       +------------+

</pre>


* Logical data model: Coming to the second main data type, this kind provide less abstraction and is more detailed regarding the data and its relationships. We are now focusing more on identifying attributes, relationships and constraints. This model acts as a base for Physical data models, which is the third category, and it does not specify any technical system requirement. This is determined in the next data model. 
If you get into the designer's shoes, you may promptly wonder how helpful this is for normalization and optimization. 

Back to our lovely supply chain example, this translates to:

<span style="font-size: 30px;">Attributes:</span>

<span style="font-size: 20px;">Supplier Entity</span>

| Attribute    | Key       |
|--------------|-----------|
| supplier_id  | Primary   |
| name         |           |
| contact_info |           |

<span style="font-size: 20px;">Warehouse Entity</span>

| Attribute    | Key       |
|--------------|-----------|
| warehouse_id | Primary   |
| location     |           |
| capacity     |           |

<span style="font-size: 20px;">Product Entity</span>

| Attribute    | Key       |
|--------------|-----------|
| product_id   | Primary   |
| name         |           |
| description  |           |
| price        |           |

<span style="font-size: 20px;">Customer Entity</span>

| Attribute    | Key       |
|--------------|-----------|
| customer_id  | Primary   |
| name         |           |
| email        |           |
| address      |           |

<span style="font-size: 20px;">Order Entity</span>

| Attribute    | Key       |
|--------------|-----------|
| order_id     | Primary   |
| order_date   |           |
| total_amount |           |


<span style="font-size: 30px;">Relationships:</span>

* Supplier (supplier_id) 1 <-----> * Product (supplier_id)
* Warehouse (warehouse_id) 1 <-----> * Product (warehouse_id)
* Customer (customer_id) 1 <-----> * Order (customer_id)
* Order (order_id) 1 <-----> * Product (order_id)

* Physical data model: This kind specifically supply us with a detailed view of the physical data storage. This entails a finalized design that illustrates the relationships among entities defined above, data types and indices. All the technical requirements that the previous data model was missing so to say. To make this more meticulous, this type of model can also include a database management system's specific properties.

<span style="font-size: 20px;">Table: Supplier</span>

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| supplier_id    | INT       | Primary Key, Auto Increment |
| name           | VARCHAR   | Not Null                  |
| contact_info   | VARCHAR   |                           |

<span style="font-size: 20px;">Table: Warehouse</span>

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| warehouse_id   | INT       | Primary Key, Auto Increment |
| location       | VARCHAR   | Not Null                  |
| capacity       | INT       |                           |

<span style="font-size: 20px;">Table: Product</span>

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| product_id     | INT       | Primary Key, Auto Increment |
| name           | VARCHAR   | Not Null                  |
| description    | VARCHAR   |                           |
| price          | DECIMAL   |                           |

Table: Customer

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| customer_id    | INT       | Primary Key, Auto Increment |
| name           | VARCHAR   | Not Null                  |
| email          | VARCHAR   |                           |
| address        | VARCHAR   |                           |

Table: Order

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| order_id       | INT       | Primary Key, Auto Increment |
| order_date     | DATE      | Not Null                  |
| total_amount   | DECIMAL   |                           |

<span style="font-size: 20px;">Table: Order_Product (Many-to-Many Join Table)</span>

| Column         | Data Type | Constraints               |
|----------------|-----------|---------------------------|
| order_id       | INT       | Foreign Key (Order)       |
| product_id     | INT       | Foreign Key (Product)     |


### Think back

We saw a bit what data modeling is and what it entails. But take a moment and and think of the whole process before reaching the last stage. How would it look like?

Generally, the process of data modeling in 10 steps may look like:

<p> 1. <mark style="background-color: orange;">Purpose.</mark> Why do we need this? Remeber that we're building business processes that you expect to be <ins>generating data</ins> but also those that will be <ins>asking for data</ins>.</p>

<p> 2. <mark style="background-color: orange;">Requirement gathering.</mark> Understand the requirements and answer questions as : Do we have data? If yes, where? </p>

<p> 3. <mark style="background-color: orange;">Identify entities.</mark> Entities represent the major objects or concepts in the domain. Design the schema in a board, or with the old pen and paper. </p>

<p> 4. <mark style="background-color: orange;">Create a Conceptual Data Model aka CDM.</mark> Start writing down the queries that you expect you will be required to do. </p>

<p> 5. <mark style="background-color: orange;">Identify the properties per entity and its relationships.</mark> Relationships describe how the entities are related to each other. </p>

<p> 6. <mark style="background-color: orange;">Define the attributes.</mark> Attributes are the characteristics or data elements associated with each entity. </p>

<p> 7. <mark style="background-color: orange;">Use Normalization techniques.</mark> This is only for relationsal databases and out of this post's scope. </p>

<p> 8. <mark style="background-color: orange;">Create a Logical Data model aka LDM.</mark> It focuses on data consistency and integrity. Prototype and test (use a fake data generator to check for potential issues). </p>

<p> 9. <mark style="background-color: orange;">Assign Primary Keys and constraints.</mark> </p>

<p> 10. <mark style="background-color: orange;">Create a Physical Data model aka PDM.</mark> It's an LDM translation into the specific database management system's requirements. </p>

Now document, review, maintain. Remember that Data Modeling is an iterative process!

Note: You would probably see all the above data models represented in an [entity-relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model). I have tried to use my amazing hyphen-minus, pipe (vertical bar) skills for simplicity. 

### Tips learned the hard way on this Whimsical Journey

* Make sure you get your business requirements as detailed and clear as possible. Also, make sure you properly understand them.

* Review the dataset for intricate interdependencies. These could be in the form of hierarchies, like Country -> State -> City -> Neighborhood, or dynamic relationships like Product -> Supplier -> Manufacturer. Consider the most appropriate approach to represent these dependencies in a database - whether by using nested tables or implementing a recursive model.

* Be very careful about your [cardinality](https://en.wikipedia.org/wiki/Cardinality_%28data_modeling%29) and structure your schema with very solid foundations. On top of that, pay close attention to the datatypes you are choosing. 

* Test. Test. and then Test. Play around with [MVP](https://en.wikipedia.org/wiki/Minimum_viable_product). This includes modifying your data.

* Create your diagrams (i.e., entity-relationship diagrams) before you write **any code**. 

### Stuff that you may want to think about

* Why are OLTP and OLAP data models designed differently?

