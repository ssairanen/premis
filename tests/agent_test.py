"""Test for the Premis agent class"""

import lxml.etree as ET
import premis.base as p
import premis.agent_base as a

def test_agent():
    """Test agent"""
    agent_id = p.identifier('a', 'b', 'agent')
    agent = a.agent(agent_id, 'c', 'd')
    xml = '<premis:agent xmlns:premis="info:lc/xmlns/premis-v2">' \
          '<premis:agentIdentifier><premis:agentIdentifierType>' \
          'a</premis:agentIdentifierType><premis:agentIdentifierValue>' \
          'b</premis:agentIdentifierValue></premis:agentIdentifier>' \
          '<premis:agentName>c</premis:agentName>' \
          '<premis:agentType>d</premis:agentType></premis:agent>'
    assert ET.tostring(agent) == xml


def test_iter_agents():
    """Test iter_agents"""
    # TODO


def test_agent_count():
    """Test agent_count"""
    # TODO


def test_agents_with_type():
    """Test agents_with_type"""
    # TODO

