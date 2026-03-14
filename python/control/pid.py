class PIDController:
    def __init__(self, kP=1.0, kI=0.0, kD=0.0):
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.tolerance = 0.0
        self.tolerancePercent = 0.0

        self.positionError = 0.0
        self.velocityError = 0.0
        self.totalError = 0.0
        self.prevError = 0.0

        self.setpoint = 0.0
        self._atSetpoint = False

    # Updates tolerance as a hardcoded value
    def setTolerance(self, tolerance):
        self.tolerance = tolerance
        self.tolerancePercent = 0.0

    # Updates tolerance as a percent of the setpoint
    def setTolerancePercent(self, percent):
        self.tolerancePercent = percent
        self.tolerance = 0.0

    # Updates all PID values
    def setPID(self, kP, kI, kD):
        self.kP = kP
        self.kI = kI
        self.kD = kD

    # Gets tolerance
    def getTolerance(self, isPercent=False):
        if isPercent:
            return self.tolerancePercent
        return self.tolerance

    # Gets all PID values in a list [kP, kI, kD]
    def getPID(self):
        return [self.kP, self.kI, self.kD]

    # Sets new setpoint
    def setSetpoint(self, setpoint):
        self.setpoint = setpoint

    # Gets current setpoint
    def getSetpoint(self):
        return self.setpoint

    # Optional reset for integral/derivative history
    def reset(self):
        self.positionError = 0.0
        self.velocityError = 0.0
        self.totalError = 0.0
        self.prevError = 0.0
        self._atSetpoint = False

    # Calculates voltage from measurement, setpoint, and maxValue
    # dt = loop period in seconds
    # battery_voltage default is 12V
    def calculateForVoltage(self, measurement, maxValue, dt=0.02, battery_voltage=12.0):
        # PROPORTIONAL: current error
        self.positionError = self.setpoint - measurement

        # DERIVATIVE: change in error / time
        if dt != 0:
            self.velocityError = (self.positionError - self.prevError) / dt
        else:
            self.velocityError = 0.0

        # update previous error
        self.prevError = self.positionError

        # INTEGRAL: accumulated error over time
        self.totalError += self.positionError * dt

        # raw voltage output
        desiredVoltage = (
            (self.setpoint + (self.kP * self.positionError) + (self.kI * self.totalError) + (self.kD * self.velocityError))
            * battery_voltage / maxValue
        )

        if self.setpoint == 0:
            desiredVoltage = 0.0

        # clamp voltage to [-12, 12]
        desiredVoltage = max(-12.0, min(12.0, desiredVoltage))

        return desiredVoltage

    # Returns whether or not the measurement is at the setpoint with tolerance
    def atSetpoint(self, measurement):
        if self.tolerance != 0:
            self._atSetpoint = (self.setpoint - self.tolerance <= measurement <= self.setpoint + self.tolerance)

        elif self.tolerancePercent != 0:
            lower = self.setpoint * (1 - self.tolerancePercent)
            upper = self.setpoint * (1 + self.tolerancePercent)
            self._atSetpoint = (lower <= measurement <= upper)

        else:
            self._atSetpoint = (measurement == self.setpoint)

        return self._atSetpoint