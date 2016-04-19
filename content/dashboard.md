Dashboard or Trashboard?
Don't crash the dashboard
Dashboard hash-up

* No timeseries

What is on a car dashboard?
* Speedo
  * continuous, some marked speeds e.g. 50 k, 100 k, or 30 mph, 70 mph
  * speed limits 5, 10, 15, 20, 30, 40, 50, 60, 70, might as well be continous
  * advisories in 5s
  * deliberte overestimate on average (mitigate risk of poor judgement/response)
  * large (precise) dial or digital
* Revs
  * Continuous, red orange black indicators
  * Why?  Fuel efficiency?
* Distance since reset
  * Interactive! (reset)
  * Usually one decimal place
  * follow signs '400m on right'
  * company car personal use / vice versa
  * distance to destination
  * average speed in head (wasn't easy before car computers)
  * estimate fuel left
  * distance from last petrol station
* Total distance
  * Mileage log
  * Easily added since distance-since-reset is already there
  * periodic servicing
  * resale
  * integers (or thousands?)
  * small, not distracting
* Clock
  * Similar to distance
  * Interactive! (set)
  * minutes usually sufficient
  * still works when car not running (only one that does) all others are for
      driver when driving
* Fuel
  * continuous, unitless, small (low precision)
  * Rough markers, merely visual cues -- need driver experience to interpret
      when empty
  * Deliberate underestimate
* Warnings
  * Battery, oil, water -- why not levels like fuel?
  * Expensive to measure levels?
  * Driver to manually check level before long journeys
* Full beam / sidelights / fog reminders
* Others e.g. seatbelts
  * Shown too often, ignored
  * Gear -- better to feel for it, keep eyes on road
  * GPS? Not good, distracting

#### Size

* Speed is largest -- precision, importance
* Why revs also often large and precise?

#### Position

* In driver's immediate vision

#### Audience

* Driver only -- see position

#### Generality

* Very similar across all vehicles
* Simple design familiar to all
* Design doesn't disturb function

#### Types of display

* dial, clock/counter, lamp (nothing fancy)

#### Interactivity

* Set clock
* Reset distance

No need to interact -- driver has enough to do already

#### Response

Obvious (control speed, gears, lights, replenish fuel/oil/water/battery)

#### Decisions

All indicators require context and judgement for decision by the *driver*.

* speed limit, road conditions, load
* distance to destination / petrol station
* condition of vehicle (total distance)
* money (fuel)
* ambient light, weather, tunnels, presence of other vehicles (lights)
* urgency (time)

#### Education and training

* Unless driver understands, no licence

#### Design

Unless meet regulations, no vehicle

#### Necessity

Unless heeded, late / breakdown / crash / jail

#### Updates

* When car is on
* Continuous / when something changes (for instant response or instant
    preparation to respond e.g. fuel/oil)
* Automatic (necessarily?  See weather forecast)
* Passive -- not on request

#### Lifetime

* Same as vehicle
* No change to vehicle/purpose/destination/cargo/condition/owner requires a
    change to the dashboard.

## Other types of dashboard

* Medical (pulse, oxygen, etc)
* Aeroplane (years of training to cope with complexity vs. onoe or two weeks for
    a car)
* Market trading
* McDonalds?  Really a list
* Weather forecast
  * Do in detail as above, standard symbols, needs context for decision, *not*
      autoomatic (meteorologist), revisions, levels of detail for broad
      audience, not interactive except for scope but that'll change with
      persistant personal profiles on weather apps.
  * If ignore, okay, if disestablish, bugger!  Very expensive, R&D making slow
      progress

## Not on car dashboard

* Lots of MOT stuff
  * Break pads, tire tread, rust, tire pressure, spare wheel, exhaust fumes,
      cargcargo weight, traffic, weather forecast, directions, compass, altitude
* Driver is responsible, but doesn't need to know MOT stuff while driving.  It
    can be reserved for the ordinary work programme / special project.

## Dashboards I know

* TSM
* Speeding tickets
* Tourism
* REAR
* MTAGDP
* MBIE Dashboard

## Traps

Manager drive many vehicles (projects and people) so need many dashboards.  One
dashboard (or via interaction) per direct report?  No, one per audience, limited
to what they can immediately respond to or prepare to respond to -- if no more
space on dashboard, no more capacity in manager.

Drill-down control freak
* Hierarchy is not working
* Senior manager doesn't have context to interpret lower levels, freedom to
    drop everything and respond immediately, time to coordinate preparation.
* Alarms need to come *up* to senior level (if it isn't happening, dashboard
    won't fix it).  Seniors should have mostly alarms (lamps, strategic) and few
    dials (operational).

Migrate existing measures into dashboard -- no! Existing measures are probably
designed for another context e.g. Annual Report (MOT) or operations (dials) so
not suitable for managers.  If Annual Report doesn't work then probably both
measures and possible responses need redevelopment.  If annual report is
working then dashboard is expensive eye-candy.


When data can bet cut many ways, interactivity is the lazy option -- client-side
processing -- because most stuff is boring, or (worse) misleading (multiple
compacomparisons), and exhausting because requires much client contextual
knowledge, whereas a selective report can provide the necessary context.

Speed strongly and causally associated with distance and time, to a lesser
extent safety, and at certain thresholds in certain contexts, legality.  All are
concerns of the driver when driving.

Traffic lights graphs 

No dashboard tells the driver what to do or what to prioritise.  That is a human
decision.  When cars drive themselves, we won't need dashboards.  o

The information on the dashboard is insufficient to drive the car.  The driver
also needs at least one eye, and hearing helps.  For the car to drive itself it
needs to observe its context, anticipate the actions of other road users, and
prioritise competing objectives.  The first one (observation) is close to being
solved by LiDaR and computer vision.  The second (anticipation) will never be
perfect, which makes the final one (prioritisation) a tough call (who should the
vehicle kill, a pedestrian or a passenger? -- link).

If a manager of McDonald's want's to 'drill down' into the factors behind
customer satisfaction, then here is one pathway: Flavour -> meat -> elbow-deep
inside a cow.  The need to drill down is only felt when reporting up isn't
working.  Drills needn't go down unless reports aren't coming up.  When a
reporting structure works well, every level of aggregation involves humans
talking to other humans about data.  All the conversations are between managers
and their direct reports, beginning, "This stat looks funny", and none of them
involve the CEO brandishing his drill at an intern, saying "Gotcha!"

Blurred boundary between dashboard (operational) and interactive graphic
(journalism)

Todo:
* dashboard standards
