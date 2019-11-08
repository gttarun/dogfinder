# DogFinder

## Challenges/Decisions

Having worked with Flask framework extensively in the past, I had some trouble adjusting back in Django. 

The project/app structure as well as Django's ORM is much easier to work with. However, I had some trouble with URL dispatching since Flask uses @classmethod decorators to reirect you to the right function/method instead of having a seperate file to manage the redirecting. Additionally, I had to rejog my memory about regex and input params while keeping in mind to support accepting JSON and returning the same as well.

The last challenge was the radius feature. Firstly, I had to do some research in order to understand how to use longitude/latitude as well as perfrom calculations with them. After digging in a little deeper I learned that the calculation will require using the spherical law of cosines due to the Earth being a 3 dimensional sphere object. (Earth is slightly ellipsoidal but using a spherical model the errors are less than 0.3% which is negligabe and thus for most use cases the spherical model will work just fine)

## API Use

### Return ALL dogs' location and details
* GET
	* /dogs

### Return a specific dog's location and details
* GET
	* /dogs/<dog_id>
* UPDATE
	* /dogs/<dog_id>
		* input: curl --header "Content-Type: application/json" --request PUT --data '{"lon":"30.379753", "lat":"-97.737992"}' http://127.0.0.1:8000/dogs/2/

### Return all dogs within a radius from a given longitude/latitude
* GET
	* /dogs/nearby
		* input: curl --header "Content-Type: application/json" --request GET --data '{"lon":"30.379753", "lat":"-97.737992", "radius":"10"}' http://127.0.0.1:8000/dogs/nearby/

### Return all parks location and details
* GET
	* /parks

### Return a specific park's location and details
* GET
	* /parks/<park_name>




