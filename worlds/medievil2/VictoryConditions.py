from rule_builder.rules import Has, Rule


def defeat_demon_victory() -> Rule:
    return Has("Victory")
