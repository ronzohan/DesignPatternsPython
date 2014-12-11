Feature: Instantiate a huge object, RealSubject , which contains
		 10 million digits using proxy design pattern
		 		 

		 @create_multiple_proxy_instance
		 Scenario: Create multiple proxy instance 
		 Given I instatiated multiple proxy will have message
		 |message                 |
		 |Created new object      |
		 |Count of references =  1|
	 	 |Using cached object     |
		 |Count of references =  2|
		 |Using cached object     |
		 |Count of references =  3|
		 Then I will delete proxy 2 and will output
		 |message                              |
         |Deleted object. Count of objects =  2|
		 