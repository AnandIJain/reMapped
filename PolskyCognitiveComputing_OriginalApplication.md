# reMapped
All files related to the reMapped transportation project

Initial application document:

**1.	What problem are you trying to solve OR the subject area you're interested in exploring? What kind of questions are getting asked?

According to the World Bank, the world’s urban population was roughly 54% in 2014 and has been steadily increasing since the World Bank first began collecting data on urban population in 1960. As people become more concentrated in metropolitan areas, adaptive and efficient transportation becomes increasingly valuable. Cities must ensure that citizens do not spend excessive amounts of time in transit. 

A major factor that contributes to decreased mobility within a city (an area) is owning and driving a car. In terms of the ratio of road-space usage to passenger count, single passenger cars far more wasteful than public transportation or bicycles, which either have a higher passenger density or occupy less space. 

Additionally, it is important to keep in mind that it would be extremely challenging to mitigate traffic issues associated with driving by attempting to increase road-space. Therefore, cities must turn to improving mobility through other methods. One of the primary methods is recording and analyzing data on the transit usage across the city and adapting current resources and systems to better suit the transit needs as shown by the recorded data. 

The University of Chicago manages a shuttle service for University affiliates and, in following the trend of recording transit data, has installed ID card readers in all shuttles. The data that is currently recorded by these scanners is the route of the bus, the time of the ID swipe, and the individual’s affiliation to the University. By analyzing this data, the University can better understand the needs of riders, enabling the University to more appropriately allocate shuttles.

However, the data currently being analyzed provides an incomplete model of ridership trends and the transit needs of University affiliates. I often see busses driving around campus with no passengers, which creates pollution and costs money, with no apparent benefit (unless it is assumed that there is someone waiting for the shuttle at a later stop). If the data recorded during each shuttle trip was expanded to include the current time and location of the bus upon a passenger’s entry and exit, then the University would have the data to determine if new shuttle routes exist that better address the transit needs of University affiliates.

This analysis and data collection has the potential to better optimize the efficiency of the shuttles. In doing such a project, The University of Chicago could become a model for what good, efficient transit can be.


**2.	How do people currently address the problem?

While novel transit solutions are constantly being innovated, the goal of an effective transit system is more or less consistent: to provide a system that maximizes ridership and mobility within the area and minimizes travel time and system expenditures. Achieving this goal, in the context of creating a bus system, begins with developing a macroscopic understanding of the city. This means collecting data on the properties of the city that imply needing access to public transportation, such as the location and statistics on dense housing neighborhoods, shopping and job centers, and popular sights and destinations. Using this data, a rough model for the necessities of the system can be mapped out and used to approximate general locations in which buses will travel between. 

The next step in creating efficient bus routes is collecting data that is more specific to individual locations and streets, such as the amount of foot-traffic, street-traffic, and economic activity for the location throughout the day. Once this data has been collected, transit agencies can make informed decisions on specific route and stop placement.  For example, since there is a large amount of tourism and economic activity at the Navy Pier, it is intuitive to have bus routes that go to the densest and most accessible parts of the Pier.

However, it is important to recognize that making these decisions requires the consideration of more factors and variables than a person could accurately comprehend and weigh. For this reason, it has become almost universal practice within transit systems to record and analyze ridership data to determine if the ridership is matching the expected levels. It is important to ensure that the transit needs are being matched by the provided services as it is problematic to have an overcrowded bus or an underused one. Overcrowded routes or buses imply a potential outlet to increase ridership, whereas underused routes or buses are financially inefficient and imply that a route improvement might exist.

If ridership trends were predictable, it is intuitive that transit authorities would not want to wait until the discrepancy in ridership and expectations hits a certain threshold to adapt routes and stops to meet transit needs. Therefore, when transit agencies create their systems, approximated models of the city up to 25 years in advance are kept in mind. The reason is that making alterations to routes, even if they improve the efficiency of the system, have the potential to decrease ridership in the short term as individuals adjust to the new routes. Therefore, by designing the system with the long-term future of the city in mind, transit agencies are able to better minimize the amount of large scale system changes that will be necessary.


**3.	Who are the experts that weigh in to answer questions or uncover relevant information from available information?

