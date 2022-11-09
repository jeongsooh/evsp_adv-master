# test = [{
#   'timestamp' : '2022-10-26T17:31:49.000Z', 
#   'sampledValue' : [
#       {
#           'value' : '3673.80', 
#           'context' : 'Sample.Periodic', 
#           'format' : 'Raw', 
#           'measurand' : 'Energy.Active.Import.Register', 
#           'unit' : 'Wh'
#       },
#       {
#           'value' : '72.44', 
#           'context' : 'Sample.Periodic', 
#           'format' : 'Raw', 
#           'measurand' : 'Temperature', 
#           'unit' : 'Celcius'
#       }
#   ]
# }]

# print(test[0]['sampledValue'][0]['value'])

from datetime import datetime, timezone, timedelta
import time

timestamp = time.time()

dt = '2022-08-06T03:44:55.024Z'
dt_now = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(hours=9)
# dt = datetime.now() - timedelta(hours=9)
dt_utc = datetime.utcnow() 
print('dt = {}, dt_utc = {}'.format(dt_now, dt_utc))
# dt2 = datetime.fromtimestamp(timestamp, timezone(timedelta(hours=9)))
# dt2 = datetime.fromtimestamp(timestamp - timedelta(hours=9))
# print('timestamp -> datetime is ', dt2)

{
  'configurationKey': [
    {'key': 'GetConfigurationMaxKeys', 'readonly': True, 'value': '50'}, 
    {'key': 'NumberOfConnectors', 'readonly': True, 'value': '1'}, 
    {'key': 'SupportedFeatureProfilesMaxLength', 'readonly': True, 'value': '4'}, 
    {'key': 'MeterValueSampleInterval', 'readonly': False, 'value': '120'}, 
    {'key': 'ClockAlignedDataInterval', 'readonly': False, 'value': '0'}, 
    {'key': 'ConnectionTimeOut', 'readonly': False, 'value': '180'}, 
    {'key': 'MinimumStatusDuration', 'readonly': False, 'value': '0'}, 
    {'key': 'ResetRetries', 'readonly': False, 'value': '1'}, 
    {'key': 'HeartbeatInterval', 'readonly': False, 'value': '120'}, 
    {'key': 'MeterValuesAlignedDataMaxLength', 'readonly': False, 'value': '1'}, 
    {'key': 'MeterValuesSampledDataMaxLength', 'readonly': False, 'value': '1'}, 
    {'key': 'StopTxnAlignedDataMaxLength', 'readonly': False, 'value': '1'}, 
    {'key': 'StopTxnSampledDataMaxLength', 'readonly': False, 'value': '1'}, 
    {'key': 'TransactionMessageAttempts', 'readonly': False, 'value': '3'}, 
    {'key': 'TransactionMessageRetryInterval', 'readonly': False, 'value': '3'}, 
    {'key': 'LocalAuthListMaxLength', 'readonly': True, 'value': '20'}, 
    {'key': 'SendLocalListMaxLength', 'readonly': True, 'value': '10'}, 
    {'key': 'ChargeProfileMaxStackLevel', 'readonly': True, 'value': '0'}, 
    {'key': 'MaxChargingProfilesInstalled', 'readonly': True, 'value': '0'}, 
    {'key': 'ChargingScheduleMaxPeriods', 'readonly': True, 'value': '0'}, 
    {'key': 'AuthorizationCacheEnabled', 'readonly': False, 'value': 'false'}, 
    {'key': 'AuthorizeRemoteTxRequests', 'readonly': False, 'value': 'true'}, 
    {'key': 'AllowOfflineTxForUnknownId', 'readonly': False, 'value': 'false'}, 
    {'key': 'LocalAuthorizeOffline', 'readonly': False, 'value': 'false'}, 
    {'key': 'LocalPreAuthorize', 'readonly': False, 'value': 'false'}, 
    {'key': 'UnlockConnectorOnEVSideDisconnect', 'readonly': False, 'value': 'false'}, 
    {'key': 'StopTransactionOnEVSideDisconnect', 'readonly': False, 'value': 'true'}, 
    {'key': 'StopTransactionOnInvalidId', 'readonly': False, 'value': 'true'}, 
    {'key': 'LocalAuthListEnabled', 'readonly': False, 'value': 'false'}, 
    {'key': 'SupportedFeatureProfiles', 'readonly': True, 'value': 'Core,FirmwareManagement,LocalAuthListManagement,RemoteTrigger'}, 
    {'key': 'SupportedFileTransferProtocols', 'readonly': True, 'value': 'HTTP,FTP'}, 
    {'key': 'ConnectorPhaseRotation', 'readonly': False, 'value': 'NotApplicable'}, 
    {'key': 'MeterValuesAlignedData', 'readonly': False, 'value': 'Energy.Active.Import.Register'}, 
    {'key': 'MeterValuesSampledData', 'readonly': False, 'value': 'Energy.Active.Import.Register'}, 
    {'key': 'StopTxnSampledData', 'readonly': False, 'value': 'Energy.Active.Import.Register'}, 
    {'key': 'StopTxnAlignedData', 'readonly': False, 'value': 'Energy.Active.Import.Register'}, 
    {'key': 'AuthorizationKey', 'readonly': False, 'value': 'ocpp'}, 
    {'key': 'ChargingScheduleAllowedChargingRateUnit', 'readonly': True, 'value': 'Current'}
  ]
}