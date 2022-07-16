def connection(url='http://www.google.com/', timeout=5):

	# --------------------------------- Checks Internet Connection -----------------

    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


if __name__ == "__main__":
	z = connection()