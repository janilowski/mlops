from settings import Settings


def test_settings_load_expected_values(monkeypatch):
    # Use dummy values so the test does not depend on local secrets.
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("APP_NAME", "ML API test")
    monkeypatch.setenv("MY_PRECIOUS", "test-secret")

    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ML API test"
    assert settings.MY_PRECIOUS.get_secret_value() == "test-secret"
