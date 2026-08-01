from validators.asset_validator import AssetValidator
from validators.cmdb_validator import CMDBValidator

VALIDATOR_REGISTRY = {
    "CMDBValidator": CMDBValidator,
    "AssetValidator": AssetValidator,
}