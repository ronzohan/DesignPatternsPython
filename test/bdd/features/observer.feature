Feature: A simple subject that will be able to add, remove, and notify the
		 observers
		 
		 @add_observer
		 Scenario: Add observer
		 Given a subject
		 And a USA time observer "usa_time_observer" registers to subject
		 Then subject will have "1" observer
