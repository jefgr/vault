# Session 1
Compare the following terms
- data
- knowledge
- information
- wisdom

# Session 2
> zie wpo1.pdf

1. For a robotic football player, develop a PEAS description of the task environment. 

| Agent                   | Performance measure   | Environment                                                                                                                                            | Actuators                                            | Sensors                                                                                                                                                                 |
| ----------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| robotic football player | Amount of matches won | Footballfield lines, scores, goals, teammates and opponents, ball (location, speed, possession), gametime, referees, weatherconditions, groundcoverage | limbs (arms and legs), head, speaker (communication) | Orientation, cameras, microphone, pressuresensors, distancemeasurements, weatherinstruments, balance/gyroscope, accelerometer, voltmeter (batterijpercentage checken),  |

2. For the agent in the previous exercise, characterize the environment according to the properties given at the end this lecture’s slides (or Section 2.3 of the textbook). 
> Partially Observable: You don't know what other players want/ are going to do; you cannot measure the ground condition of the whole field at the same time
> 
> Stochastic: there are external forces on the environment, other players may interfere
> 
> Sequential: within a single match, the actions of the agent are dependant on previous actions; each match is episodic, a match doesn't influence the next/previous one
> 
> Dynamic: Ball can be moving, other players may take actions, matchclock keeps going
> 
> Continuous: Toestanden en acties zijn niet telbaar dus continuous
> 
> Multiple Agent: Multiple players

3. Fill in the table below and discuss your answers with your colleagues.

| Agent                   | Performance measure                                                                        | Environment                                                                                                                   | Actuators                                                                                                                       | Sensors                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Doctor                  | Amount of helped patients                                                                  | Docter's office, patients, other specialists, nurses, medical files from the patient, medical instruments, medical literature | Medical implements, prescription writing implement, speakers, arms to manipulate patients, monitor to display things to patient | Camera, microphone, pressuresensors, thermometer, IR-scanner, stetoscope |
| Internet shopping agent | Requisted items delivered (within certain time period, price rang,...) client-satisfaction | The Internet, consumer, payment methods                                                                                       | Internet navigation tools (webrequests, API-calls), communication tool to consumer,                                             | Webscraper, webcontent analyser (text, images, webpages,...)             |
| Interactive Dutch tutor | Succesfully teaching Dutch, Student satisfaction                                           | classroom, students, blackboard, projector, webplatform, lesmateriaal                                                         | Speakers, writing arm, remote for slides, rode styllo                                                                           | Camera, microphone                                                       |

# Sessie 3
> Zie papieren notities en wpo2a.pdf

# Sessie 4
eerste orde predicaat logica

valid: alle waarderingen modellen, altijd waar
satisfiable: minstens 1 model
unsatisfiable: geen enkel model

> Zie papieren notities en wpo2b.pdf

# Sessie 5
> Zie papieren notities en wpo3.pdf

# Sessie 6
> Zie papieren notities en wpo4.pdf
> Bekijk ook oplossingen van Youri

# Sessie 7
> Zie papieren notities en wpo5.pdf

# Sessie 8
> Zie papieren notities en wpo6.pdf
> Aanpassingen van de code zijn niet gedaan in de local-search-exercises/simulated-annealing.rkt,
> maar in de copy in ai/simulated-annealing.rkt
> 2 mogelijke oplossingen, ik heb andere als Youri

# Sessie 9
> Zie papieren notities en wpo7.pdf

## Oefening 1
![[gametree-wpo7-oefening1.png]]
MiniMax:
![[gametree-oef1-wpo7-minimax.png]]

 αβ-pruning:

# Session 10


|     |     |
| --- | --- |
|     |     |
