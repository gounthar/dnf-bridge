import dnfbridge.providers

# FIXME should warn/error when selected preferred does not RPROVIDES pkg
# FIXME should pick a default one in absence of PREFERRED_
def resolve_virtual_runtime_dep(d, pkg):
    if pkg.startswith("virtual/"):
        preferred_rpm_rproviders = dnfbridge.providers.preferred_rpm_rproviders(d)
        preferred = preferred_rpm_rproviders.get(pkg, None)
        if preferred is not None:
            return preferred

        bb.error(f"PREFERRED_RPM_RPROVIDERS not set for '{pkg}', dependency graph will be incomplete")

    return pkg
