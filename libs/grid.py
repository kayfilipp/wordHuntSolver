def create_grid(n: int = 3):
    return [[None]*n]*n


def submit_word_grid(st):
    """
    st: streamlit instance
    updates session state with an n*n dictionary
    fails if the edited grid is empty or not all dimensions are edited properly.
    """

    grid: dict = st.session_state.get('temp_grid', None)
    dim: int = st.session_state['grid_dim']

    if not grid:
        st.error("Please provide a grid.")
        return

    edited_rows: dict = grid['edited_rows']
    rows = edited_rows.keys()

    # fail if the number of edited rows or columns is != n
    if len(rows) != dim:
        st.error("Please insert one letter into each cell.")
        return

    # concurrently check if each row has the correct number of edited cells and load it into a new data structure
    for i in range(0, dim):
        for j in range(0, dim):
            cell = edited_rows[i].get(str(j), '')
            if len(cell) != 1 or not cell.isalpha():
                st.error("Please insert one letter into each cell.")
                return

            edited_rows[i][str(j)] = str(cell).lower()

    st.session_state['grid'] = edited_rows


def render_table(st):
    """Takes the grid element and plots it in streamlit instance"""
    grid = st.session_state['grid']
    dim = st.session_state['grid_dim']
    html = """
        <style>
            table, th, td {
              border:1px solid black;
            }
            td {
                text-align: center
            }
        </style>
        <table style='width:100%' table-layout:'fixed' border='2'>
    """

    for i in range(0, dim):
        td = [f"<td>{grid[i][str(j)]}</td>" for j in range(0,dim)]
        td = "".join(td)
        html += f"<tr>{td}</tr>"

    html+="</table>"
    st.html(html)


def transform_grid(st):
    """Transforms grid from a row * column to a column * row struc"""
    grid = st.session_state['grid']
    dim = st.session_state['grid_dim']
    rows = []

    for i in range(0,dim):
        columns = []
        for j in range(0,dim):
            columns.append(grid[j][str(i)])
        rows.append(columns)

    st.session_state['grid_final'] = rows
