from emoji import emojize
def main():
    x = input("Input: ").strip()
    print("Output:", emojize(x, language='alias'))





if __name__ == "__main__":
	main()