"""
Hello, this program is a simple represantation of genetics algorithm in python.
"""


from fuzzywuzzy import fuzz
import random
import string


class Agent:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.letters) for _ in xrange(length))  # generates random string
        self.fitness = -1  # giving the starting fitness to the agent (will be incremented later)

    def __str__(self):

        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness)


in_str = None  # input string (will be added in the main method)
in_str_len = None  # length of the input string
population = 20  # population of one generation
generations = 1000  # number of generations


def init_agents(population, length):

    return [Agent(length) for _ in xrange(population)]  # creating 20 Agents (1 generation)


def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str)  # for each agent calculates ratio(difference) between input string and randomly generated

    return agents


def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)  # sorting agents array by fitness
    print '\n'.join(map(str, agents))
    agents = agents[:4]  # selecting the most fitness agent

    return agents


def crossover(agents):  # takes the most fitness pairs of selected agents and and randomly recopmbines parts of them to generate the better child(better string)

    offspring = []

    for _ in xrange((population - len(agents)) / 2):

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)  # randomly choosing two agents
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)  # creating two new Agents
        split = random.randint(0, in_str_len)  # generating random int from 0 to lenth of input string
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]  # first part of the first parent plus second part of the second
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)  # adding two children to agents array

    return agents


def mutation(agents):  # with a 10% chance changes one letter of the agent.string

    for agent in agents:

        for idx, param in enumerate(agent.string):  # to char array, idx - counter, param - char

            if random.uniform(0.0, 1.0) <= 0.1:  # 10% chance

                agent.string = agent.string[0:idx] + random.choice(string.letters) + agent.string[idx + 1:in_str_len]  # changing one letter of the agent.string

    return agents


def ga():

    agents = init_agents(population, in_str_len)

    for generation in xrange(generations):

        print 'Generation: ' + str(generation)

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)

        if any(agent.fitness >= 90 for agent in agents):

            print 'Threshold met!'
            exit(0)


if __name__ == '__main__':

    in_str = ''  # place your string here
    in_str_len = len(in_str)
    ga()
