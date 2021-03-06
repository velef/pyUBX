#!/usr/bin/env python3
"""Unit tests."""

import unittest
from ubx import UBX
from ubx import parseUBXPayload, parseUBXMessage


class TestStringMethods(unittest.TestCase):

    def testClassId1(self):
        getVer = UBX.MON.VER.Get()
        self.assertEqual(getVer._class, 0x0A)
        self.assertEqual(getVer._id, 0x04)

    def testClassId2(self):
        self.assertEqual(UBX.MON._class, 0x0A)
        self.assertEqual(UBX.MON.VER._class, 0x0A)
        self.assertEqual(UBX.MON.VER._id, 0x04)

    def testRXM(self):
        rxm = UBX.CFG.RXM(b'\x48\x00')
        self.assertEqual(rxm.reserved1, 0x48)
        self.assertEqual(rxm.lpMode, 0x00)
        rxm.lpMode = 1
        msg = rxm.serialize()
        rxm2 = parseUBXMessage(msg)
        self.assertEqual(rxm.reserved1, 0x48)
        self.assertEqual(rxm.lpMode, 0x01)

    def testMON_SPAN(self):
        # F9P data payload
        payload = b'\x00\x02\x00\x00\x39\x37\x37\x3A\x3A\x39\x39\x39\x39\x38\x38\x39\x39\x39\x3B\x3B\x3A\x3A\x39\x3B\x3F\x3C\x3D\x3E\x3C\x3D\x3F\x3F\x45\x3E\x40\x43\x66\x43\x55\x43\x47\x47\x44\x47\x49\x47\x4B\x48\x50\x47\x4C\x4E\x4F\x51\x56\x57\x5B\x5D\x60\x61\x66\x67\x69\x6C\x6E\x6F\x75\x73\x79\x79\x7A\x7D\x7E\x80\x83\x85\x86\x88\x87\x88\x8C\x8D\x8C\x8F\x92\x94\x95\x94\x93\x90\x8F\x8F\x8F\x8E\x8E\x90\x90\x8F\x8E\x8F\x91\x90\x92\x91\x93\x92\x91\x93\x94\x93\x94\x95\x99\x9E\xA3\xA6\xA5\xA0\x99\x96\x98\x98\x97\x97\x95\x97\x97\x97\x95\x94\x94\x99\x95\x94\x93\x92\x93\x9C\x93\x92\x92\x92\x94\x96\x97\x96\x95\x92\x90\x90\x8C\x8C\x8C\x8C\x8B\x8C\x8B\x8A\x8C\x8B\x8A\x8A\x8B\x8A\x8B\x8C\x8B\x8E\x8C\x8A\x89\x8B\x8B\x89\x89\x88\x87\x87\x85\x87\x86\x86\x84\x84\x84\x82\x82\x80\x80\x7E\x7D\x79\x79\x77\x75\x71\x71\x6E\x6D\x69\x65\x62\x5F\x5C\x57\x54\x52\x50\x4D\x4B\x4C\x4A\x4A\x49\x47\x47\x46\x45\x45\x42\x43\x42\x41\x41\x46\x40\x41\x3E\x42\x40\x40\x3D\x3D\x3D\x3D\x3C\x41\x3F\x3A\x3A\x39\x3A\x3A\x3A\x39\x39\x3A\x3A\x39\x38\x38\x3A\x39\x38\x38\x38\x39\x39\x38\x39\x00\x20\xA1\x07\x20\xA1\x07\x00\x82\xB3\x61\x5E\x33\x00\x00\x00\x34\x36\x33\x32\x36\x36\x36\x36\x36\x39\x38\x39\x39\x3A\x3B\x39\x3A\x42\x42\x41\x42\x40\x40\x41\x43\x49\x47\x46\x49\x47\x49\x4D\x4C\x51\x54\x51\x54\x57\x58\x5A\x5C\x5F\x5D\x60\x63\x64\x68\x68\x6B\x6C\x6E\x72\x73\x76\x78\x79\x7D\x7E\x81\x87\x84\x87\x88\x8A\x8B\x8C\x8E\x8E\x90\x91\x91\x94\x94\x95\x94\x96\x96\x97\x96\x96\x97\x97\x96\x99\x98\x99\x9A\x99\x99\x98\x99\x99\x9B\x9B\x9B\x99\x98\x97\x97\x96\x96\x96\x97\x94\x94\x94\x94\x94\x95\x94\x95\x94\x93\x96\x94\x94\x95\x95\x95\x96\x95\x95\x95\x95\x95\x94\x94\x91\x93\x94\x94\x93\x92\x97\x9C\x9A\x93\x92\x91\x91\x92\x91\x90\x91\x90\x8F\x8F\x90\x8F\x8F\x8E\x8E\x8C\x8E\x8F\x8D\x8E\x8D\x94\x8B\x8C\x8C\x8B\x8E\x8A\x89\x8B\x8B\x8B\x8C\x8D\x8B\x8B\x8A\x8B\x8A\x8B\x8A\x8B\x89\x8A\x89\x89\x88\x85\x86\x85\x84\x82\x81\x81\x7D\x7C\x7C\x79\x77\x74\x74\x71\x6E\x6C\x6A\x67\x66\x64\x61\x5F\x5E\x5B\x59\x57\x56\x56\x51\x50\x4E\x4D\x4B\x49\x49\x47\x44\x44\x43\x41\x3F\x3E\x3C\x3C\x3A\x3B\x3A\x38\x39\x37\x37\x38\x38\x37\x4A\x36\x35\x35\x34\x34\x34\x34\x33\x33\x32\x34\x33\x34\x33\x33\x32\x00\x20\xA1\x07\x20\xA1\x07\x00\x6A\xDA\xF4\x48\x2D\x00\x00\x00'
        span=parseUBXPayload(UBX.MON._class,  UBX.MON.SPAN._id, payload)
        self.assertEqual(span.numRfBlocks, 2)
        self.assertEqual(span.center_2, 1224006250)
        self.assertEqual(span.spectra[1]['spectrumBinCenterFreqs'][0], 1160006250.0)

    def testMON_VER(self):
        payload = b'\x52\x4f\x4d\x20\x43\x4f\x52\x45\x20\x33\x2e\x30\x31\x20\x28\x31\x30\x37\x38\x38\x38\x29\x00\x00\x00\x00\x00\x00\x00\x00\x30\x30\x30\x38\x30\x30\x30\x30\x00\x00\x46\x57\x56\x45\x52\x3d\x53\x50\x47\x20\x33\x2e\x30\x31\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\x52\x4f\x54\x56\x45\x52\x3d\x31\x38\x2e\x30\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x47\x50\x53\x3b\x47\x4c\x4f\x3b\x47\x41\x4c\x3b\x42\x44\x53\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x53\x42\x41\x53\x3b\x49\x4d\x45\x53\x3b\x51\x5a\x53\x53\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        ver = parseUBXPayload(UBX.MON._class, UBX.MON.VER._id, payload)
        self.assertEqual(ver.swVersion, "ROM CORE 3.01 (107888)")
        self.assertEqual(ver.hwVersion, "00080000")
        self.assertEqual(ver.extension_1, "FWVER=SPG 3.01")
        self.assertEqual(ver.extension_2, "PROTVER=18.00")
        self.assertEqual(ver.extension_3, "GPS;GLO;GAL;BDS")
        self.assertEqual(ver.extension_4, "SBAS;IMES;QZSS")

    def testCFG_GNSS(self):
        payload = b'\x00\x20\x20\x07\x00\x08\x10\x00\x01\x00\x01\x01\x01\x01\x03\x00\x01\x00\x01\x01\x02\x04\x08\x00\x00\x00\x01\x01\x03\x08\x10\x00\x00\x00\x01\x01\x04\x00\x08\x00\x00\x00\x01\x03\x05\x00\x03\x00\x01\x00\x01\x05\x06\x08\x0e\x00\x01\x00\x01\x01'
        gnss = parseUBXPayload(UBX.CFG._class, UBX.CFG.GNSS._id, payload)
        self.assertEqual(gnss.msgVer, 0x00)
        self.assertEqual(gnss.numConfigBlocks, 0x07)
        self.assertEqual(gnss.maxTrkCh_1, 0x10)
        self.assertEqual(gnss.flags_4, 0x01010000)
        self.assertEqual(gnss.maxTrkCh_7, 0x0E)


if __name__ == '__main__':
    unittest.main()
