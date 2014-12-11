Feature: A simple subject that will be able to add, remove, and notify the
		 observers
		 
		 @add_observer
		 Scenario: Add observer
		 Given a subject, observer "usa_time_observer" and "eu_time_observer"
		 And observer "usa_time_observer" and "eu_time_observer" registers to subject
		 Then the subject notifies its observer
		 |message                                                |
		 |Observer usa_time_observer says: 2014-12-11 04:02:20PM |
         |Observer eu_time_observer says: 2014-12-11 04:02:22PM  |
		 