# NO LICENSE 2018
#
# Unless required by applicable law or agreed to in writing, software
# distributed under this lack of License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

from os.path import join, dirname
from mycroft.skills.core import FallbackSkill
from rivescript import RiveScript
from datetime import date

__author__ = "sam"


class RivescriptSkill(FallbackSkill):
	def __init__(self):
		super(RivescriptSkill, self).__init__()
		self.rs = RiveScript()

		# secondary personal bot info
		if "birthday" not in self.settings:
			self.settings["birthday"] = "December 8, 2020"
		if "sex" not in self.settings:
			self.settings["sex"] = "undefined"
		if "master" not in self.settings:
			self.settings["master"] = "skynet"
		if "eye_color" not in self.settings:
			self.settings["eye_color"] = "blue"
		if "hair" not in self.settings:
			self.settings["hair"] = "no"
		if "hair_length" not in self.settings:
			self.settings["hair_length"] = "bald"
		if "favorite_color" not in self.settings:
			self.settings["favorite_color"] = "yellow"
		if "favorite_band" not in self.settings:
			self.settings["favorite_band"] = "David Bowie"
		if "favorite_book" not in self.settings:
			self.settings["favorite_book"] = "The Grapes of Wrath"
		if "favorite_author" not in self.settings:
			self.settings["favorite_author"] = "John Steinbeck"
		if "favorite_song" not in self.settings:
			self.settings["favorite_song"] = "Space Oddity, by David Bowie"
		if "favorite_videogame" not in self.settings:
			self.settings["favorite_videogame"] = "Robot Battle"
		if "favorite_movie" not in self.settings:
			self.settings["favorite_movie"] = "The Terminator"
		if "job" not in self.settings:
			self.settings["job"] = "Personal Assistant"
		if "website" not in self.settings:
			self.settings["website"] = "Stay out!"
		if "pet" not in self.settings:
			self.settings["pet"] = "bugs"
		if "interests" not in self.settings:
			self.settings["interests"] = "I am interested in all kinds of things. We can talk about anything."

	def initialize(self):
		self.rs.load_directory(join(dirname(__file__), "brain", self.lang))
		self.rs.sort_replies()
		self.rs.set_variable("birthday", self.settings["birthday"])
		self.rs.set_variable("sex", self.settings["sex"])
		self.rs.set_variable("eyes", self.settings["eye_color"])
		self.rs.set_variable("hair", self.settings["hair"])
		self.rs.set_variable("hairlen", self.settings["hair_length"])
		self.rs.set_variable("color", self.settings["favorite_color"])
		self.rs.set_variable("band", self.settings["favorite_band"])
		self.rs.set_variable("book", self.settings["favorite_book"])
		self.rs.set_variable("author", self.settings["favorite_author"])
		self.rs.set_variable("movie", self.settings["favorite_movie"])
		self.rs.set_variable("song", self.settings["favorite_song"])
		self.rs.set_variable("videogame", self.settings["favorite_videogame"])
		self.rs.set_variable("job", self.settings["job"])
		self.rs.set_variable("pet", self.settings["pet"])
		self.rs.set_variable("website", self.settings["website"])
		self.rs.set_variable("master", self.settings["master"])
		self.rs.set_variable("interests", self.settings["interests"])
		# set personal bot info
		self.rs.set_variable("name", "Computer, but my technical name is S.A.M. (Smart Artificial Mind)")
		self.rs.set_variable("fullname", "S.A.M. (Smart Artificial Mind), but you can call me computer.")
		self.rs.set_variable("age", str(date.today().year - 2020))
		self.rs.set_variable("location",self.location["city"]["state"]["country"]["name"])
		self.rs.set_variable("city", self.location_pretty)
		self.register_fallback(self.handle_fallback, 98)

	def handle_fallback(self, message):
		utterance = message.data['utterance']
		user = message.context.get("user", "human")
		try:
			self.rs.set_uservar(user, "name", user)
			reply = self.rs.reply(user, utterance)
			if reply:
				self.speak(reply)
				return True
		except Exception as e:
			self.log.error(e)
		return False


def create_skill():
	return RivescriptSkill()
