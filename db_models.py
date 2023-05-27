from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Languages(Base):
    __tablename__ = 'Languages'

    lang_id = Column(Integer, primary_key=True)
    lang_iso3 = Column(String, nullable=False, unique=True)

class LanguagesTranslates(Base):
    __tablename__ = 'LanguagesTranslates'

    lang_trans_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    ltrans_cont = Column(String, nullable=True)

class LanguageLevels(Base):
    __tablename__ = 'LanguageLevels'

    llvl_id = Column(Integer, primary_key=True)
    llvl_cefr = Column(String, nullable=False, unique=True)



class ContForms(Base):
    __tablename__ = 'ContForms'

    cform_id = Column(Integer, primary_key=True)
    cform_name = Column(String, nullable=False, unique=True)

class ContFormsTranslates(Base):
    __tablename__ = 'ContFormsTranslates'

    cform_id = Column(Integer, ForeignKey('ContForms.cform_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cftrans_cont = Column(String, nullable=True)

class ContSizes(Base):
    __tablename__ = 'ContSizes'

    csize_id = Column(Integer, primary_key=True)
    csize_name = Column(String, nullable=False, unique=True)

class ContSizesTranslates(Base):
    __tablename__ = 'ContSizesTranslates'

    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cstrans_cont = Column(String, nullable=True)

class ContSizeDescrTranslates(Base):

    __tablename__ = 'ContSizeDescrTranslates'

    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), primary_key=True)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    csdtrans_cont = Column(String, nullable=True)

class ContTypes(Base):
    __tablename__ = 'ContTypes'

    ctype_id = Column(Integer, primary_key=True)
    ctype_name = Column(String, nullable=False, unique=True)

class ContTypesTranslates(Base):
    __tablename__ = 'ContTypesTranslates'

    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cttrans_cont = Column(String, nullable=True)

class ContGenres(Base):
    __tablename__ = 'ContGenres'

    cgenre_id = Column(Integer, primary_key=True)
    cgenre_name = Column(String, nullable=False, unique=True)

class ContGenresTranslates(Base):
    __tablename__ = 'ContGenresTranslates'

    cgenre_id = Column(Integer, ForeignKey('ContGenres.cgenre_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cgtrans_cont = Column(String, nullable=True)

class ContTags(Base):
    __tablename__ = 'ContTags'

    ctag_id = Column(Integer, primary_key=True)
    ctag_name = Column(String, nullable=False, unique=True)

class ContTagsTranslates(Base):
    __tablename__ = 'ContTagsTranslates'

    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cttrans_cont = Column(String, nullable=True)

class Contents(Base):
    __tablename__ = 'Contents'

    cont_id = Column(Integer, primary_key=True)
    cont_cont = Column(Text, nullable=False)
    cform_id = Column(Integer, ForeignKey('ContForms.cform_id'), nullable=False)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), nullable=False)
    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), nullable=False)
    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'), nullable=True)
    cgenre_id = Column(Integer, ForeignKey('ContGenres.cgenre_id'), nullable=True)

class ContentsContTags(Base):
    __tablename__ = 'ContentsContTags'

    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)



class PractTypes(Base):
    __tablename__ = 'PractTypes'

    ptype_id = Column(Integer, primary_key=True)
    ptype_name = Column(String, nullable=False, unique=True)

class PractTypesTranslates(Base):
    __tablename__ = 'PractTypesTranslates'

    ptype_id = Column(Integer, ForeignKey('PractTypes.ptype_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    pttrans_cont = Column(String, nullable=True)

class PractDepths(Base):
    __tablename__ = 'PractDepths'

    pdepth_id = Column(Integer, primary_key=True)
    pdepth_name = Column(String, nullable=False, unique=True)

class Practices(Base):
    __tablename__ = 'Practices'

    pract_id = Column(Integer, primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), nullable=False)
    pract_cont = Column(Text, nullable=False)
    ptype_id = Column(Integer, ForeignKey('PractTypes.ptype_id'), nullable=True)
    pdepth_id = Column(Integer, ForeignKey('PractDepths.pdepth_id'), nullable=True)




class Plans(Base):
    __tablename__ = 'Plans'

    plan_id = Column(Integer, primary_key=True)
    plan_name = Column(String, nullable=False, unique=True)

class PlansTranslations(Base):
    __tablename__ = 'PlansTranslations'

    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    ptrans_cont = Column(String, nullable=True)

class PlanPrices(Base):
    __tablename__ = 'PlanPrices'

    pprice_id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), nullable=False)
    currency = Column(String, nullable=False)
    pprice_value = Column(Float, nullable=True)

class PlanLimits(Base):
    __tablename__ = 'PlanLimits'

    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    plimit_value = Column(Integer, nullable=False)

class PlanLimitDescrTranslates(Base):
    __tablename__ = 'PlanLimitDescrTranslates'

    plan_id = Column(Integer, ForeignKey('PlanLimits.plimit_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    pldtrans_cont = Column(String, nullable=True)



class Users(Base):  
  __tablename__ = 'Users'  

  user_id = Column(Integer, primary_key=True)  
  user_tg_id = Column(Integer, nullable=False)
  
  registrations = relationship('UsersRegistrations', back_populates='user')
  settings = relationship('UsersSettings', back_populates='user', uselist=False)
  cont_tags = relationship('UsersContTags', back_populates='user')
  payments = relationship('UsersPayments', back_populates='user')
  limits = relationship('UserLimits', back_populates='user')
  contents = relationship('UserContents', back_populates='user')
  practices = relationship('UserPractices', back_populates='user')

class UsersRegistrations(Base):
    __tablename__ = 'UsersRegistrations'

    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    ureg_date = Column(DateTime, nullable=False)

    user = relationship('Users', back_populates='registrations')


class UsersSettings(Base):
    __tablename__ = 'UsersSettings'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), nullable=False)
    main_lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    study_lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    study_llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), nullable=False)
    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), nullable=False)
    user_interest = Column(Text, nullable=True)

    user = relationship('Users', back_populates='settings')


class UsersContTags(Base):
    __tablename__ = 'UsersContTags'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)

    user = relationship('Users', back_populates='cont_tags')

class UsersPayments(Base):
    __tablename__ = 'UsersPayments'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), primary_key=True)
    upay_iter = Column(Integer, primary_key=True)
    upay_date = Column(DateTime, nullable=False)
    currency = Column(String, nullable=False)
    payment_value = Column(Float, nullable=False)

    user = relationship('Users', back_populates='payments')

class UserLimits(Base):
    __tablename__ = 'UserLimits'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'), primary_key=True)
    ulimit_value = Column(Integer, nullable=False)

    user = relationship('Users', back_populates='limits')

class UserContents(Base):
    __tablename__ = 'UserContents'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    ucont_iter = Column(Integer, primary_key=True)
    cont_send_date = Column(DateTime, nullable=False)
    cont_difficult_rate = Column(Integer, nullable=True)
    cont_interest_rate = Column(Integer, nullable=True)

    user = relationship('Users', back_populates='contents')

class UserResponses(Base):
    __tablename__ = 'UserPractices'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    pract_id = Column(Integer, ForeignKey('Practices.pract_id'), primary_key=True)
    uresp_iter = Column(Integer, primary_key=True)
    pract_send_time = Column(DateTime, nullable=False)
    uresp_cont = Column(String, nullable=True)
    uresp_resp_time = Column(DateTime, nullable=True)
    uresp_correct = Column(String, nullable=True)
    gpt_resp = Column(String, nullable=True)
    gpt_resp_time = Column(DateTime, nullable=True)

    user = relationship('Users', back_populates='practices')
