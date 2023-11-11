class Transport:
    pass


class WaterTransport(Transport):
    pass


class PassengerWaterTransport(WaterTransport):
    pass


class CargoWaterTransport(WaterTransport):
    pass


class AirTransport(Transport):
    pass


class Aviation(AirTransport):
    pass


class PassengerAviation(Aviation):
    pass


class CargoAviation(Aviation):
    pass


class Aeronautics(AirTransport):
    pass


class GroundTransport(Transport):
    pass


class RailwayTransport(GroundTransport):
    pass


class PassengerRailwayTransport(RailwayTransport):
    pass


class CargoRailwayTransport(RailwayTransport):
    pass


class RoadTransport(GroundTransport):
    pass


class PassengerRoadTransport(RoadTransport):
    pass


class CargoRoadTransport(RoadTransport):
    pass


class MeansOfIndividualMobility(GroundTransport):
    pass


class Scooter(MeansOfIndividualMobility):
    pass


class Bicycle(MeansOfIndividualMobility):
    pass


class SkateBoard(MeansOfIndividualMobility):
    pass


class DrivenByAnimalsTransport(GroundTransport):
    pass


class Carriage(DrivenByAnimalsTransport):
    pass


class SpaceTransport(Transport):
    pass
