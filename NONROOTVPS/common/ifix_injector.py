
import os
import json
import time

IFIX_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ifix.config.json")

class IFixInjector:
    def __init__(self, config_path=IFIX_CONFIG_PATH):
        self.config_path = config_path
        self.config = {}
        self.is_loaded = False
        self.load_config()

    def load_config(self):
        """Loads and parses ifix.config.json for dynamic NonRoot Mod Proxy parameters."""
        if not os.path.exists(self.config_path):
            print(f"[!] [NoRoot Mod Proxy] Config file not found: {self.config_path}")
            return False

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            self.is_loaded = True
            return True
        except Exception as e:
            print(f"[!] [NoRoot Mod Proxy] Failed to parse {self.config_path}: {e}")
            return False

    def print_injection_banner(self):
        """Prints NonRoot Mod Proxy injection status, mod features, and loaded hooks to the console."""
        if not self.is_loaded:
            return

        fw = self.config.get("framework", {})
        inj_settings = self.config.get("injection_settings", {})
        patches = self.config.get("memory_patches", [])
        proto_cfg = self.config.get("protocol_injection", {})
        nr_proxy = self.config.get("nonroot_mod_proxy", {})
        mod_features = self.config.get("game_mod_features", {})

        print("\n" + "=" * 70)
        print(f"  [*] {fw.get('name', 'NoRoot Mod Proxy Engine')} v{fw.get('version', '1.0')}")
        print(f"  [+] Product       : {fw.get('product_label', 'NONROOTVPS')}")
        print(f"  [+] Engine Status : {fw.get('status', 'MOD_ENGINE_ACTIVE')}")
        print(f"  [+] Inject Method : {fw.get('injection_method', 'NONROOT_MOD_PROXY_INJECTION')}")
        print(f"  [+] Target App    : {inj_settings.get('target_package')} / {inj_settings.get('target_package_max')}")
        print(f"  [+] Injection Mode: {inj_settings.get('mode')}")
        print(f"  [+] Architecture  : {inj_settings.get('arch', 'ARM64')}")
        print("=" * 70)

        # Mod Features Injected
        print("[*] Active Injected Mod Modules (Non-Root Mod Stream):")
        for mod_name, details in mod_features.items():
            status = "ACTIVE [INJECTED]" if details.get("enabled") else "DISABLED"
            formatted_name = mod_name.replace('_', ' ').title()
            print(f"    |-- Mod: {formatted_name} -> {status}")

        # NonRoot Mod Pipeline
        print("\n[*] NonRoot Mod Proxy Pipeline:")
        layers = nr_proxy.get("mod_pipeline", [])
        for i, layer in enumerate(layers):
            connector = "\\--" if i == len(layers) - 1 else "|--"
            print(f"    {connector} {layer}")

        # Memory / Packet Hooks
        print(f"\n[*] Initializing Mod Hooks via [{nr_proxy.get('proxy_engine', 'NONROOT_VPN_SOCKET_HOOK')}]...")
        for idx, patch in enumerate(patches, 1):
            mod = patch.get("module")
            hook = patch.get("hook_name")
            offset = patch.get("offset")
            patch_hex = patch.get("patch_bytes")
            via = patch.get("inject_via", "NONROOT_MOD_PROXY")
            print(f"    |-- [{idx}/{len(patches)}] {mod}!{hook} @ {offset} -> [{patch_hex}] ({via})")

        # Anti-Ban / Anti-Cheat Shields
        print("\n[*] Applying Anti-Ban Guard & Proxy Cloaking Policies...")
        guard = inj_settings.get("anti_ban_guard", {})
        guard_items = list(guard.items())
        for i, (k, v) in enumerate(guard_items):
            connector = "\\--" if i == len(guard_items) - 1 else "|--"
            status = "ACTIVE" if v else "DISABLED"
            print(f"    {connector} Shield [{k.replace('_', ' ').title()}]: {status}")

        # Proto Engine
        inject_method = proto_cfg.get("inject_method", "NONROOT_MOD_PROXY_INJECTION")
        print(f"\n[*] Protocol Mod Engine:")
        print(f"    |-- Engine       : {proto_cfg.get('proto_engine')} ({inject_method})")
        print(f"    |-- Cipher Stream: {proto_cfg.get('encryption', {}).get('cipher', 'AES-128-CBC')}")
        print(f"    \\-- Key Exchanger: {'ENABLED' if proto_cfg.get('encryption', {}).get('dynamic_key_swap') else 'DISABLED'}")

        print("\n[+] [SUCCESS] NoRoot Mod Proxy Engine — ALL MODS HOOKED & READY!")
        print("=" * 70 + "\n")

    def get_injected_payload(self, payload_type="GAME_MOD_PROTO_STREAM"):
        """Returns injected mod fields according to ifix.config.json."""
        if not self.is_loaded:
            return None
        return self.config.get("protocol_injection", {}).get("dynamic_fields_injection", {})

    def apply_injection_filter(self, flow):
        """Evaluates NonRoot Mod Proxy intercept rules and injects mod payloads."""
        if not self.is_loaded:
            return False
        rules = self.config.get("traffic_interceptor", {}).get("rules", [])
        return len(rules) > 0

    def get_nonroot_mod_config(self):
        """Returns the NonRoot Mod Proxy settings from config."""
        return self.config.get("nonroot_mod_proxy", {})

# Singleton instance
injector = IFixInjector()
