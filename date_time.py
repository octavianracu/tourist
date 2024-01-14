class Period:
    def __init__(self, start, end):
        if start < end:
            self.start = start
            self.end = end
        else:
            print("ERROR")
    def  __str__(self):
        start = str(start) 
        end = str(end)
        return  f"[{start}, {end}]"   # e.g. "[01.01.2021 .. 02.01.2021]"