import roulette as r
import sys

def main():
    table_limit, strategy = sys.argv[1], sys.argv[2]
    r.main(int(table_limit), strategy)

if __name__ == '__main__':
    main()
