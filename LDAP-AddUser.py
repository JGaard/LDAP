import ldap, sys
impoty ldap.modlist as modlist

def LDAPauthorize():
    ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    server = AD_SERVER
    
    l = ldap.initialize(server)
    l.protocol_version=ldap.VERSION3
    l.start_tls_s()
    
    l.bind_s(ADMIN_LOGIN, ADMIN_PASS)
    
    return l
    
def addUser(username, firstname, surname, email, password, organization):
    
    l = LDAPauthorize()

    dn = 'CN=' +firstname + ' ' + surname + ',OU=' + organization + ',' + LOCAL_DC
    password_value = unicode_pass.encode('utf-16-le')
    
    attrs = {}
    attrs['objectclass'] = "user"
    attrs['uid'] = username
    attrs['sAMAccountname'] = username
    attrs['sn'] = surname
    attrs['givenName'] = firstname
    attrs['cn'] = firstname + ' ' + surname
    attrs['displayName'] = firstname + ' ' + surname
    attrs['mail'] = email
    attrs['company'] = organization
    attrs['userPrincipalName'] = username + LOCAL_DC_PATH
    attrs['unicodePwd'] = password_value
    attrs['userAccountControl'] = '66048' #<-- SUBJECT TO CHANGE BASED ON NEW USER REQUIREMENTS; SEE ARTICLE ON AD FLAGS 
    
    ldif = modlist.addModlist(attrs)
    l.add_s(dn, ldif)
