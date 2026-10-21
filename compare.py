from Bio import Align
from nw import needleman_wunsch
from sw import smith_waterman


def make_aligner(mode):
    aligner=Align.PairwiseAligner()
    aligner.mode=mode
    aligner.match_score=1
    aligner.mismatch_score= -1
    aligner.open_gap_score=-2
    aligner.extend_gap_score=-2
    return aligner

glob = make_aligner("global")
loc = make_aligner("local")

a, b = "GAT", "GT"
print("global  mine:", needleman_wunsch(a, b)[2], " biopython:", glob.score(a, b))
print("local   mine:", smith_waterman(a, b)[2], " biopython:", loc.score(a, b)) 