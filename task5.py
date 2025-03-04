import pytest
from dash import Dash
from dash.testing.application_runners import import_app
import dash_html_components as html
import dash_core_components as dcc

# Import the app from your Dash app file (for example, `app.py`)
# Make sure to import your Dash app correctly
from app import app  # Import your app here

@pytest.fixture
def test_app():
    # Use the imported app to create a test client
    app.config['TESTING'] = True
    return app.server

# Test 1: Check if the header is present
def test_header(test_app):
    # Run the app in the test client
    # Find the header by its HTML tag (assuming it's an H1)
    header = test_app.layout.find_element('h1')
    # Assert that the header contains the text 'Sales Visualizer for Soul Foods'
    assert header.text == 'Sales Visualizer for Soul Foods'

# Test 2: Check if the visualization (graph) is present
def test_visualization(test_app):
    # Find the graph by its component ID
    graph = test_app.layout.find_element('#sales-line-chart')
    # Assert that the graph is present (it should have a specific tag or id)
    assert graph is not None

# Test 3: Check if the region picker (radio button) is present
def test_region_picker(test_app):
    # Find the radio button component by its ID
    region_picker = test_app.layout.find_element('#region-selector')
    # Assert that the radio button is present
    assert region_picker is not None
