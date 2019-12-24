sae_app_name = os.environ.get("APP_NAME", "")
if sae_app_name == "":
    #south support on SAE is not so good. May met problem. So do not use south in SAE
    INSTALLED_APPS += (
        'south',
    )