Improving transit and increasing the mobility within a city is an immensely complex issue and requires the expertise of a multitude of disciplines. For example, knowledge of city planning and urban development is necessary to ensure that the transit system is adapting to changes within the city and is correctly allocating resources to various locations. Additionally, traffic engineers are necessary to plan routes that will be efficient and avoid being inhibited by traffic as much as possible, while still maximizing ridership. 

Data analysists and statisticians are also immensely important in the extrapolation of meaning from the large ridership datasets. For example, the analysis for determining the inefficiency of a route is largely accomplished through statistical modelling. 

Additionally, computer scientists are becoming increasingly vital to optimization and pathing tasks that require the analysis of many variables, such as the creation of efficient bus routes. Computer scientists specializing in machine learning would be useful to lend their expertise as the prediction of ridership based on past data is a machine learning task.

Singapore, with the help of the A-STAR Institute of High Performance Computing, has already applied machine learning models to the dataset of one week of transit rides to prove that the distribution of amenities further from the ‘central business district’ would increase public transit use. In this study, Singapore employed the use of machine learning to aid in their decision-making with regards to large city planning projects, such as their goal to spread out regional business centers, instead of relying solely on a singular central business district. Similar techniques could be applied to the ridership data in Chicago to help make decisions in planning the city for the future. 


**4. What computer systems/tools, if any, are currently being used to help address the problem? 

In the case of many metropolitan areas, municipalities and transit authorities are increasingly becoming aware of the value of data collection. It is rare to find a transit system that solely relies on manual data collection. Many cities use a swipe system, such as the Ventra card or our ID system for housing, dining halls, libraries, and shuttles. Cities utilize this ridership data to make decisions on changing bus routes and finding creative solutions to improve mobility within the city.

In 2015, the City of Houston underwent dramatic changes in their Metro system. The primary motivation for this was that ridership was not meeting desired levels and, most importantly, their publicly available ridership data showed the current system to be inefficient. Houston’s making these changes represents a shift in attitude regarding data driven decisions in city planning. Although ridership decreased in the short term, Houston recovered and has been one of the national leaders in ridership. These results are especially impressive in the context of a nation whose public transportation usage has overall been decreasing. For reference, public transit usage changes from 2015 to 2016 in Houston were +2.3%, while Chicago experienced a drop of 3.2%.

Chicago, too, has ridership data publicly available and has almost all data since 2001, which is uploaded onto the data.cityofchicago.org website. Having data across this large of a time-span is quite incredible and useful for understanding ridership trends through a multitude of time scopes. With over a decade of data, it would be apparent that certain trends occur on different time cycles. For example, each year, ridership all throughout Chicago increases dramatically for Lollapalooza, which would be recognized as a trend that occurs on a yearly basis. Additionally, with the ridership data backing up this trend, the transit agency would be able to prepare for the dramatic increase in ridership, especially near Grant Park. 


**5. What data underpins the expertise or system/tool capabilities? 

The data that is important in creating and maintaining a transit system is acquired from a multitude of sources. For example, when creating the baseline macroscopic perspective of the city, real estate sales, economic activity, new building developments, and median income would all be useful. Real estate sales would reflect housing trends in the city, economic activity would have a correlation to the amount of foot traffic in the area, and new building developments would imply how the area is changing and whether the area is becoming increasingly industrial or not. The traffic data throughout the city is also important in designing routes that maximize ridership and minimize travel time. 	

However, the ridership data is most important resource available to transit agencies. Typically, the data recorded from a single person’s trip would be an identifier, the time swiped, the bus route, and occasionally the location at the time the card was swiped. Ridership data is the most immediate and reliable data set for determining the efficiency of a given system, route, or stop. Additionally, since there is such a large amount of data, inferences on the other data can be made. For example, if the ridership data shows that the times at which a given bus is supposed to arrive at a stop is consistently earlier during rush hour than the times that passengers at that stop enter the bus, it could be inferred that a possible cause for the delay is heightened traffic. 

These sources of data are all used to enhance and more accurately represent a model of the city and the transit needs of the city’s citizens.


**6. Is the data structured e.g., tabular data, unstructured e.g., free form text, or both?

The data that would be recorded and used in developing an efficient transit system would come from multiple sources, which presents a challenge in converting each data source into a single uniform dataset. 

Ridership data is the most cleanly formatted set as it is entirely tabular and the expansion of data points per swipe would only require adding additional columns to the spreadsheet. However, more complex data such as new building developments, real estate sales, and the economic activity of a given area are harder to format. 

