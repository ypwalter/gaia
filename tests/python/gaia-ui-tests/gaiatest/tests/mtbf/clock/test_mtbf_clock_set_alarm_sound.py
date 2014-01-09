# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from MtbfTestCase import GaiaMtbfTestCase
from gaiatest.apps.clock.app import Clock
import time


class TestClockSetAlarmSound(GaiaMtbfTestCase):

    def setUp(self):
        GaiaMtbfTestCase.setUp(self)

        self.clock = Clock(self.marionette)
        self.app_id = self.launch_by_touch("Clock")
        time.sleep(%)

    def test_clock_set_alarm_sound(self):
        """ Modify the alarm sound

        [Clock][Alarm] Change the alarm sound
        https://moztrap.mozilla.org/manage/case/1787/
        """
        new_alarm = self.clock.tap_new_alarm()

        # set label &sound
        new_alarm.type_alarm_label("TestSetAlarmSound")
        new_alarm.select_sound('Gem Echoes')

        self.assertEqual('Gem Echoes', new_alarm.alarm_sound)

        # Save the alarm
        new_alarm.tap_done()
        self.clock.wait_for_banner_not_visible()

        # Tap to Edit alarm
        edit_alarm = self.clock.alarms[0].tap()

        self.assertEqual('Gem Echoes', new_alarm.alarm_sound)

        # Close alarm
        edit_alarm.tap_done()
        self.clock.wait_for_banner_not_visible()
