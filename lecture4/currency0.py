import requests

def main():
    #https://api.fixer.io/latest?base=USD&symbols=EUR
    base = input("First Currency: ")
    other = input("Second Currency: ")

    # res=requests.get("http://data.fixer.io/api/latest?access_key=b3eea800a21b14c7e06903eaff07449a",
    # params={"base": base, "symbols": other})

    res=requests.get(f"http://data.fixer.io/api/convert?access_key=b3eea800a21b14c7e06903eaff07449a&from={base}&to={other}&amount=1")
    # print(res)
    if(res.status_code!=200):
        raise Exception("Error:API request unsuccessful")

    # print(res.status_code)
    try:
        data=res.json()
        print(data)
        rate=data['rates'][other]
        print(f"1 {base} is = {rate}")
    except:
        print("Either Currency code is wrong or  currency note found")

if __name__ == "__main__":
    main()
