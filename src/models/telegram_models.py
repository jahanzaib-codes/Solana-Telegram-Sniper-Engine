"""Data models for Telegram user sessions, encrypted wallets, and swap execution."""

from pydantic import BaseModel, Field
from typing import Optional, List


class EncryptedWalletVault(BaseModel):
    public_address: str
    encrypted_private_key_hex: str
    iv_hex: str
    auth_tag_hex: str
    sol_balance: float = 0.0
    created_at_timestamp: int


class TelegramUserSession(BaseModel):
    telegram_user_id: int
    username: str
    wallet: EncryptedWalletVault
    auto_slippage_bps: int = 150  # 1.5%
    auto_tip_mode: str = "VERY_HIGH"  # "MEDIUM" | "HIGH" | "VERY_HIGH"


class SwapOrderRequest(BaseModel):
    order_id: str
    telegram_user_id: int
    token_mint: str
    token_symbol: str
    action: str  # "BUY" | "SELL"
    amount_sol: Optional[float] = None
    token_amount: Optional[float] = None
    slippage_bps: int = 150
    priority_fee_micro_lamports: int = 500_000
    jito_tip_sol: float = 0.01


class ExecutionDispatchReport(BaseModel):
    order_id: str
    telegram_user_id: int
    status: str  # "CONFIRMED" | "REVERTED" | "SLIPPAGE_BREACH"
    transaction_signature: str
    route_used: str  # "Jupiter V6 Direct" | "Raydium CPMM" | "Pump.fun"
    executed_inflow_desc: str
    tokens_received_or_sold: float
    unit_price_usd: float
    total_cost_sol: float
    jito_bundle_id: str
    dispatch_latency_ms: float
    audit_notes: List[str] = Field(default_factory=list)
