class Player:
    def __init__(self, rank, fname, age, team, pos, gp, g, a, pts, pm, pim, ps, evg, ppg, shg, gwg, eva, ppa, sha, shots, sp, toi, atoi, blk, hit, fow, fol, fop, name):
        self.rank = rank
        self.fname = fname
        self.age = age
        self.team = team
        self.pos = pos
        self.gp = gp
        self.g = g
        self.a = a
        self.pts = pts
        self.pm = pm
        self.pim = pim
        self.ps = ps
        self.evg = evg
        self.ppg = ppg
        self.shg = shg
        self.gwg = gwg
        self.eva = eva
        self.ppa = ppa
        self.sha = sha
        self.shots = shots
        self.sp = sp
        self.toi = toi
        self.atoi = atoi
        self.blk = blk
        self.hit = hit
        self.fow = fow
        self.fol = fol
        self.fop = fop
        self.name = name

    def __str__(self):
        return f"Player: {self.name}, Team: {self.team}, Pos: {self.pos}, GP: {self.gp}, G: {self.g}, A: {self.a}, PTS: {self.pts}, +/-: {self.pm}, PIM: {self.pim}, PS: {self.ps}, EVG: {self.evg}, PPG: {self.ppg}, SHG: {self.shg}, GWG: {self.gwg}, EVA: {self.eva}, PPA: {self.ppa}, SHA: {self.sha}, Shots: {self.shots}, SP: {self.sp}, TOI: {self.toi}, ATOI: {self.atoi}, BLK: {self.blk}, HIT: {self.hit}, FOW: {self.fow}, FOL: {self.fol}, FOP: {self.fop}"