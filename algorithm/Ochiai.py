from math import sqrt
from operator import itemgetter
class Ochiai:
    def rankBySuspiciousness(self, CoverageList):
        suspiciousness = []
        i = 1
        for statementCoverage in CoverageList:
            suspiciousness.append([i, self.getOchiai(statementCoverage)])
            i += 1
        suspiciousnessRank = sorted(suspiciousness, key=itemgetter(1), reverse=True)
        return suspiciousnessRank

    def getOchiai(self, statementCoverage):
        ncf = statementCoverage[0]
        ncs = statementCoverage[1]
        nuf = statementCoverage[2]
        nus = statementCoverage[3]
        nf = ncf + nuf
        ns = ncs + nus
        if nf!=0 and ncf+ncs!=0:
            return ncf / sqrt(nf*(ncf+ncs))
        else:
            return -1
