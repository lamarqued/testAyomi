# Test Ayomi

Technical test asked by Ayomi.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project being containerized with Docker, you'll require Docker in order to run it.

### Installing

In order to run the container, write the following command on a terminal :

```
docker-compose up
```

Once it's done, you can access it on your favorite browser at https://localhost:8000/

## Testing

### Test accounts

Two accounts are available on the application :
* **test** (username : test, password : testpassword), *user*
* **admin** (username : admin, password : adminpassword), *superuser*

### Routes

Three routes are available on the application :
* **/accounts/login**, login page
* **/index**, dashboard page where you can change your email address
* **/admin**, built-in django page to manage users

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - Used to ease CSS encoding
* [Docker](https://www.docker.com/) - Used to containerize the application

## Authors

**Denis LAMARQUE** - [Linkedin](https://www.linkedin.com/in/denis-lamarque-8b0534141/)
