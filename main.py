import NewtonRaphson
if __name__ == "__main__":
    def d(x): return x*x - 2*x - 5
    ans = NewtonRaphson.newtonRaphson(d, -4)
    print(ans)
