class Team:
    def __init__(self, rank, team, av_age, gp, wins, losses, ot_losses, points, pts_pct, goals_for, goals_against, shootout_wins, shootout_losses, srs, sos, goals_per_game, goals_against_per_game, powerplay_percent, powerplay_opportunities, powerplay_goals, powerplay_goals_against, penalty_kill_percent, shorthanded_goals, shorthanded_goals_against, penalties_per_game, opposing_penalties_per_game, shots_per_game, shooting_percent, shots_against_per_game, save_percent, shutouts, name):
        self.rank = rank
        self.team = team
        self.av_age = av_age
        self.gp = gp
        self.wins = wins
        self.losses = losses
        self.ot_losses = ot_losses
        self.points = points
        self.pts_pct = pts_pct
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.shootout_wins = shootout_wins
        self.shootout_losses = shootout_losses
        self.srs = srs
        self.sos = sos
        self.goals_per_game = goals_per_game
        self.goals_against_per_game = goals_against_per_game
        self.powerplay_percent = powerplay_percent
        self.powerplay_opportunities = powerplay_opportunities
        self.powerplay_goals = powerplay_goals
        self.powerplay_goals_against = powerplay_goals_against
        self.penalty_kill_percent = penalty_kill_percent
        self.shorthanded_goals = shorthanded_goals
        self.shorthanded_goals_against = shorthanded_goals_against
        self.penalties_per_game = penalties_per_game
        self.opposing_penalties_per_game = opposing_penalties_per_game
        self.shots_per_game = shots_per_game
        self.shooting_percent = shooting_percent
        self.shots_against_per_game = shots_against_per_game
        self.save_percent = save_percent
        self.shutouts = shutouts
        self.name = name
        
    def __repr__(self):
        return f"Team: {self.team}, GP: {self.gp}, W: {self.wins}, L: {self.losses}, OTL: {self.ot_losses}, PTS: {self.points}, GF: {self.goals_for}, GA: {self.goals_against}, PPG: {self.powerplay_goals}, PPO: {self.powerplay_opportunities}, PKP: {self.penalty_kill_percent}, SHG: {self.shorthanded_goals}, SHA: {self.shorthanded_goals_against}, PIM/G: {self.penalties_per_game}, SVP: {self.save_percent}, SO: {self.shutouts}"
