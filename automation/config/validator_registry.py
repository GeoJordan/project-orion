from validators.asset_validator import AssetValidator
from validators.cmdb_validator import CMDBValidator
from validators.ipam_validator import IPAMValidator
from validators.firmware_validator import FirmwareValidator

VALIDATOR_REGISTRY = {
    "CMDBValidator": CMDBValidator,
    "AssetValidator": AssetValidator,
    "IPAMValidator": IPAMValidator,
    "FirmwareValidator": FirmwareValidator,
}