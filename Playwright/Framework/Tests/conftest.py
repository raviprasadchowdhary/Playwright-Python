import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def test_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name to run tests against (chromium, firefox, webkit)",
    )
    parser.addoption(
        "--custom-tracing",
        action="store",
        default="on",
        choices=["on", "off"],
        help="Enable or disable Playwright tracing (on/off)",
    )


@pytest.fixture(scope="function")
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    tracing_enabled = request.config.getoption("--custom-tracing") == "on"

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    # Start tracing if enabled
    if tracing_enabled:
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

    yield page

    # Stop tracing and save if enabled
    if tracing_enabled:
        traces_dir = Path(__file__).parent / "traces"
        traces_dir.mkdir(parents=True, exist_ok=True)
        trace_path = str(traces_dir / f"trace_{request.node.name}.zip")
        context.tracing.stop(path=trace_path)
        print(f"\nTrace saved at: {trace_path}")

    context.close()
    browser.close()
