"""
function_app.py — Azure Functions entry point for: Support-mailbox-automation
Objective: This workflow addresses the customer inquiry on the orders and respond back to the customer with latest update on the provided order number.

Python v2 programming model.
Wraps orchestrator.run() with two triggers:
  • Timer — runs on schedule: 0 */15 * * * *
            Override by setting WORKFLOW_SCHEDULE in Azure App Settings.
  • HTTP  — POST/GET /api/run  for on-demand invocation.

Run locally:
    func start

Deploy to Azure:
    az functionapp deployment source config-zip ...
"""

import json
import logging
import os

import azure.functions as func

from orchestrator import run  # your existing workflow logic

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
logger = logging.getLogger("workflow.trigger")

# Schedule: override with WORKFLOW_SCHEDULE app setting if needed
_SCHEDULE = os.getenv("WORKFLOW_SCHEDULE", "0 */15 * * * *")


@app.timer_trigger(
    schedule="0 */15 * * * *",  # hardcoded — change WORKFLOW_SCHEDULE app setting and redeploy to adjust
    arg_name="timer",
    run_on_startup=False,
    use_monitor=False,
)
def support_mailbox_automation_scheduled(timer: func.TimerRequest) -> None:
    """Timer trigger — execute 'Support-mailbox-automation' on schedule."""
    if timer.past_due:
        logger.warning("Timer is past due — running immediately.")
    logger.info("Scheduled execution starting.")
    run()
    logger.info("Scheduled execution complete.")


@app.route(route="run", methods=["GET", "POST"])
def support_mailbox_automation_on_demand(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger — invoke 'Support-mailbox-automation' on demand."""
    try:
        body: dict = req.get_json() if req.get_body() else {}
    except (ValueError, TypeError):
        body = {}
    try:
        result = run(body)
        return func.HttpResponse(
            json.dumps(result, default=str),
            mimetype="application/json",
            status_code=200,
        )
    except Exception as exc:
        logger.error("Workflow failed: %s", exc, exc_info=True)
        return func.HttpResponse(
            json.dumps({"error": str(exc)}),
            mimetype="application/json",
            status_code=500,
        )
