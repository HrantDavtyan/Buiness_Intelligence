import dash
import dash_core_components as dcc
import dash_html_components as html

from my_plots import f1

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div([

	# row 1
	html.Div([
		# first 4 columns of row 1
		html.Div([
			html.H1(children='My Application'),
		], className="four columns"),

		# next 6 columns of row 1
		html.Div([
			html.Label("Dropdown"),
			dcc.Dropdown(
				options = [
				{"label":"Google","value":"GOOGL"},
				{"label":"Microsoft","value":"MSFT"},
				{"label":"Apple","value":"AAPL"}
				],
				value = "GOOGL"
				),
		], className="four columns")

	], className="row"),

	# row 2
	html.Div([

		# first 6 columns in row 2
		html.Div([
			dcc.Graph(id="figure_1", figure= f1)
		], className="six columns")

	], className="row")

])


if __name__ == '__main__':
    app.run_server(debug=True)