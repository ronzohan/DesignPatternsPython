Feature: Instantiate a huge object, RealSubject , which contains
		 10 million digits using proxy design pattern
		 		 

		 @create_multiple_proxy_instance
		 Scenario: Create multiple proxy instance 
		 Given I instatiated multiple proxy
		 |proxy |
		 |proxy1|
		 |proxy2|
		 |proxy3|
		 Then the proxy class will have "3" reference count
		 
		 @delete_proxy_instance
		 Scenario: Delete proxy instance 
		 Given I instatiated a proxy
		 And I delete that instance
		 Then the proxy class will now have "0" reference count