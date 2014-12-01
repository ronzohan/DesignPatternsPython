Feature: A crawler app that will get images from different websites

		Scenario: Download all images from a website
		Given I want to download all images in a website "http://localhost/pics.html"
		The crawler will put the pictures into the images folder
		|imagename  |
		|ron.jpg    |
		|kay.jpg    |
		|jennie.jpg |
		
		Scenario: Mistyped given url
		Given I want to download all images in a website "http://///localhost/pics.html"
		The crawler will put the pictures into the images folder
		|imagename  |
		|ron.jpg    |
		|kay.jpg    |
		|jennie.jpg |
		
		
		
		