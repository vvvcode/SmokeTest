from configurator.AppiumDriverConfigurator import driver_configurator


def test_appium_driver_configutator():
    driver=driver_configurator('Android', '5.1', '80843ef8', '/Users/risan/Downloads/mobile-dev-v2.3.3-debug.apk')
    contexts = driver.contexts
    for context in contexts:
        print context

