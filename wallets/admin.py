
from django.contrib import admin
from wallets.models import *


@admin.register(PairContract)
class PairContractAdmin(admin.ModelAdmin):
    list_display = ["dex", "token", "pair", "chain"]


@admin.register(PoolContract)
class PoolContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("name", "address", )


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    search_fields = ("address", )


@admin.register(TargetWallet)
class TargetWalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ("wallet", )
    list_display = ("transaction_hash", "timestamp", "token_in", "amount", "percent", "wallet", )



