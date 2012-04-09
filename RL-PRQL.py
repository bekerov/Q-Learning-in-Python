#!/usr/bin/env python
import MDP
import Agent
import PRQLearning
import time
import sys
import pylab as pl

def main():
    filePath = sys.argv[1]
    myMDP = MDP.MDP()
    myMDP.carrega(filePath)

    myAgent = Agent.Agent(myMDP)
    
    alpha              = 0.05
    gamma              = 0.95
    epsilon            = 0.0
    epsilonIncrement   = 0.0005
    gammaPRQL          = 0.95
    tau                = 0.0
    deltaTau           = 0.05
    psi                = 1.0
    v                  = 0.95

    K                  = 20       # number of episodes
    H                  = 100      # number of steps
    numberOfExecutions = 1000
    
    Wacumulado = 0
    for i in range(numberOfExecutions):
        print 'Running experiment ' + str(i + 1) + ' of ' + str(numberOfExecutions)
        myPRQLearning = None
        myPRQLearning = PRQLearning.PRQLearning(myMDP,                               \
                                                myAgent,                             \
                                                alpha            = alpha,            \
                                                gamma            = gamma,            \
                                                epsilon          = epsilon,          \
                                                epsilonIncrement = epsilonIncrement, \
                                                K                = K,                \
                                                H                = H,                \
                                                gammaPRQL        = gammaPRQL,        \
                                                tau              = tau,              \
                                                deltaTau         = deltaTau,         \
                                                psi              = psi,              \
                                                v                = v,                \
                                                filePath         = filePath)
        W, Ws = myPRQLearning.execute()
        Wacumulado += pl.array(Ws)
        
    Ws = Wacumulado / numberOfExecutions
    
    myPRQLearning.myQLearning.obtainPolicy()
    myPRQLearning.myQLearning.printPolicy(filePath + 'policy.out')
    myPRQLearning.myQLearning.printQ(filePath + 'Q.out')

    f = open(filePath + 'parameters.out', 'w')
    f.write('alpha =            ' + str(alpha) + '\n')
    f.write('gamma =            ' + str(gamma) + '\n')
    f.write('epsilon =          ' + str(epsilon) + '\n')
    f.write('epsilonIncrement = ' + str(epsilonIncrement) + '\n')
    f.write('numberOfSteps =    ' + str(K) + '\n')
    f.close()

    f = open(filePath + 'w.out', 'w')
    for w in Ws:
        f.write(str(w) + '\n')
    f.close()

    #pl.plot(range(len(Ws)), Ws)
    #pl.show()
    
main()