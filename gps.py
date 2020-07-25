import time
import logging

from sim_access.adapter import SerialAdapter
from sim_access.sim import SIMModuleBase


logger = logging.getLogger(__name__)


class GPS(SIMModuleBase):
    def on_sms(self, number, content):
        logger.info(
            f"Text from: {number}, Content: \'{content}\'"
        )


if __name__ == '__main__':

    # Serial Port, it can be Arduino Port, or /devtty0 in Raspberry
    serial_port = 'COM3'

    APN = 'pwg'

    serial_adapter = SerialAdapter(devfile=serial_port)

    sim = GPS(serial_adapter)

    #based on https://m2msupport.net/m2msupport/atciicr-bring-up-gprs-or-circuit-switch-connection/
    sim.network_attach()
    sim.network_setapn(APN) # usmobile apn
    sim.network_bringup()
    addr = sim.network_ipaddr()

    print(f'My IP: {addr}')

    ((longitude, latitude), date, time) = sim.gps_location_date_time(APN)
    print(f'Longitude: {longitude}\nLatitude: {latitude}\nDate: {date}\nTime: {time}\n')

    sim.mainloop()