from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Languages(Base):
    __tablename__ = 'Languages'

    lang_id = Column(Integer, primary_key=True)
    lang_iso3 = Column(String, nullable=False)

class LanguagesTranslates(Base):
    __tablename__ = 'LanguagesTranslates'

    lang_trans_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    ltrans_cont = Column(String)

class LanguageLevels(Base):
    __tablename__ = 'LanguageLevels'

    llvl_id = Column(Integer, primary_key=True)
    llvl_cefr = Column(String, nullable=False)



class ContForms(Base):
    __tablename__ = 'ContForms'

    cform_id = Column(Integer, primary_key=True)
    cform_name = Column(String, nullable=False)

class ContFormsTranslates(Base):
    __tablename__ = 'ContFormsTranslates'

    cform_id = Column(Integer, ForeignKey('ContForms.cform_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cftrans_cont = Column(String)

class ContSizes(Base):
    __tablename__ = 'ContSizes'

    csize_id = Column(Integer, primary_key=True)
    csize_name = Column(String, nullable=False)

class ContSizesTranslates(Base):
    __tablename__ = 'ContSizesTranslates'

    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cstrans_cont = Column(String)

class ContSizeDescrTranslates(Base):

    __tablename__ = 'ContSizeDescrTranslates'

    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), primary_key=True)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    csdtrans_cont = Column(String)

class ContTypes(Base):
    __tablename__ = 'ContTypes'

    ctype_id = Column(Integer, primary_key=True)
    ctype_name = Column(String, nullable=False)

class ContTypesTranslates(Base):
    __tablename__ = 'ContTypesTranslates'

    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cttrans_cont = Column(String)

class ContGenres(Base):
    __tablename__ = 'ContGenres'

    cgenre_id = Column(Integer, primary_key=True)
    cgenre_name = Column(String, nullable=False)

class ContGenresTranslates(Base):
    __tablename__ = 'ContGenresTranslates'

    cgenre_id = Column(Integer, ForeignKey('ContGenres.cgenre_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cgtrans_cont = Column(String)

class ContTags(Base):
    __tablename__ = 'ContTags'

    ctag_id = Column(Integer, primary_key=True)
    ctag_name = Column(String, nullable=False)

class ContTagsTranslates(Base):
    __tablename__ = 'ContTagsTranslates'

    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    cttrans_cont = Column(String)

class Contents(Base):
    __tablename__ = 'Contents'

    cont_id = Column(Integer, primary_key=True)
    cont_cont = Column(Text, nullable=False)
    cform_id = Column(Integer, ForeignKey('ContForms.cform_id'), nullable=False)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), nullable=False)
    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), nullable=False)
    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'))
    cgenre_id = Column(Integer, ForeignKey('ContGenres.cgenre_id'))

class ContentsContTags(Base):
    __tablename__ = 'ContentsContTags'

    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)



class QnTypes(Base):
    __tablename__ = 'QnTypes'

    qtype_id = Column(Integer, primary_key=True)
    qtype_name = Column(String, nullable=False)

class QnTypesTranslates(Base):
    __tablename__ = 'QnTypesTranslates'

    qtype_id = Column(Integer, ForeignKey('QnTypes.qtype_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    qttrans_cont = Column(String)

class QnDepths(Base):
    __tablename__ = 'QnDepths'

    qdepth_id = Column(Integer, primary_key=True)
    qdepth_name = Column(String, nullable=False)

class Questions(Base):
    __tablename__ = 'Questions'

    qn_id = Column(Integer, primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), nullable=False)
    qn_content = Column(Text, nullable=False)
    qtype_id = Column(Integer, ForeignKey('QnTypes.qtype_id'))
    qdepth_id = Column(Integer, ForeignKey('QnDepths.qdepth_id'))




class Plans(Base):
    __tablename__ = 'Plans'

    plan_id = Column(Integer, primary_key=True)
    plan_name = Column(String, nullable=False)

class PlansTranslations(Base):
    __tablename__ = 'PlansTranslations'

    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    ptrans_cont = Column(String)

class PlanPrices(Base):
    __tablename__ = 'PlanPrices'

    pprice_id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), nullable=False)
    currency = Column(String, nullable=False)
    pprice_value = Column(Float)

class PlanLimits(Base):
    __tablename__ = 'PlanLimits'

    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    plimit_value = Column(Integer, nullable=False)

class PlanLimitDescrTranslates(Base):
    __tablename__ = 'PlanLimitDescrTranslates'

    plan_id = Column(Integer, ForeignKey('PlanLimits.plimit_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    llvl_id = Column(Integer, ForeignKey('LanguageLevels.lang_id'), primary_key=True)
    lang_id = Column(Integer, ForeignKey('Languages.lang_id'), primary_key=True)
    pldtrans_cont = Column(String)



class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    user_tg_id = Column(Integer, nullable=False)

class UsersRegistrations(Base):
    __tablename__ = 'UsersRegistrations'

    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    ureg_date = Column(String, nullable=False)

class UsersSettings(Base):
    __tablename__ = 'UsersSettings'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), nullable=False)
    main_lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    study_lang_id = Column(Integer, ForeignKey('Languages.lang_id'), nullable=False)
    study_llvl_id = Column(Integer, ForeignKey('LanguageLevels.llvl_id'), nullable=False)
    csize_id = Column(Integer, ForeignKey('ContSizes.csize_id'), nullable=False)
    user_interest = Column(Text)

class UsersContentTags(Base):
    __tablename__ = 'UsersContentTags'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    ctag_id = Column(Integer, ForeignKey('ContTags.ctag_id'), primary_key=True)

class UsersPayments(Base):
    __tablename__ = 'UsersPayments'

    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    plan_id = Column(Integer, ForeignKey('Plans.plan_id'), nullable=False)
    upay_date = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    payment_value = Column(Float, nullable=False)

class UserLimits(Base):
    __tablename__ = 'UserLimits'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    ctype_id = Column(Integer, ForeignKey('ContTypes.ctype_id'), primary_key=True)
    ulimit_value = Column(Integer, nullable=False)

class UserContents(Base):
    __tablename__ = 'UserContents'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    cont_id = Column(Integer, ForeignKey('Contents.cont_id'), primary_key=True)
    ucont_iter = Column(Integer, primary_key=True)
    cont_send_date = Column(String, nullable=False)
    cont_difficult_rate = Column(Integer)
    cont_interest_rate = Column(Integer)

class RespCorrects(Base):
    __tablename__ = 'RespCorrects'

    rcorr_id = Column(Integer, primary_key=True)
    rcorr_name = Column(String, nullable=False)

class UserQuestions(Base):
    __tablename__ = 'UserQuestions'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    qn_id = Column(Integer, ForeignKey('Questions.qn_id'), primary_key=True)
    uqn_iter = Column(Integer, primary_key=True)
    qn_send_time = Column(String, nullable=False)
    uqn_resp = Column(String)
    uqn_resp_time = Column(String)
    rcorr_id = Column(Integer, ForeignKey('RespCorrects.rcorr_id'))
    gpt_resp = Column(String)
    gpt_resp_time = Column(String)
