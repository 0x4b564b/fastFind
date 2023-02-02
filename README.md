# fastFind
Find what you're searching for in seconds! Our Python script opens top search results from Google with a single command line argument. Plus, customize the number of tabs opened with the -t option. Effortlessly save time and stay organized with this innovative tool




# FastFind
A command-line tool that opens the first link of Google search results in the browser.




## Usage
python fastfind.py <search-query>
  
  
  
 
## Requirements
- Python 3.x
- webbrowser module

## How it works
FastFind uses the Google search API to retrieve the first link of the search results, and then opens it in the default web browser.

## Notes
- The API may return different results depending on the user's location and search history.
- FastFind only opens the first link of the search results.
  
  
  
  
## Example 
python fastfind.py cats playing piano -t 5
  
This opens the first 5 links of the Google search for "cats playing piano" in your default web browser. 
  
  
  

## Features 
- Quick and easy way to search for something on Google and open the results in your browser. 
- Option to specify the number of links you want to open. 
- Opens the results in your default web browser. 
  
  
  

## Tech Stack 
- Python 
- Requests library for making HTTP requests 
- BeautifulSoup for parsing HTML 
- Webbrowser library to open URLs in the default browser. 


 
  
  
