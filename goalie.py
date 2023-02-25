class Goalie:
    def __init__(self, rank, fname, age, team, gp, gs, w, l, to, ga, sa, sv, svp, gaa, so, gps, minutes, qs, qsp, rbs, gap, gsaa, g, a, pts, pim, name):
        self.rank = rank
        self.first_name = fname
        self.age = age
        self.team = team
        self.gp = gp
        self.gs = gs
        self.w = w
        self.l = l
        self.to = to
        self.ga = ga
        self.sa = sa
        self.sv = sv
        self.svp = svp
        self.gaa = gaa
        self.so = so
        self.gps = gps
        self.minutes = minutes
        self.qs = qs
        self.qsp = qsp
        self.rbs = rbs
        self.gap = gap
        self.gsaa = gsaa
        self.g = g
        self.a = a
        self.pts = pts
        self.pim = pim
        self.name = name
        
    def __str__(self):
        return f"Goalie: {self.name}, Team: {self.team}, GP: {self.gp}, GS: {self.gs}, W: {self.w}, L: {self.l}, T/O: {self.to}, GA: {self.ga}, SA: {self.sa}, SV: {self.sv}, SVP: {self.svp}, GAA: {self.gaa}, SO: {self.so}, GPS: {self.gps}, MIN: {self.minutes}, QS: {self.qs}, QSP: {self.qsp}, RBS: {self.rbs}, GAP: {self.gap}, GSAA: {self.gsaa}, G: {self.g}, A: {self.a}, PTS: {self.pts}, PIM: {self.pim},"
