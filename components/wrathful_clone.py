import customtkinter as ctk
from utils.widgets import Widgets
from utils.objects.item import Item


class WrathfulClone:
    @staticmethod
    def show_component(tab, database):
        _tab = ctk.CTkFrame(tab, fg_color="transparent")
        _tab.pack(side="top", padx=10, pady=20)

        _tab.items = []
        _tab.entries = {}

        Widgets.header(
            _tab,
            "Wrathful Clone",
            """This will clone all Wrathful items and will multiply their stats. 
            \nMake sure your starting entry and the following 208 entries are not in use. 
            \nPrefix is the text that will replace Wrathful in the item name.
            \nMultipliers are float representations of percentages 101% = 1.01, 150% = 1.5, 200% = 2.0, ect.
            \nIf you want to reduce a stat, use a number less than 1.0. 50% = 0.5, 25% = 0.25, ect.
            \nOnly thing you have to do now is change the display ids.""",
        )
        row_one = ctk.CTkFrame(_tab, fg_color="transparent")
        row_one.pack(side="top", padx=0, pady=5)

        row_two = ctk.CTkFrame(_tab, fg_color="transparent")
        row_two.pack(side="top", padx=0, pady=0)

        entry_names = [
            ("wrath_entry", "Starting Entry", row_one),
            ("wrath_prefix", "Name Prefix", row_one),
            ("wrath_stat", "Stat Multiplier", row_one),
            ("wrath_dmg", "Damage Multiplier", row_two),
            ("wrath_armor", "Armor Multiplier", row_two),
            ("wrath_block", "Block Multiplier", row_two),
        ]

        for name, text, parent in entry_names:
            Widgets.custom_entry(parent, _tab.entries, name, text, 6, 6, 120)

        def command():
            WrathfulClone.wrathful_fetch(
                _tab,
                database,
                _tab.entries["wrath_entry"].get(),
                _tab.entries["wrath_prefix"].get(),
                _tab.entries["wrath_stat"].get(),
                _tab.entries["wrath_dmg"].get(),
                _tab.entries["wrath_armor"].get(),
                _tab.entries["wrath_block"].get(),
            )

        btn = ctk.CTkButton(tab, text="Create Clone", width=400, command=command)
        btn.pack(side="top", padx=10, pady=0)

    @staticmethod
    def wrathful_fetch(
        tab,
        database,
        entry,
        prefix,
        stat_multiplier,
        dmg_multiplier,
        armor_multiplier,
        block_multiplier,
    ):
        query = "SELECT * FROM item_template WHERE NAME LIKE 'Wrathful %'"
        results = database.fetch(query)
        tab.items.clear()

        for row in results:
            item = Item(
                entry=row["entry"],
                class_=row["class"],
                subclass=row["subclass"],
                sound_override_subclass=row["SoundOverrideSubclass"],
                name=row["name"],
                display_id=row["displayid"],
                quality=row["Quality"],
                flags=row["Flags"],
                flags_extra=row["FlagsExtra"],
                buy_count=row["BuyCount"],
                buy_price=row["BuyPrice"],
                sell_price=row["SellPrice"],
                inventory_type=row["InventoryType"],
                allowable_class=row["AllowableClass"],
                allowable_race=row["AllowableRace"],
                item_level=row["ItemLevel"],
                required_level=row["RequiredLevel"],
                required_skill=row["RequiredSkill"],
                required_skill_rank=row["RequiredSkillRank"],
                required_spell=row["requiredspell"],
                required_honor_rank=row["requiredhonorrank"],
                required_city_rank=row["RequiredCityRank"],
                required_reputation_faction=row["RequiredReputationFaction"],
                required_reputation_rank=row["RequiredReputationRank"],
                max_count=row["maxcount"],
                stackable=row["stackable"],
                container_slots=row["ContainerSlots"],
                stats_count=row["StatsCount"],
                stat_type1=row["stat_type1"],
                stat_value1=row["stat_value1"],
                stat_type2=row["stat_type2"],
                stat_value2=row["stat_value2"],
                stat_type3=row["stat_type3"],
                stat_value3=row["stat_value3"],
                stat_type4=row["stat_type4"],
                stat_value4=row["stat_value4"],
                stat_type5=row["stat_type5"],
                stat_value5=row["stat_value5"],
                stat_type6=row["stat_type6"],
                stat_value6=row["stat_value6"],
                stat_type7=row["stat_type7"],
                stat_value7=row["stat_value7"],
                stat_type8=row["stat_type8"],
                stat_value8=row["stat_value8"],
                stat_type9=row["stat_type9"],
                stat_value9=row["stat_value9"],
                stat_type10=row["stat_type10"],
                stat_value10=row["stat_value10"],
                scaling_stat_distribution=row["ScalingStatDistribution"],
                scaling_stat_value=row["ScalingStatValue"],
                dmg_min1=row["dmg_min1"],
                dmg_max1=row["dmg_max1"],
                dmg_type1=row["dmg_type1"],
                dmg_min2=row["dmg_min2"],
                dmg_max2=row["dmg_max2"],
                dmg_type2=row["dmg_type2"],
                armor=row["armor"],
                holy_res=row["holy_res"],
                fire_res=row["fire_res"],
                nature_res=row["nature_res"],
                frost_res=row["frost_res"],
                shadow_res=row["shadow_res"],
                arcane_res=row["arcane_res"],
                delay=row["delay"],
                ammo_type=row["ammo_type"],
                ranged_mod_range=row["RangedModRange"],
                spell_id1=row["spellid_1"],
                spell_trigger1=row["spelltrigger_1"],
                spell_charges1=row["spellcharges_1"],
                spell_ppm_rate1=row["spellppmRate_1"],
                spell_cooldown1=row["spellcooldown_1"],
                spell_category1=row["spellcategory_1"],
                spell_category_cooldown1=row["spellcategorycooldown_1"],
                spell_id2=row["spellid_2"],
                spell_trigger2=row["spelltrigger_2"],
                spell_charges2=row["spellcharges_2"],
                spell_ppm_rate2=row["spellppmRate_2"],
                spell_cooldown2=row["spellcooldown_2"],
                spell_category2=row["spellcategory_2"],
                spell_category_cooldown2=row["spellcategorycooldown_2"],
                spell_id3=row["spellid_3"],
                spell_trigger3=row["spelltrigger_3"],
                spell_charges3=row["spellcharges_3"],
                spell_ppm_rate3=row["spellppmRate_3"],
                spell_cooldown3=row["spellcooldown_3"],
                spell_category3=row["spellcategory_3"],
                spell_category_cooldown3=row["spellcategorycooldown_3"],
                spell_id4=row["spellid_4"],
                spell_trigger4=row["spelltrigger_4"],
                spell_charges4=row["spellcharges_4"],
                spell_ppm_rate4=row["spellppmRate_4"],
                spell_cooldown4=row["spellcooldown_4"],
                spell_category4=row["spellcategory_4"],
                spell_category_cooldown4=row["spellcategorycooldown_4"],
                spell_id5=row["spellid_5"],
                spell_trigger5=row["spelltrigger_5"],
                spell_charges5=row["spellcharges_5"],
                spell_ppm_rate5=row["spellppmRate_5"],
                spell_cooldown5=row["spellcooldown_5"],
                spell_category5=row["spellcategory_5"],
                spell_category_cooldown5=row["spellcategorycooldown_5"],
                bonding=row["bonding"],
                description=row["description"],
                page_text=row["PageText"],
                language_id=row["LanguageID"],
                page_material=row["PageMaterial"],
                start_quest=row["startquest"],
                lock_id=row["lockid"],
                material=row["Material"],
                sheath=row["sheath"],
                random_property=row["RandomProperty"],
                random_suffix=row["RandomSuffix"],
                block=row["block"],
                item_set=row["itemset"],
                max_durability=row["MaxDurability"],
                area=row["area"],
                map_=row["Map"],
                bag_family=row["BagFamily"],
                totem_category=row["TotemCategory"],
                socket_color1=row["socketColor_1"],
                socket_content1=row["socketContent_1"],
                socket_color2=row["socketColor_2"],
                socket_content2=row["socketContent_2"],
                socket_color3=row["socketColor_3"],
                socket_content3=row["socketContent_3"],
                socket_bonus=row["socketBonus"],
                gem_properties=row["GemProperties"],
                required_disenchant_skill=row["RequiredDisenchantSkill"],
                armor_damage_modifier=row["ArmorDamageModifier"],
                duration=row["duration"],
                item_limit_category=row["ItemLimitCategory"],
                holiday_id=row["HolidayId"],
                script_name=row["ScriptName"],
                disenchant_id=row["DisenchantID"],
                food_type=row["FoodType"],
                min_money_loot=row["minMoneyLoot"],
                max_money_loot=row["maxMoneyLoot"],
                flags_custom=row["flagsCustom"],
                verified_build=row["VerifiedBuild"],
            )

            tab.items.append(item)

        WrathfulClone.wrathful_multiply(
            tab,
            database,
            entry,
            prefix,
            stat_multiplier,
            dmg_multiplier,
            armor_multiplier,
            block_multiplier,
        )

    @staticmethod
    def wrathful_multiply(
        tab,
        database,
        entry,
        prefix,
        stat_multiplier,
        dmg_multiplier,
        armor_multiplier,
        block_multiplier,
    ):
        start_entry = int(entry)
        for item in tab.items:
            item.entry = start_entry
            start_entry += 1
            item.name = item.name.replace("Wrathful", prefix)
            item.stat_value1 = int(item.stat_value1) * float(stat_multiplier)
            item.stat_value2 = int(item.stat_value2) * float(stat_multiplier)
            item.stat_value3 = int(item.stat_value3) * float(stat_multiplier)
            item.stat_value4 = int(item.stat_value4) * float(stat_multiplier)
            item.stat_value5 = int(item.stat_value5) * float(stat_multiplier)
            item.stat_value6 = int(item.stat_value6) * float(stat_multiplier)
            item.stat_value7 = int(item.stat_value7) * float(stat_multiplier)
            item.stat_value8 = int(item.stat_value8) * float(stat_multiplier)
            item.stat_value9 = int(item.stat_value9) * float(stat_multiplier)
            item.stat_value10 = int(item.stat_value10) * float(stat_multiplier)
            item.dmg_min1 = int(item.dmg_min1) * float(dmg_multiplier)
            item.dmg_max1 = int(item.dmg_max1) * float(dmg_multiplier)
            item.dmg_min2 = int(item.dmg_min2) * float(dmg_multiplier)
            item.dmg_max2 = int(item.dmg_max2) * float(dmg_multiplier)
            item.armor = int(item.armor) * float(armor_multiplier)
            item.block = int(item.block) * float(block_multiplier)

        WrathfulClone.wrathful_insert(tab, database)

    @staticmethod
    def wrathful_insert(tab, database):
        queries = []

        for item in tab.items:
            item.name = item.name.replace("'", "\\'")
            query = f"""INSERT INTO `item_template` (`entry`, `class`, `subclass`, `SoundOverrideSubclass`, `name`, `displayid`, `Quality`, `Flags`, `FlagsExtra`, `BuyCount`, `BuyPrice`, `SellPrice`, `InventoryType`, `AllowableClass`, `AllowableRace`, `ItemLevel`, `RequiredLevel`, `RequiredSkill`, `RequiredSkillRank`, `requiredspell`, `requiredhonorrank`, `RequiredCityRank`, `RequiredReputationFaction`, `RequiredReputationRank`, `maxcount`, `stackable`, `ContainerSlots`, `StatsCount`, `stat_type1`, `stat_value1`, `stat_type2`, `stat_value2`, `stat_type3`, `stat_value3`, `stat_type4`, `stat_value4`, `stat_type5`, `stat_value5`, `stat_type6`, `stat_value6`, `stat_type7`, `stat_value7`, `stat_type8`, `stat_value8`, `stat_type9`, `stat_value9`, `stat_type10`, `stat_value10`, `ScalingStatDistribution`, `ScalingStatValue`, `dmg_min1`, `dmg_max1`, `dmg_type1`, `dmg_min2`, `dmg_max2`, `dmg_type2`, `armor`, `holy_res`, `fire_res`, `nature_res`, `frost_res`, `shadow_res`, `arcane_res`, `delay`, `ammo_type`, `RangedModRange`, `spellid_1`, `spelltrigger_1`, `spellcharges_1`, `spellppmRate_1`, `spellcooldown_1`, `spellcategory_1`, `spellcategorycooldown_1`, `spellid_2`, `spelltrigger_2`, `spellcharges_2`, `spellppmRate_2`, `spellcooldown_2`, `spellcategory_2`, `spellcategorycooldown_2`, `spellid_3`, `spelltrigger_3`, `spellcharges_3`, `spellppmRate_3`, `spellcooldown_3`, `spellcategory_3`, `spellcategorycooldown_3`, `spellid_4`, `spelltrigger_4`, `spellcharges_4`, `spellppmRate_4`, `spellcooldown_4`, `spellcategory_4`, `spellcategorycooldown_4`, `spellid_5`, `spelltrigger_5`, `spellcharges_5`, `spellppmRate_5`, `spellcooldown_5`, `spellcategory_5`, `spellcategorycooldown_5`, `bonding`, `description`, `PageText`, `LanguageID`, `PageMaterial`, `startquest`, `lockid`, `Material`, `sheath`, `RandomProperty`, `RandomSuffix`, `block`, `itemset`, `MaxDurability`, `area`, `Map`, `BagFamily`, `TotemCategory`, `socketColor_1`, `socketContent_1`, `socketColor_2`, `socketContent_2`, `socketColor_3`, `socketContent_3`, `socketBonus`, `GemProperties`, `RequiredDisenchantSkill`, `ArmorDamageModifier`, `duration`, `ItemLimitCategory`, `HolidayId`, `ScriptName`, `DisenchantID`, `FoodType`, `minMoneyLoot`, `maxMoneyLoot`, `flagsCustom`, `VerifiedBuild`) VALUES ({item.entry}, {item.class_}, {item.subclass}, {item.sound_override_subclass}, '{item.name}', {item.display_id}, {item.quality}, {item.flags}, {item.flags_extra}, {item.buy_count}, {item.buy_price}, {item.sell_price}, {item.inventory_type}, {item.allowable_class}, {item.allowable_race}, {item.item_level}, {item.required_level}, {item.required_skill}, {item.required_skill_rank}, {item.required_spell}, {item.required_honor_rank}, {item.required_city_rank}, {item.required_reputation_faction}, {item.required_reputation_rank}, {item.max_count}, {item.stackable}, {item.container_slots}, {item.stats_count}, {item.stat_type1}, {item.stat_value1}, {item.stat_type2}, {item.stat_value2}, {item.stat_type3}, {item.stat_value3}, {item.stat_type4}, {item.stat_value4}, {item.stat_type5}, {item.stat_value5}, {item.stat_type6}, {item.stat_value6}, {item.stat_type7}, {item.stat_value7}, {item.stat_type8}, {item.stat_value8}, {item.stat_type9}, {item.stat_value9}, {item.stat_type10}, {item.stat_value10}, {item.scaling_stat_distribution}, {item.scaling_stat_value}, {item.dmg_min1}, {item.dmg_max1}, {item.dmg_type1}, {item.dmg_min2}, {item.dmg_max2}, {item.dmg_type2}, {item.armor}, {item.holy_res}, {item.fire_res}, {item.nature_res}, {item.frost_res}, {item.shadow_res}, {item.arcane_res}, {item.delay}, {item.ammo_type}, {item.ranged_mod_range}, {item.spell_id1}, {item.spell_trigger1}, {item.spell_charges1}, {item.spell_ppm_rate1}, {item.spell_cooldown1}, {item.spell_category1}, {item.spell_category_cooldown1}, {item.spell_id2}, {item.spell_trigger2}, {item.spell_charges2}, {item.spell_ppm_rate2}, {item.spell_cooldown2}, {item.spell_category2}, {item.spell_category_cooldown2}, {item.spell_id3}, {item.spell_trigger3}, {item.spell_charges3}, {item.spell_ppm_rate3}, {item.spell_cooldown3}, {item.spell_category3}, {item.spell_category_cooldown3}, {item.spell_id4}, {item.spell_trigger4}, {item.spell_charges4}, {item.spell_ppm_rate4}, {item.spell_cooldown4}, {item.spell_category4}, {item.spell_category_cooldown4}, {item.spell_id5}, {item.spell_trigger5}, {item.spell_charges5}, {item.spell_ppm_rate5}, {item.spell_cooldown5}, {item.spell_category5}, {item.spell_category_cooldown5}, {item.bonding}, '{item.description}', {item.page_text}, {item.language_id}, {item.page_material}, {item.start_quest}, {item.lock_id}, {item.material}, {item.sheath}, {item.random_property}, {item.random_suffix}, {item.block}, {item.item_set}, {item.max_durability}, {item.area}, {item.map_}, {item.bag_family}, {item.totem_category}, {item.socket_color1}, {item.socket_content1}, {item.socket_color2}, {item.socket_content2}, {item.socket_color3}, {item.socket_content3}, {item.socket_bonus}, {item.gem_properties}, {item.required_disenchant_skill}, {item.armor_damage_modifier}, {item.duration}, {item.item_limit_category}, {item.holiday_id}, '{item.script_name}', {item.disenchant_id}, {item.food_type}, {item.min_money_loot}, {item.max_money_loot}, {item.flags_custom}, {item.verified_build})"""
            queries.append(query)

        database.execute_many(queries)
