import plotly.graph_objects as go

def plot_race_positions(drivers, positions):
    fig = go.Figure()
    
    for driver in drivers:
        fig.add_trace(go.Scatter(
            x=positions[driver]["x"],
            y=positions[driver]["y"],
            mode="lines+markers",
            name=driver
        ))
    
    fig.update_layout(
        title="🏎️ Real-Time Race Tracking",
        xaxis_title="Track Position (X)",
        yaxis_title="Track Position (Y)",
        paper_bgcolor="black",
        font=dict(color="white")
    )
    
    return fig
