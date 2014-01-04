import ldap, sys
import ldap.modlist as modlist
import datetime, time

def LDAPauthorize():
    ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    server = AD_SERVER
    
    l = ldap.initialize(server)
    l.protocol_version=ldap.VERSION3
    l.start_tls_s()
    
    l.bind_s(ADMIN_LOGIN, ADMIN_PASS)
    
    return l

def deactivateLastLogonPriorTo(year, month, day):
    l = LDAPauthorize()
    
    for org in LOCAL_DOMAINS: #<--Optional, for orginization/multiple domains
        base_dn = 'OU=' + str(org) + ',DC=9thStreet,DC=internal' 
        filter = '(&(objectCategory=person)(objectClass=user)(lastLogonTimestamp<=' + str(dateTimetoLargeInt(year, month, day)) + '))'
        attrs = []

    for i in l.search_s( base_dn, ldap.SCOPE_SUBTREE, filter, attrs ):
        mod_attrs = [( ldap.MOD_REPLACE, 'userAccountControl', '514')]
        l.modify_s(i[0], mod_attrs)

def dateTimetoLargeInt(year, month, day):
    seconds_in_year = 31556900
    epoch_time_no_subseconds = int(convertDate(year, month, day))
    LargeIntTime = (seconds_in_year * (1969 - 1600) + (epoch_time_no_subseconds - 22500)) * 10000000
    return LargeIntTime

def convertDate(year, month, day):
    date = datetime.datetime(year, month, day)
    return time.mktime(date.timetuple())
