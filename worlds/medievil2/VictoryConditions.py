from rule_builder.rules import CanReachLocation, Rule


def defeat_demon_victory() -> Rule:
    return CanReachLocation("Cleared: The Demon")
