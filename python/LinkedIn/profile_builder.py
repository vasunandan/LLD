from profile import Profile

class ProfileBuilder:
    def __init__(self,profile):
        self.profile = profile
    def set_picture(self,picture):
        self.profile.picture = picture
        return self
    def set_headline(self,headline):
        self.profile.headline = headline
        return self
    def set_summary(self,summary):
        self.profile.summary = summary
        return self
    def set_experience(self,exp):
        self.profile.experience = exp
        return self
    def set_education(self,edu):
        self.profile.education = edu
        return self
    def build(self):
        return self.profile
        