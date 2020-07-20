from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        bikes_page = requests.get("http://localhost:8000/bikes.html")
        soup_bikes = BeautifulSoup(bikes_page.content, 'html.parser')
        self._bikes = soup_bikes
        cars_page = requests.get("http://localhost:8000/cars.html")
        soup_cars = BeautifulSoup(cars_page.content, 'html.parser')
        self._cars = soup_cars
       
    # testing index.html
    def test_index_nav(self):
        assert self._index.find_all('nav')
        assert self._index.find('ul',{'class':'nav navbar-nav navbar-right'})
    def test_index_navbar(self):
        assert self._index.find('a',{'class':'navbar-brand'})
        assert self._index.find('button',{'data-target':'#navbarCollapse'})
        assert self._index.find('li',{'class':'dropdown'})
    def test_index_panels(self):
        site1= self._index.find('div',{'class':'row'})
        site2= site1.find('div',{'class':'col-lg-4'})
        site3= site2.find('div',{'class':'panel-heading'}) 
        a=0
        for site2 in site1.find('div',{'class':'col-lg-4'}):
            a=a+1
            print(a)
        assert a==3
        b=0
        for site3 in site1.find('div',{'class':'panel-heading'}):
            b=b+1
        assert b==3
        c=0
        for form in site1.find_all('form'):
            c=c+1
        assert c==3
    def test_column1(self):
        site1= self._index.find('div',{'class':'row'})
        site2=self._index.find('a',{'class':'btn btn-lg btn-success btn-block'})
        site3= site1.find('div',{'class':'panel-body'})    
        b=0
        for site3 in site1.find('div',{'class':'panel-body'}):
            b=b+1
        assert b==3
        c=0
        for site2 in self._index.find_all('a',{'class':'btn btn-lg btn-success btn-block'}):
            c=c+1
        assert c==3
    def test_footer(self):
        assert self._index.find('footer')
    def test_other_comp(self):
        assert self._index.find('input',{'placeholder':'Enter Pickup city'})
        assert self._index.find('input',{'placeholder':'Enter pickup date'})
        assert self._index.find('input',{'placeholder':'Enter Drop Date'})
        assert self._index.find('input',{'placeholder':'E-mail'})
        assert self._index.find('input',{'placeholder':'Password'})
        assert self._index.find('input',{'value':'Remember Me'})
        assert self._index.find('input',{'type':'checkbox'})
        assert self._index.find('input',{'type':'password'})
        assert self._index.find('')
        assert self._index.find('')
#bikes.html testing ...............................................................
    def test_bikes_nav(self):
        assert self._bikes.find_all('nav')
        assert self._bikes.find('ul',{'class':'nav navbar-nav navbar-right'})
    def test_bikes_navbar(self):
        assert self._bikes.find('a',{'class':'navbar-brand'})
        assert self._bikes.find('button',{'data-target':'#navbarCollapse'})
        assert self._bikes.find('li',{'class':'dropdown'})
        site1= self._bikes.find('div',{'class':'row'})
        a=0
        for site1 in self._bikes.find_all('div',{'class':'row'}):
            a=a+1
        assert a==4
        assert self._bikes.find('div',{'class':'col-lg-9 col-centered'})
        assert self._bikes.find('div',{'class':'panel-heading'})
        assert self._bikes.find('div',{'class':'panel-body'})
        assert self._bikes.find('form',{'class':'form form-inline'})
        assert self._bikes.find('input',{'placeholder':'Enter Pickup City'})
        assert self._bikes.find('input',{'placeholder':'Enter pickup Date'})
        assert self._bikes.find('input',{'placeholder':'Enter Drop Date'})
    def test_bikes_body(self):
        assert self._bikes.find('div',{'class':'col-lg-2'})
        assert self._bikes.find('div',{'class':'col-lg-9'})
        assert self._bikes.find('span',{'class':'pull-right'})
        site1 = self._bikes.find('div',{'class':'checkbox'})
        a=0
        for site1 in self._bikes.find_all('div',{'class':'checkbox'}):
            a=a+1
        assert a>=10
        assert self._bikes.find('div',{'class':'panel-heading'})
        site2=self._bikes.find('div',{'class':'col-lg-3'})

        b=0
        for site2 in self._bikes.find_all('div',{'class':'col-lg-3'}):
            b=b+1
        assert b>=8
        c=0
        for img in self._bikes.find_all('img'):
            c=c+1
        assert c>=8
        d=0
        for button in self._bikes.find_all('button'):
            d=d+1
        assert d>=9
    def test_bikes_footer(self):
        assert self._bikes.find_all('footer')
#cars.html testing.................................................................
    def test_cars_nav(self):
        assert self._cars.find_all('nav')
        assert self._cars.find('ul',{'class':'nav navbar-nav navbar-right'})
    def test_cars_navbar(self):
        assert self._cars.find('a',{'class':'navbar-brand'})
        assert self._cars.find('button',{'data-target':'#navbarCollapse'})
        assert self._cars.find('li',{'class':'dropdown'})
        site1= self._cars.find('div',{'class':'row'})
        a=0
        for site1 in self._cars.find_all('div',{'class':'row'}):
            a=a+1
        assert a==4
        assert self._cars.find('div',{'class':'col-lg-9 col-centered'})
        assert self._cars.find('div',{'class':'panel-heading'})
        assert self._cars.find('div',{'class':'panel-body'})
        assert self._cars.find('form',{'class':'form form-inline'})
        assert self._cars.find('input',{'placeholder':'Enter Pickup City'})
        assert self._cars.find('input',{'placeholder':'Enter pickup Date'})
        assert self._cars.find('input',{'placeholder':'Enter Drop Date'})
    def test_cars_body(self):
        assert self._cars.find('div',{'class':'col-lg-2'})
        assert self._cars.find('div',{'class':'col-lg-9'})
        assert self._cars.find('span',{'class':'pull-right'})
        site1 = self._cars.find('div',{'class':'checkbox'})
        a=0
        for site1 in self._cars.find_all('div',{'class':'checkbox'}):
            a=a+1
        assert a>=10
        assert self._cars.find('div',{'class':'panel-heading'})
        site2=self._cars.find('div',{'class':'col-lg-3'})

        b=0
        for site2 in self._cars.find_all('div',{'class':'col-lg-3'}):
            b=b+1
        assert b>=8
        c=0
        for img in self._cars.find_all('img'):
            c=c+1
        assert c>=8
        d=0
        for button in self._cars.find_all('button'):
            d=d+1
        assert d>=9
    def test_cars_footer(self):
        assert self._cars.find_all('footer')