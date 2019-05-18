import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.LEDForwardVoltage import LEDForwardVoltage
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class DigitalOutput(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()
		self._setDutyCycle_async = None
		self._onsetDutyCycle_async = None
		self._setLEDCurrentLimit_async = None
		self._onsetLEDCurrentLimit_async = None
		self._setState_async = None
		self._onsetState_async = None

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def getDutyCycle(self):
		_DutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_DutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _DutyCycle.value

	def setDutyCycle(self, DutyCycle):
		_DutyCycle = ctypes.c_double(DutyCycle)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DutyCycle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDutyCycle(self):
		_MinDutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMinDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinDutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinDutyCycle.value

	def getMaxDutyCycle(self):
		_MaxDutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMaxDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDutyCycle.value

	def setDutyCycle_async(self, DutyCycle, asyncHandler):
		_DutyCycle = ctypes.c_double(DutyCycle)

		_ctx = ctypes.c_void_p()
		if asyncHandler != None:
			_ctx = ctypes.c_void_p(AsyncSupport.add(asyncHandler, self))
		_asyncHandler = AsyncSupport.getCallback()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setDutyCycle_async
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DutyCycle, _asyncHandler, _ctx)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def enableFailsafe(self, failsafeTime):
		_failsafeTime = ctypes.c_uint32(failsafeTime)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_enableFailsafe
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _failsafeTime)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinFailsafeTime(self):
		_MinFailsafeTime = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMinFailsafeTime
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinFailsafeTime))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinFailsafeTime.value

	def getMaxFailsafeTime(self):
		_MaxFailsafeTime = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMaxFailsafeTime
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxFailsafeTime))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxFailsafeTime.value

	def getLEDCurrentLimit(self):
		_LEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_LEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _LEDCurrentLimit.value

	def setLEDCurrentLimit(self, LEDCurrentLimit):
		_LEDCurrentLimit = ctypes.c_double(LEDCurrentLimit)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _LEDCurrentLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinLEDCurrentLimit(self):
		_MinLEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMinLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinLEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinLEDCurrentLimit.value

	def getMaxLEDCurrentLimit(self):
		_MaxLEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMaxLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxLEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxLEDCurrentLimit.value

	def setLEDCurrentLimit_async(self, LEDCurrentLimit, asyncHandler):
		_LEDCurrentLimit = ctypes.c_double(LEDCurrentLimit)

		_ctx = ctypes.c_void_p()
		if asyncHandler != None:
			_ctx = ctypes.c_void_p(AsyncSupport.add(asyncHandler, self))
		_asyncHandler = AsyncSupport.getCallback()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setLEDCurrentLimit_async
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _LEDCurrentLimit, _asyncHandler, _ctx)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getLEDForwardVoltage(self):
		_LEDForwardVoltage = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getLEDForwardVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_LEDForwardVoltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _LEDForwardVoltage.value

	def setLEDForwardVoltage(self, LEDForwardVoltage):
		_LEDForwardVoltage = ctypes.c_int(LEDForwardVoltage)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setLEDForwardVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _LEDForwardVoltage)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def resetFailsafe(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_resetFailsafe
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getState(self):
		_State = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_State))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _State.value

	def setState(self, State):
		_State = ctypes.c_int(State)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _State)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def setState_async(self, State, asyncHandler):
		_State = ctypes.c_int(State)

		_ctx = ctypes.c_void_p()
		if asyncHandler != None:
			_ctx = ctypes.c_void_p(AsyncSupport.add(asyncHandler, self))
		_asyncHandler = AsyncSupport.getCallback()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setState_async
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _State, _asyncHandler, _ctx)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

