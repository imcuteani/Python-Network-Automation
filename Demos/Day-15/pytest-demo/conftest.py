# Pytest as test automation framework for automated network validation. 
# Pytest allows for network automation to treat infrastructure like software code. 
# Instead of manually typing show commands to check the network status, you can use python libraries to pull 
# network state data and use pytest assertions to instantly flag the failures. 

# Key components for Network testing --- 
# integrating pytest into a Network DevOps workflow involves combining the test runner with dedicated network
# automation library- 

# 1. Data Collection drivers - use libraries like Netmiko(CLI/SSH), Scrapli, PyGNMI(for gnMI/OpenConfig telemetry)to 
# securely pull data from live devices.

# 2. State management for devices - In Pytest, we can use 'yield' keyword which splits the fixture code into Setup and 
# teardown (disconnect), preventing the hung ssh connections on your device hardware. 
# With Pytest the actual device values can be matched with expected configurations. Pytest introspects standard
# python boolean configurations to output readable error logs when a paramater fails validation. 
# 
# 3. For single validation logic - enables running a single validation logic across multiple devices simultaneously. 
#  a single routing test can ingest a list of 50 different IP addresses or interface names and evaluate each seperately. 
# 
# 4. Markers -> Pytest helps to categorize the test based network roles or environments. Teams can use markers like 
# # @pytest.mark.ospf or @pytest.mark.spine to selectively filter and execute test blocks.  
# 5. Pytest configuration - A centralized, local configuration file containing shared fixers, custom command line hooks, global test plugins. 

# Differences between PyATS Framework and Pytest framework 

# 1. Cisco PyATS is an automated network testing, device profiling and configuration verification framework. 
# 1. Pytest is a general purpose software testing tool (unit, functional, API, E2E testing)

# 2. Cisco PyATS allows network engineers and NetDevOps team. 
# 2. PyTest targets software developers and QA automation engineers. 
# 
# 
# 3. PyATS is the complete out-of-the box ecosystem including device drivers and parsers. 
# 3. Pytest is the lean test runner and assertion framework extensible via plugins. 
# 
# 4. PyATS allows native SSH/Telnet terminal control via the unicorn library 
# 4. Pytest requires 3rd-party libraries (Netmiko, Scapy) to touch network hardware. 
# 
# 5. Cisco PyATS has built-in Genie engine to convert raw CLI outputs into structured JSON. 
# 5. Pytest relies on external text parsers like TextFSM or TTP. 
# 
# 6. PyATS is optimized for Cisco platform but limited extensible support to Juniper, Arista and others. 
# 6. Pytest is universally flexible, completely decoupled from network vendors platform and vendor agnostic.
# 
# Real time scenarios to use Cisco PyATS
# -------------------------------------------------------
# choose the PyATS framework when managing physical or virtual network infra 
# a) state diffing - you need to take snapshot of the network route tables or interface statuses before a 
# maintenance window, perform changes and run a differential comparison to catch unintended impacts. 
# 
# b) Multi-vendor Ecosystem - You want to standardize object model (like abstracting BGP or OSPF) across various 
# platforms like Cisco IOS-XE, Juniper Junos or Arista EOS. 
# 
# c) Batteries included network validation - you prefer using thousands of pre-built production grade CLI parsers rather 
# than writing regex to understand network states. 
# 
# Real time scenarios to use PyTest 
# ------------------------------------------------
# choose pytest for standard software testing workflows or lean network validation. 
# 
# 1. application code - you are building python applications, APIs, web scraping tools or internal configuration tools. 
# 2. advanced test architecture - pytest can be used for testing features like native fixtures, heavy parameterization to loop
# tests over multiple data pools, or parallel test execution. 
# 
# 3. minimalist infra checks - when it's needed to run basic API queries (checking a controller endpoint) or ping sweeping without 
# logging into raw device CLI. 
# 
# How both PyATS and PyTest integrate together 
# -------------------------------------------------------
# In real time scenario, it's common practice to wrap PyATS logic directly inside pytest execution environment. 
# 1. pytest acts as overall test runner, handling test layout and environment configuration, generating test dashboard.
# 2. pyATS and Genie are loaded inside pytest fixtures to maintain SSH connectons and retrieve the structured status data 
# # from switches and firewalls. 
# 3. Standard python assert statements inside pytest evaluate whether the infra returned by PyATS matches with the design specifications.     


# configuration to leverage pytest fixtures to reuse network connection objects across the multiple test scenarios
# without repeating code 

import pytest
from scrapli import Scrapli

@pytest.fixture(scope="session")
def router_conn():
    """Establishes a reusable SSH connection to the Cisco IOS router"""
    device = {
        "device_type": "cisco_ios_telnet",
        "host": "192.168.80.128",
        "port": "5008",
        "username": "admin",
        "password": "cisco123",
    }
    with Scrapli(**device) as conn:
        yield conn  # supplies connection object to the tests


# Best Practices for Network Automation with pytest
# -------------------------------------------------------
# state management - the 'yield' keyword splits the fixture code into Setup (connect) and device
# teardown (disconnect) preventing hung SSH sessions on your hardware. 

# Efficiency - Setting "scope='module'" forces pytest to authenticate exactly once for the whole file 
# rather than dropping and recreating the connection for every distinct test block. 

# Clean assertions - Using textfsm=True inside netmiko allows to query real world status using clear 
# python dictionaries instead of brittle regular expressions on raw terminal text. 

