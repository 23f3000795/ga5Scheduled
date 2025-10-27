# /// script
# dependencies = ["playwright"]
# ///
from playwright.sync_api import sync_playwright

def scrape_quotes():
    with sync_playwright() as p:
        # Channel is optional. Use "chrome", "msedge", "chrome-beta", "msedge-beta", "msedge-dev"
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        page.goto("https://sanand0.github.io/tdsdata/js_table/?seed=88")
        rows = page.query_selector_all("table tr")  # Assuming the table rows are in <tr> elements
        
        total_sum = 0  # Initialize a variable to store the sum
        
        # Iterate over each row
        for row in rows:
            # Get all cells in the row (assuming <td> for data cells)
            cells = row.query_selector_all("td")
            
            # Iterate through each cell in the row and sum the values
            for cell in cells:
                # Try to convert cell content to a number
                try:
                    cell_value = int(cell.inner_text().strip())
                    total_sum += cell_value  # Add the number to the total sum
                except ValueError:
                    # If the cell cannot be converted to a number, skip it
                    continue
        
        # Output the result
        print(f"Total sum of all numeric values: {total_sum}")
        
        # Optionally, save the result to a file
        with open("table_sum.txt", "a", encoding="utf-8") as file:
            file.write(f"Total sum of all numeric values: {total_sum}\n")
        
        browser.close()

if __name__ == "__main__":
    scrape_quotes()