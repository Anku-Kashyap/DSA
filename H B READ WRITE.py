#                   '''HEART BEAT READ AND WRITE FROM STATION'''
import OpenOPC

import pywintypes  # To avoid timeout error
import time

import sys

import win32file
from pylogix import PLC
sys.path.append('..')

pywintypes.datetime = pywintypes.TimeType
x = time.time()
v = time.time()
opc = OpenOPC.client()
servers = opc.servers()
opc.connect('Kepware.KEPServerEX.V6')
aliases = opc.list()

while True:

    x1 = time.time()
    l = []
    with PLC() as comm:
        IP = '192.168.13.110'
        comm.IPAddress = IP
        comm.ProcessorSlot = 0

        Read_data = [
            ('NAI_N_HEART_BEAT_WRITE'),
            ('NAI_S_HEART_BEAT_WRITE'),
            ('NSP_N_HEART_BEAT_WRITE'),
            ('NSP_S_HEART_BEAT_WRITE'),
            ('SLM_N_HEART_BEAT_WRITE'),
            ('SLM_S_HEART_BEAT_WRITE'),
            ('AZP_N_HEART_BEAT_WRITE'),
            ('AZP_S_HEART_BEAT_WRITE')
        ]
        ret = comm.Read(Read_data)
        Hb_l = [0, 1, 2, 3, 4, 5, 6, 7]
        k = 0
        while k <= 8:
            for r in ret:
                x = r.Value
                if k == 0:
                    Hb_l[0] = x
                if k == 1:
                    Hb_l[1] = x
                if k == 2:
                    Hb_l[2] = x
                if k == 3:
                    Hb_l[3] = x
                if k == 4:
                    Hb_l[4] = x
                if k == 5:
                    Hb_l[5] = x
                if k == 6:
                    Hb_l[6] = x
                if k == 7:
                    Hb_l[7] = x
                k = k + 1
        # print(Hb_l)

        tag_val = [('Channel7.Device1.AA_NAI_N HB WRITE TO STATION', l[0]),

                   ('Channel7.Device1.AA_NAI_S HB WRITE TO STATION', l[1]),
                   ('Channel7.Device1.AA_NSP_N HB WRITE TO STATION', l[2]),
                   ('Channel7.Device1.AA_NSP_S HB WRITE TO STATION', l[3]),
                   ('Channel7.Device1.AA_SLM_N HB WRITE TO STATION', l[4]),
                   ('Channel7.Device1.AA_SLM_S HB WRITE TO STATION', l[5]),
                   ('Channel7.Device1.AA_AZP_N HB WRITE TO STATION', l[6]),
                   ('Channel7.Device1.AA_AZP_S HB WRITE TO STATION', l[7])]
        Tag = [
            ('Channel7.Device1.AA_NAI_N HB WRITE TO STATION'),
            ('Channel7.Device1.AA_NAI_S HB WRITE TO STATION'),
            ('Channel7.Device1.AA_NSP_N HB WRITE TO STATION'),
            ('Channel7.Device1.AA_NSP_S HB WRITE TO STATION'),
            ('Channel7.Device1.AA_SLM_N HB WRITE TO STATION'),
            ('Channel7.Device1.AA_SLM_S HB WRITE TO STATION'),
            ('Channel7.Device1.AA_AZP_N HB WRITE TO STATION'),
            ('Channel7.Device1.AA_AZP_S HB WRITE TO STATION')]

        try:

            Write_Val = opc.write(tag_val)
            Read = opc.read(Tag)

        except OpenOPC.TimeoutError:
            print("TimeoutError occured", flush=True)

        z1 = time.time()
        print(z1 - x1, flush=True)
