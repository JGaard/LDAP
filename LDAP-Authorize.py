import ldap, sys
import ldap.modlist as modlist

def LDAPauthorize():
    ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    server = AD_SERVER
    
    l = ldap.initialize(server)
    l.protocol_version=ldap.VERSION3
    l.start_tls_s()
    
    l.bind_s(ADMIN_LOGIN, ADMIN_PASS)
    
    return l
    
