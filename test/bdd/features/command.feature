Feature: An app that emulates unix commands 
		 using a command design pattern
		 
		 @command
		 Scenario: Perform ls, touch and rm
		 Given I have ls command and reciever
		 And I have reciever and command for rm and touch with name "test_file"
		 When I have create and delete file commands
		 Then I will call invoker class and call create_file
		 |message                                                                                                            |
		 |Creating file...                                                                                                   | 
         |Content of dir:  .pydevproject README.md coverage.xml .project .coverage .gitignore                       |
		 |Content of dir:  .pydevproject README.md coverage.xml .project .coverage .gitignore test_file                      |
		 |File created.                                                                                                      |
		 And then call delete_file from invoker class
		 |message                                                                                                            |
		 |Deleting file...                                                                                                   | 
         |Content of dir:  .pydevproject README.md coverage.xml .project .coverage .gitignore test_file                      |
		 |Content of dir:  .pydevproject .test_file README.md coverage.xml .project .coverage .gitignore                     |
		 |File deleted.                                                                                                      |
		 And then call undo_all from invoker class
		 |message           |
		 |Undo all...       |
         |Undo all finished.|
		 