Overall, data useful to improving a transit system exists in all the above formats. However, as it relates to the improvement of the University of Chicago’s shuttle system, it may not be as important to acquire and analyze data that is not information recorded on shuttle swipes, since real estate sales and economic activity are less influential on the ridership trends of University shuttles than 
Chicago’s public transportation.


**7. What makes the problem especially difficult to address?
  
There are two major obstacles in accomplishing and finishing this project. Since I am proposing to log the location of the bus upon the entry and exit of a rider, there are inherent privacy concerns that must be addressed. However, there are ways to safely and non-intrusively record and analyze this data. 

Many individuals, including myself, have privacy concerns when location data is tracked, especially from one’s phone. The reason that it is especially concerning to have location data tracked from one’s phone is that the degree to which a person in possession of that data would be confident in the identity of the person is high. However, in this case, the location data of the bus is being recorded, as the shuttles already utilize this data to send to the UChicago mobile app. Recording the shuttle’s location data adds a degree of anonymity to the identity of the rider. The second method for counteracting privacy concerns is to adopt the privacy methods used by the Array of Things project. The Array of Things takes in raw data, which is processed and sent to the main dataset, at which point the raw data is deleted, since the deep learning algorithm has no use for it. A similar solution could be devised to protect the identity and location of shuttle riders. A third method for calming privacy concerns would be implementing the increased data logging as a optional decision. Only those who opt in to having the location of the bus logged on entry and exit would be affected. 

The second obstacle is my needing to learn more about machine learning, programming, and computational statistical analysis so that I will be able to contribute and accomplish this project. I am hoping that I will be able to learn more as I progress through the project. 


**8. How might this problem area be improved by a cognitive approach? 

A cognitive approach refers to pattern recognition, which is very similar to what an adaptive algorithm is. Machine learning is based around the idea that computers can be made more efficient through pattern analysis and recognition. For example, a machine learning algorithm applied to shuttle ridership data would recognize that shuttle ridership is heightened during Finals week, as more people are staying up late at the library. Recognizing this beforehand, we would be able to apply this to future finals weeks and hire more drivers specifically during these times. As stated, the use of a ‘cognitive approach’ would allow the data analysis to be expedited as far less manual labor would be done on compiling and analyzing data. Building a system that is reliant on being adaptive is also more future-proof than more static systems that are not capable of tracking ridership patterns and inferring usage from past data.

Additionally, as the University of Chicago expands and grows increasingly further from the main quad, recognizing specific areas of growth will be crucial in development of new transportation solutions, including new shuttle routes. For example, once the new Polsky Center for Entrepreneurship and Innovation opens, there will be a larger group of individuals needing transport between the main campus and the new location. Applying machine learning algorithms on this ridership data will be especially important in the months after the Center opens so that the routes and frequency of buses can be calibrated and optimized. 


**9.	Describe one or more real-life scenarios for your application. Be expansive.
  
While this project would directly affect University affiliates, machine learning principles could be applied to any transit system and, after some time, would result in improvements. The reason that there is a high probability for increased mobility and transit efficiency in a transit system is that a machine learning algorithm could better take all past data into account to predict future ridership. A person would be unable to do this, as the sheer quantity of data being produced is too large for a human to correctly recognize all the trends in the data. 

The City of Chicago should use machine learning algorithms to analyze data produced by CTA busses. Chicago would be especially suited to transit route alterations as the cost of rerouting busses is minimal compared to that of the subway or the “L”. Furthermore, the route alterations could be made gradually, as opposed to the dramatic alterations made in the City of Houston, which would easy transit riders into the new bus system and would mitigate the possible short-term ridership losses, like those experienced in Houston. 


**10. Who will benefit from a solution to the problem?

University affiliates would benefit directly from this project, however, if it is shown that increased ridership and improved bus routes is a result of applying machine learning principles to transit ridership data, cities all over the world could benefit. If the City of Chicago were to adopt the application of machine learning to their system and ridership increased, traffic would decrease as more people started preferring public transportation over cars. By increasing mobility within the city, citizens are more likely to travel around the city, which would naturally increase economic activity. Furthermore, as a result of increased public transportation usage, there would be less smog and pollution being emitted. For extremely polluted cities, increasing the efficacy of public transportation is a clear route to decreasing car usage and greenhouse gas emissions.
