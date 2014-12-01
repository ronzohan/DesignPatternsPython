from lettuce import step
from Singleton.crawler import run_crawler
import os
from nose.tools import assert_equal


@step(u'Given I want to download all images in a website "([^"]*)"')
def given_i_want_to_download_all_images_in_a_website_group1(step, url):
    run_crawler(url)


@step(u'The crawler will put the pictures into the images folder')
def the_crawler_will_put_the_pictures_into_the_images_folder(step):
    pic_list = []
    for row in step.hashes:
        pic_list.append(row['imagename'].encode("utf-8"))

    # Sort the two list to check if the two lists are equal
    pic_list = sorted(pic_list)
    downloaded_pic_list = sorted(os.listdir(os.getcwd() + '/images'))

    assert_equal(pic_list, downloaded_pic_list)
