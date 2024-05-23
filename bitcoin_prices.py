name: Bitcoin

on: 
  schedule:
    - cron: "*/5 * * * *" 

jobs:
  write-prices:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      with:
        token: ${{ secrets.GITHUB_TOKEN }} 
        
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests

    - name: Run Python script
      run: |
        python bitcoin_prices.py

    - name: Commit changes
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Ensure the token is available
      run: |
        git config --global user.name 'johnclareacholonu'
        git config --global user.email 'johnclareacholonu@users.noreply.github.com'
        git add bitcoin_prices.csv
        git commit -m 'Update rbitcoin_prices.csv with new prices'
        git push https://x-access-token:${GITHUB_TOKEN}@github.com/${{ github.repository }}.git HEAD:${{ github.ref }}
