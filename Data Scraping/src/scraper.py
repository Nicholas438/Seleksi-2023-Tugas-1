# -*- coding: utf-8 -*-
"""scrapping_coursera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VUrzrnvtBcqlQ6OtaShGTbAuzlsttH9Z
"""

from bs4 import BeautifulSoup
import requests

# importing the required libraries for scrapping purpose.

response = requests.get("https://www.coursera.org/courses")
html_soup = BeautifulSoup(response.content, 'html.parser')

# we have set the url to scrap and using get method we send a request and then using html.parser we parsed the response content with help of scrapping library called beautiful soup.


url = html_soup.find_all(href=True)

#find all the URLs (items in the html where href exists)



def auto_Scrapper(html_tag,course_case):
  for i in range(1,20):
    url = "https://www.coursera.org/courses?page=" +str(i) + "&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for j in range(0,12):
      x = soup.find_all(html_tag)[j].get_text()
      course_case.append(x)
        
# the function auto_Scrapper is used to get two parameters that is the tag and what to scrap and get the content scrapped.      


def auto_Scrapper_Class(html_tag,course_case,tag_class,rating):

  for i in range(1,20):
    
    url = "https://www.coursera.org/courses?page=" +str(i) + "&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    passing = [[40,10],[54,2],[67,2],[72,5],[81,4],[83,6]]
    
    if rating == True:
        tabs = 12
        if i == 40 or i == 54 or i == 67 or i == 72 or i == 81 or i == 83:
           tabs = 11
        j = 0
        tab_num = 0
        while j < (tabs):
            
            if [i,tab_num] in passing:
                course_case.append(' ')
                print(' ',tab_num,i)
                tab_num += 1
            
            x = soup.find_all(html_tag, class_ = tag_class)[j].get_text()
            print(x,j,i)
            course_case.append(x)
            j += 1
            tab_num += 1
    else:
        for j in range(12):
            x = soup.find_all(html_tag, class_ = tag_class)[j].get_text()
            print(x,j,i)
            course_case.append(x)

def auto_Scrapper_Class_skip(html_tag,course_case,tag_class,num,learn):
  
  for i in range(1,20):
    url = "https://www.coursera.org/courses?page=" +str(i) + "&index=prod_all_products_term_optimization"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    passing = [[6,25],[6,29],[9,5],[16,5],[16,9],[20,9],[20,17],[20,45],[22,13],[24, 37],[26,13],[26,45],[27,37],[28,45],
               [29,25],[29,45],[31,5],[32,21],[35,17],[35,33],[36,17],[38,5],[38,6],[38,25],[38,41],[39,33],[40,21], [41,1],[41,33],[42,5],[42,17],[43,21],[43,45]
               ,[45,1],[46,9],[46,21],[49,17],[49,33],[49,41],[50,17],[50,6],[50,29],[50,37],[50,45],[51,17],[52,21],[53,25],[53,37],[53,45],[54,13],
               [55,1],[55,29],[56,1],[56,37],[56,41],[57,13],[57,33],[58,41],[59,5],[59,17],[59,21],[59,29],[60,29],[62,9],[62,13],[62,17],
               [63,41],[64,17],[64,37],[64,45],[65,5],[65,9],[66,9],[66,13],[66,21],[66,37],[67,9],[67,21],[67,34],[67,45],[68,5],[68,9],[68,13],[68,29],
               [69,13],[69,25],[69,29],[70,25],[71,13],[71,21],[71,23],[71,25],[71,29],[72,17],[73,29],[74,1],[74,37],[75,25],[75,37],[76,9],[76,33],[76,37],
               [77,5],[77,13],[77,17],[77,29],[77,37],[79,13],[79,37],[79,45],[80,21],[80,41],[81,1],[81,13],[81,15],[81,33],[81,41],[82,9],[82,37],[82,45],
               [83,5],[83,13],[83,26],[83,29],[83,33],[83,37]]
    add = [[22,27],[27,45],[30,1],[44,27]]
    tab_num = 0
    tabs = 48
    if i == 9 or i == 9  or i == 22 or i == 24  or i == 28 or i == 31 or i == 32  or i == 36 or i == 39 or i == 40 or i == 45 or i ==51 or i == 52 or i == 54 or i == 58 or i==60 or i==63 or i == 70 or i == 72 or i == 73:
        tabs = 47
    if i == 6 or i == 16 or i == 26 or i == 29 or i == 35 or i == 41 or i == 42 or i == 43 or i == 46 or i == 57 or i ==55 or i == 65 or i == 74 or i == 75 or i == 75 or i == 80:
        tabs = 46
    if i == 20  or i == 49  or i ==53 or i == 56 or i == 56 or i == 62 or i == 64  or i == 69 or i == 76 or i == 79 or i == 82:
       tabs = 45
    if i == 38  or i == 59 or i ==66  or i == 67 or i == 68 or i == 68:
       tabs = 44
    if i == 71 or i == 50 or i ==77 or i == 81 :
       tabs = 43
    if i == 83:
      tabs = 42
    if i == 30:
       tabs = 49

    j = 0
    while j < (tabs):
        if [i,j] in add:
           pass
        else:
            if [i,tab_num] in passing:
                if tab_num%4 == num:
                    print(" ",tab_num,i)
                    course_case.append(' ')
                tab_num += 1
                
            else:
                    
                
                


                x = soup.find_all(html_tag, class_ = tag_class)[j].get_text()

                if tab_num%4 == num:
                    print(x, tab_num, i)
                    course_case.append(x)
            tab_num += 1
        j += 1
        
            
            
            
        
# the function auto_Scrapper_Class is used to get three parameters that is the tag,what to scrap and get the content scrapped and class it belongs. 

course_title = []
course_organization = []
course_rating = []
course_learn = []
course_difficulty = []
num_rev = []

# making an empty list so that we can append each of them at the end into a list for making dataframe.



auto_Scrapper_Class_skip('p',course_learn,'css-vac8rf',1,True)
#auto_Scrapper_Class_skip('p',num_rev,'css-vac8rf',2,True)
auto_Scrapper_Class_skip('p',course_difficulty,'css-vac8rf',3,True)

auto_Scrapper_Class('p',course_rating,'css-2xargn',True)
auto_Scrapper_Class('h3',course_title,'cds-CommonCard-title',False)
auto_Scrapper_Class('p',course_organization,'cds-ProductCard-partnerNames',False)



# here we are creating the lists of all data required and appending them to list.
import pandas as pd
courses_df = pd.DataFrame({#'course_title': course_title,
                          #'course_organization': course_organization,
                          #'course_rating': course_rating,
                          'course_learn':course_learn,
                            'course_difficulty':course_difficulty,

                           })


# here we take each lists we generated by scrapping and made a dataframe out of it isung pandas library.


courses_df.to_csv('UCoursera_skills.csv')


courses_df = pd.DataFrame({'course_title': course_title,
                          'course_organization': course_organization,
                          'course_rating': course_rating,
                          #'course_learn':course_learn,
                          #  'course_difficulty':course_difficulty,

                           })


# here we take each lists we generated by scrapping and made a dataframe out of it isung pandas library.


courses_df.to_csv('UCoursera_courses.csv')
# At end we convert it into a csv file so we can use it for our data analysis part.